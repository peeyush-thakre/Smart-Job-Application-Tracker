import sqlite3
from datetime import datetime

DB_NAME = "job_tracker.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company TEXT NOT NULL,
            job_role TEXT NOT NULL,
            location TEXT,
            job_type TEXT,
            salary TEXT,
            application_date TEXT,
            status TEXT DEFAULT 'Applied',
            job_url TEXT,
            notes TEXT,
            created_at TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER NOT NULL,
            interview_date TEXT,
            round TEXT,
            status TEXT,
            notes TEXT,
            FOREIGN KEY (application_id)
            REFERENCES applications(id)
            ON DELETE CASCADE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS followups (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_id INTEGER NOT NULL,
            followup_date TEXT,
            notes TEXT,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (application_id)
            REFERENCES applications(id)
            ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


# --------------------------------------------------
# APPLICATION FUNCTIONS
# --------------------------------------------------

def add_application(
    company,
    job_role,
    location,
    job_type,
    salary,
    application_date,
    status,
    job_url,
    notes
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO applications
        (
            company,
            job_role,
            location,
            job_type,
            salary,
            application_date,
            status,
            job_url,
            notes,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        company,
        job_role,
        location,
        job_type,
        salary,
        application_date,
        status,
        job_url,
        notes,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_applications():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM applications
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def get_application(application_id):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM applications
        WHERE id = ?
    """, (application_id,))

    data = cursor.fetchone()

    conn.close()

    return data


def update_application(
    application_id,
    company,
    job_role,
    location,
    job_type,
    salary,
    application_date,
    status,
    job_url,
    notes
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE applications
        SET
            company = ?,
            job_role = ?,
            location = ?,
            job_type = ?,
            salary = ?,
            application_date = ?,
            status = ?,
            job_url = ?,
            notes = ?
        WHERE id = ?
    """, (
        company,
        job_role,
        location,
        job_type,
        salary,
        application_date,
        status,
        job_url,
        notes,
        application_id
    ))

    conn.commit()
    conn.close()


def delete_application(application_id):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM applications
        WHERE id = ?
    """, (application_id,))

    conn.commit()
    conn.close()


# --------------------------------------------------
# INTERVIEW FUNCTIONS
# --------------------------------------------------

def add_interview(
    application_id,
    interview_date,
    round_name,
    status,
    notes
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO interviews
        (
            application_id,
            interview_date,
            round,
            status,
            notes
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        application_id,
        interview_date,
        round_name,
        status,
        notes
    ))

    conn.commit()
    conn.close()


def get_interviews():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            interviews.id,
            applications.company,
            applications.job_role,
            interviews.interview_date,
            interviews.round,
            interviews.status,
            interviews.notes
        FROM interviews
        JOIN applications
        ON interviews.application_id = applications.id
        ORDER BY interviews.interview_date DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def update_interview_status(interview_id, status):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE interviews
        SET status = ?
        WHERE id = ?
    """, (status, interview_id))

    conn.commit()
    conn.close()


# --------------------------------------------------
# FOLLOW-UP FUNCTIONS
# --------------------------------------------------

def add_followup(
    application_id,
    followup_date,
    notes
):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO followups
        (
            application_id,
            followup_date,
            notes
        )
        VALUES (?, ?, ?)
    """, (
        application_id,
        followup_date,
        notes
    ))

    conn.commit()
    conn.close()


def get_followups():
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            followups.id,
            applications.company,
            applications.job_role,
            followups.followup_date,
            followups.notes,
            followups.status
        FROM followups
        JOIN applications
        ON followups.application_id = applications.id
        ORDER BY followups.followup_date
    """)

    data = cursor.fetchall()

    conn.close()

    return data


def update_followup_status(followup_id, status):
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        UPDATE followups
        SET status = ?
        WHERE id = ?
    """, (status, followup_id))

    conn.commit()
    conn.close()