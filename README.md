# Flask Mini Projects 🚀

This repository contains two simple Flask-based projects:

1. **Flask JSON API**
2. **Flask Form with MongoDB Atlas Integration**

---

## 📁 Project Overview

### 1️⃣ Flask JSON API

* Exposes an `/api` endpoint
* Reads data from a local `data.json` file
* Returns the data as a JSON response

---

### 2️⃣ Flask Form + MongoDB Atlas

* Frontend form to collect user data (name & email)
* Submits data to Flask backend
* Stores data in MongoDB Atlas
* Redirects to success page on successful submission
* Displays error on same page if submission fails

---

## 🛠️ Tech Stack

* Python 3
* Flask
* MongoDB Atlas
* PyMongo
* HTML (Jinja Templates)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

---

### 2. Create virtual environment

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/test_db?retryWrites=true&w=majority
```

⚠️ Important:

* Replace `<username>`, `<password>`, `<cluster-url>`
* If your password contains special characters (like `@`), encode them:

  * `@` → `%40`

---

## ▶️ Running the Projects

### Run Flask App

```bash
python app.py
```

App will run on:

```
http://127.0.0.1:5000/
```

---

## 🌐 Available Routes

### 📌 JSON API

```
GET /api
```

Returns data from `data.json`

---

### 📌 Form UI

```
GET /
```

Displays form

---

### 📌 Submit Form

```
POST /submit
```

* Inserts data into MongoDB
* Redirects to `/success` on success
* Shows error on same page if failed

---

### 📌 Success Page

```
GET /success
```

Displays:

```
Data submitted successfully
```

---

## 🧪 Testing

### API Test

```
http://127.0.0.1:5000/api
```

### Form Test

* Open homepage
* Submit form
* Check MongoDB Atlas for inserted data

---

## ⚠️ Common Issues

### 1. Authentication Failed

* Check MongoDB username/password
* Encode special characters in password

---

### 2. Data Not Showing in Atlas

* Ensure correct database name (`test_db`)
* MongoDB creates DB only after first insert

---

### 3. Connection Issues

* Add IP in MongoDB Atlas:

```
0.0.0.0/0
```

---

### 4. `.env` Not Loading

* Ensure `.env` is in root directory
* Use `load_dotenv()` in code

---

## 📌 Notes

* Do not commit `.env` file to GitHub
* Add `.env` to `.gitignore`
* This is a beginner-friendly project for learning Flask + MongoDB integration

---

## 🎯 Future Improvements

* Add validation and authentication
* Use AJAX for form submission
* Add frontend styling (Bootstrap)
* Deploy on AWS / Azure

---

## 👨‍💻 Author

Siddharth Tiwari

---
