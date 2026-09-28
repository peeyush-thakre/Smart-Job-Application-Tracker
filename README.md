# 💼 Smart Job Application Tracker

A simple and interactive **Job Application Tracking System** built using **Python, SQLite, and Streamlit**.

The application helps users manage job applications, track interview rounds, schedule follow-ups, view application statistics, and export application data as a CSV file.

---

## 🚀 Features

### 🏠 Dashboard

* View total job applications
* Track Applied applications
* Track Pending applications
* Track Interview applications
* Track Selected applications
* Track Rejected applications
* View recent applications

### ➕ Add Application

Add complete job application details:

* Company Name
* Job Role
* Location
* Job Type
* Salary
* Application Date
* Application Status
* Job URL
* Notes

### 📋 Application Management

* View all applications
* Search applications by company or job role
* Filter applications by status
* Delete applications
* View application details

### ✏️ Edit Application

Update existing application information:

* Company
* Job Role
* Location
* Job Type
* Salary
* Application Date
* Status
* Job URL
* Notes

### 🎯 Interview Tracker

Track interview information including:

* Company
* Job Role
* Interview Date
* Interview Round
* Interview Status
* Interview Notes

Supported interview rounds:

* HR Round
* Technical Round
* Coding Round
* Managerial Round
* Final Round

### 🔔 Follow-Up Tracker

Manage follow-up activities:

* Follow-up Date
* Company
* Job Role
* Follow-up Notes
* Follow-up Status

### 📊 Reports

Generate simple application reports:

* Application status distribution
* Applications by job type
* Application statistics

### 📥 CSV Export

Download all job application records as a CSV file for backup or further analysis.

---

# 🛠️ Tech Stack

| Technology | Purpose                     |
| ---------- | --------------------------- |
| Python     | Application logic           |
| Streamlit  | User interface              |
| SQLite     | Database                    |
| Pandas     | Data handling and reporting |

---

# 📂 Project Structure

```text
Smart-Job-Application-Tracker/
│
├── app.py
│
├── database.py
│
├── requirements.txt
│
├── job_tracker.db
│
└── README.md
```

### File Description

**`app.py`**

Main Streamlit application containing:

* Dashboard
* Application management
* Interview tracker
* Follow-up tracker
* Reports
* CSV export

**`database.py`**

Handles:

* SQLite connection
* Database creation
* Table creation
* INSERT operations
* SELECT operations
* UPDATE operations
* DELETE operations
* Interview management
* Follow-up management

**`requirements.txt`**

Contains the required Python packages.

**`job_tracker.db`**

SQLite database file created automatically when the application runs.

---

# 🗄️ Database Design

The application uses SQLite with three main tables.

## Applications

```text
applications
│
├── id
├── company
├── job_role
├── location
├── job_type
├── salary
├── application_date
├── status
├── job_url
├── notes
└── created_at
```

## Interviews

```text
interviews
│
├── id
├── application_id
├── interview_date
├── round
├── status
└── notes
```

## Follow-ups

```text
followups
│
├── id
├── application_id
├── followup_date
├── notes
└── status
```

The `application_id` connects interviews and follow-ups with the corresponding job application.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/your-username/Smart-Job-Application-Tracker.git
```

Move into the project directory:

```bash
cd Smart-Job-Application-Tracker
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

Or install directly:

```bash
pip install streamlit pandas
```

---

# ▶️ Run the Application

Run the following command:

```bash
streamlit run app.py
```

The application will open in your browser.

Default Streamlit address:

```text
http://localhost:8501
```

---

# 🖥️ Application Workflow

```text
             ┌─────────────────┐
             │     Dashboard   │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ Add Application │
             └────────┬────────┘
                      │
                      ▼
             ┌─────────────────┐
             │ SQLite Database │
             └────────┬────────┘
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Applications  Interviews  Follow-ups
          │           │           │
          └───────────┼───────────┘
                      ▼
             ┌─────────────────┐
             │     Reports     │
             └────────┬────────┘
                      │
                      ▼
                CSV Export
```

---

# 🔑 Main Python Concepts Used

This project demonstrates several important Python concepts:

### Python

* Functions
* Modules
* Dictionaries
* Lists
* Exception handling
* Date and time handling
* Conditional statements
* Loops
* File handling

### SQLite

* Database connection
* Creating tables
* INSERT
* SELECT
* UPDATE
* DELETE
* WHERE
* JOIN
* Foreign Keys
* Parameterized queries

### Streamlit

* `st.title()`
* `st.sidebar`
* `st.form()`
* `st.text_input()`
* `st.selectbox()`
* `st.date_input()`
* `st.button()`
* `st.metric()`
* `st.dataframe()`
* `st.download_button()`
* `st.session_state`
* `st.rerun()`

### Pandas

* DataFrame creation
* Filtering
* Value counts
* CSV export
* Data visualization

---

# 📸 Screenshots

Add screenshots of your application here after running it.

Example:

```text
screenshots/
│
├── dashboard.png
├── add-application.png
├── applications.png
├── interview-tracker.png
└── reports.png
```

Then add them to this README:

```markdown
![Dashboard](screenshots/dashboard.png)

![Applications](screenshots/applications.png)
```

---

# 💡 Future Improvements

Possible future features include:

* User authentication
* Password protection
* Email reminders
* Interview calendar
* Resume management
* Job description storage
* Application success-rate calculation
* Dark mode
* Advanced analytics
* Automatic follow-up reminders
* PDF report generation

---

# 🎯 Project Objectives

The main objective of this project is to create a simple system for managing the complete job application process.

It demonstrates how **Python can be combined with SQLite and Streamlit** to build a functional database-driven application without requiring a separate backend framework.

---

# 👨‍💻 Author

**Peeyush Thakre**

B.Tech Computer Science Engineering

### GitHub

https://github.com/peeyush-thakre

### LinkedIn

https://www.linkedin.com/in/peeyush-thakre-91b20a251/

---

# 📄 License

This project is created for **educational and portfolio purposes**.

You are free to modify and improve the project for learning and personal use.

---

## ⭐ If you find this project useful

Give the repository a ⭐ on GitHub and feel free to improve the project with additional features.
