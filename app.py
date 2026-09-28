import streamlit as st
import pandas as pd
from datetime import date

from database import (
    create_tables,
    add_application,
    get_applications,
    get_application,
    update_application,
    delete_application,
    add_interview,
    get_interviews,
    update_interview_status,
    add_followup,
    get_followups,
    update_followup_status
)


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Smart Job Application Tracker",
    page_icon="💼",
    layout="wide"
)


# ==========================================================
# DATABASE INITIALIZATION
# ==========================================================

create_tables()


# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 0px;
}

.subtitle {
    color: gray;
    font-size: 17px;
    margin-bottom: 25px;
}

.metric-card {
    padding: 15px;
    border-radius: 10px;
    background-color: #f5f7fa;
}

</style>
""", unsafe_allow_html=True)


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("💼 Job Tracker")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "➕ Add Application",
        "📋 Applications",
        "✏️ Edit Application",
        "🎯 Interviews",
        "🔔 Follow-ups",
        "📊 Reports"
    ]
)


# ==========================================================
# GET APPLICATION DATA
# ==========================================================

applications = get_applications()

application_df = pd.DataFrame(
    [dict(row) for row in applications]
)


# ==========================================================
# DASHBOARD
# ==========================================================

if menu == "🏠 Dashboard":

    st.markdown(
        '<div class="main-title">💼 Smart Job Application Tracker</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Track your job applications, interviews and follow-ups.</div>',
        unsafe_allow_html=True
    )

    # ------------------------------------------
    # METRICS
    # ------------------------------------------

    total = len(application_df)

    if total > 0:

        applied = len(
            application_df[
                application_df["status"] == "Applied"
            ]
        )

        interview = len(
            application_df[
                application_df["status"] == "Interview"
            ]
        )

        selected = len(
            application_df[
                application_df["status"] == "Selected"
            ]
        )

        rejected = len(
            application_df[
                application_df["status"] == "Rejected"
            ]
        )

        pending = len(
            application_df[
                application_df["status"] == "Pending"
            ]
        )

    else:

        applied = 0
        interview = 0
        selected = 0
        rejected = 0
        pending = 0

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    col1.metric("Total", total)
    col2.metric("Applied", applied)
    col3.metric("Interview", interview)
    col4.metric("Selected", selected)
    col5.metric("Rejected", rejected)
    col6.metric("Pending", pending)

    st.divider()

    # ------------------------------------------
    # RECENT APPLICATIONS
    # ------------------------------------------

    st.subheader("📋 Recent Applications")

    if total > 0:

        recent = application_df[
            [
                "company",
                "job_role",
                "location",
                "status",
                "application_date"
            ]
        ].head(10)

        st.dataframe(
            recent,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No applications yet. Go to 'Add Application' to add your first application."
        )


# ==========================================================
# ADD APPLICATION
# ==========================================================

elif menu == "➕ Add Application":

    st.title("➕ Add Job Application")

    with st.form("application_form"):

        col1, col2 = st.columns(2)

        with col1:

            company = st.text_input(
                "Company Name *"
            )

            job_role = st.text_input(
                "Job Role *"
            )

            location = st.text_input(
                "Location"
            )

            job_type = st.selectbox(
                "Job Type",
                [
                    "Full Time",
                    "Part Time",
                    "Internship",
                    "Contract",
                    "Remote"
                ]
            )

        with col2:

            salary = st.text_input(
                "Salary"
            )

            application_date = st.date_input(
                "Application Date",
                value=date.today()
            )

            status = st.selectbox(
                "Application Status",
                [
                    "Applied",
                    "Pending",
                    "Interview",
                    "Selected",
                    "Rejected"
                ]
            )

            job_url = st.text_input(
                "Job URL"
            )

        notes = st.text_area(
            "Notes"
        )

        submitted = st.form_submit_button(
            "💾 Save Application"
        )

        if submitted:

            if company.strip() == "":
                st.error("Company name is required.")

            elif job_role.strip() == "":
                st.error("Job role is required.")

            else:

                add_application(
                    company,
                    job_role,
                    location,
                    job_type,
                    salary,
                    str(application_date),
                    status,
                    job_url,
                    notes
                )

                st.success(
                    "Job application added successfully!"
                )

                st.rerun()


# ==========================================================
# APPLICATIONS
# ==========================================================

elif menu == "📋 Applications":

    st.title("📋 Job Applications")

    applications = get_applications()

    df = pd.DataFrame(
        [dict(row) for row in applications]
    )

    if df.empty:

        st.info("No applications found.")

    else:

        # ------------------------------------------
        # SEARCH
        # ------------------------------------------

        search = st.text_input(
            "🔍 Search Company or Job Role"
        )

        if search:

            df = df[
                df["company"].str.contains(
                    search,
                    case=False,
                    na=False
                )
                |
                df["job_role"].str.contains(
                    search,
                    case=False,
                    na=False
                )
            ]

        # ------------------------------------------
        # FILTER
        # ------------------------------------------

        status_filter = st.selectbox(
            "Filter by Status",
            [
                "All",
                "Applied",
                "Pending",
                "Interview",
                "Selected",
                "Rejected"
            ]
        )

        if status_filter != "All":

            df = df[
                df["status"] == status_filter
            ]

        st.dataframe(
            df[
                [
                    "id",
                    "company",
                    "job_role",
                    "location",
                    "job_type",
                    "salary",
                    "application_date",
                    "status"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

        # ------------------------------------------
        # DELETE
        # ------------------------------------------

        st.subheader("🗑️ Delete Application")

        delete_id = st.number_input(
            "Application ID",
            min_value=1,
            step=1
        )

        if st.button("Delete Application"):

            application = get_application(
                delete_id
            )

            if application:

                delete_application(
                    delete_id
                )

                st.success(
                    "Application deleted successfully."
                )

                st.rerun()

            else:

                st.error(
                    "Application ID not found."
                )


# ==========================================================
# EDIT APPLICATION
# ==========================================================

elif menu == "✏️ Edit Application":

    st.title("✏️ Edit Application")

    applications = get_applications()

    if not applications:

        st.info("No applications available.")

    else:

        application_ids = [
            row["id"]
            for row in applications
        ]

        selected_id = st.selectbox(
            "Select Application ID",
            application_ids
        )

        application = get_application(
            selected_id
        )

        if application:

            with st.form("edit_form"):

                col1, col2 = st.columns(2)

                with col1:

                    company = st.text_input(
                        "Company",
                        value=application["company"]
                    )

                    job_role = st.text_input(
                        "Job Role",
                        value=application["job_role"]
                    )

                    location = st.text_input(
                        "Location",
                        value=application["location"] or ""
                    )

                    job_type = st.selectbox(
                        "Job Type",
                        [
                            "Full Time",
                            "Part Time",
                            "Internship",
                            "Contract",
                            "Remote"
                        ],
                        index=[
                            "Full Time",
                            "Part Time",
                            "Internship",
                            "Contract",
                            "Remote"
                        ].index(
                            application["job_type"]
                        )
                        if application["job_type"]
                        in [
                            "Full Time",
                            "Part Time",
                            "Internship",
                            "Contract",
                            "Remote"
                        ]
                        else 0
                    )

                with col2:

                    salary = st.text_input(
                        "Salary",
                        value=application["salary"] or ""
                    )

                    application_date = st.date_input(
                        "Application Date",
                        value=pd.to_datetime(
                            application["application_date"]
                        ).date()
                    )

                    statuses = [
                        "Applied",
                        "Pending",
                        "Interview",
                        "Selected",
                        "Rejected"
                    ]

                    current_status = application["status"]

                    status_index = (
                        statuses.index(current_status)
                        if current_status in statuses
                        else 0
                    )

                    status = st.selectbox(
                        "Status",
                        statuses,
                        index=status_index
                    )

                    job_url = st.text_input(
                        "Job URL",
                        value=application["job_url"] or ""
                    )

                notes = st.text_area(
                    "Notes",
                    value=application["notes"] or ""
                )

                update = st.form_submit_button(
                    "🔄 Update Application"
                )

                if update:

                    update_application(
                        selected_id,
                        company,
                        job_role,
                        location,
                        job_type,
                        salary,
                        str(application_date),
                        status,
                        job_url,
                        notes
                    )

                    st.success(
                        "Application updated successfully!"
                    )

                    st.rerun()


# ==========================================================
# INTERVIEWS
# ==========================================================

elif menu == "🎯 Interviews":

    st.title("🎯 Interview Tracker")

    applications = get_applications()

    if not applications:

        st.warning(
            "Add a job application first."
        )

    else:

        with st.form("interview_form"):

            application_options = {
                f'{row["id"]} - {row["company"]} - {row["job_role"]}':
                row["id"]
                for row in applications
            }

            selected_application = st.selectbox(
                "Job Application",
                list(application_options.keys())
            )

            application_id = application_options[
                selected_application
            ]

            interview_date = st.date_input(
                "Interview Date",
                value=date.today()
            )

            round_name = st.selectbox(
                "Interview Round",
                [
                    "HR Round",
                    "Technical Round",
                    "Coding Round",
                    "Managerial Round",
                    "Final Round"
                ]
            )

            interview_status = st.selectbox(
                "Interview Status",
                [
                    "Scheduled",
                    "Completed",
                    "Passed",
                    "Failed",
                    "Rescheduled"
                ]
            )

            notes = st.text_area(
                "Interview Notes"
            )

            submit = st.form_submit_button(
                "💾 Save Interview"
            )

            if submit:

                add_interview(
                    application_id,
                    str(interview_date),
                    round_name,
                    interview_status,
                    notes
                )

                st.success(
                    "Interview added successfully!"
                )

                st.rerun()

    st.divider()

    st.subheader("📅 Interview History")

    interviews = get_interviews()

    if interviews:

        interview_df = pd.DataFrame(
            [dict(row) for row in interviews]
        )

        st.dataframe(
            interview_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No interviews recorded."
        )


# ==========================================================
# FOLLOW-UPS
# ==========================================================

elif menu == "🔔 Follow-ups":

    st.title("🔔 Follow-up Tracker")

    applications = get_applications()

    if not applications:

        st.warning(
            "Add a job application first."
        )

    else:

        with st.form("followup_form"):

            application_options = {
                f'{row["id"]} - {row["company"]} - {row["job_role"]}':
                row["id"]
                for row in applications
            }

            selected_application = st.selectbox(
                "Job Application",
                list(application_options.keys())
            )

            application_id = application_options[
                selected_application
            ]

            followup_date = st.date_input(
                "Follow-up Date",
                value=date.today()
            )

            notes = st.text_area(
                "Follow-up Notes"
            )

            submit = st.form_submit_button(
                "💾 Save Follow-up"
            )

            if submit:

                add_followup(
                    application_id,
                    str(followup_date),
                    notes
                )

                st.success(
                    "Follow-up added successfully!"
                )

                st.rerun()

    st.divider()

    st.subheader("🔔 Follow-up List")

    followups = get_followups()

    if followups:

        followup_df = pd.DataFrame(
            [dict(row) for row in followups]
        )

        st.dataframe(
            followup_df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No follow-ups recorded."
        )


# ==========================================================
# REPORTS
# ==========================================================

elif menu == "📊 Reports":

    st.title("📊 Application Reports")

    applications = get_applications()

    df = pd.DataFrame(
        [dict(row) for row in applications]
    )

    if df.empty:

        st.info(
            "Add applications to generate reports."
        )

    else:

        # ------------------------------------------
        # STATUS REPORT
        # ------------------------------------------

        st.subheader(
            "Application Status Distribution"
        )

        status_count = (
            df["status"]
            .value_counts()
            .reset_index()
        )

        status_count.columns = [
            "Status",
            "Count"
        ]

        st.bar_chart(
            status_count.set_index("Status")
        )

        # ------------------------------------------
        # JOB TYPE REPORT
        # ------------------------------------------

        st.subheader(
            "Applications by Job Type"
        )

        job_type_count = (
            df["job_type"]
            .value_counts()
            .reset_index()
        )

        job_type_count.columns = [
            "Job Type",
            "Count"
        ]

        st.bar_chart(
            job_type_count.set_index("Job Type")
        )

        # ------------------------------------------
        # EXPORT CSV
        # ------------------------------------------

        st.subheader(
            "📥 Export Applications"
        )

        csv_data = df.to_csv(
            index=False
        ).encode("utf-8")

        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name="job_applications.csv",
            mime="text/csv"
        )