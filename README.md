# 🎮 Choose Your Own Adventure

An AI-powered interactive storytelling web application where users create unique adventures by making choices. The application uses Google Gemini AI to generate dynamic story paths, making every playthrough different.

---

## 📌 Project Overview

Choose Your Own Adventure is a full-stack web application that allows users to experience AI-generated interactive stories. Every decision made by the user influences the storyline, creating a unique and engaging experience.

---

## ✨ Features

- 🤖 AI-powered story generation using Google Gemini
- 📖 Dynamic branching story paths
- 🎯 Multiple choices at every stage
- ⚡ FastAPI REST API backend
- 💻 React + Vite frontend
- 🗄️ SQLite database
- 🔄 Background story generation

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- CSS
- Axios

### Backend
- FastAPI
- Python
- SQLAlchemy
- SQLite
- LangChain
- Google Gemini API

---

## 📂 Project Structure

```text
Choose-your-own-adventure/
│
├── Frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── backend/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── main.py
│   └── pyproject.toml
│
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Choose-your-own-adventure.git
cd Choose-your-own-adventure
```
## ⚠️ Note

To run this project, add your own **Google Gemini API Key** in the `backend/.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

After that, run the backend and frontend normally.
---

### 2. Run the Backend

```bash
cd backend

uv sync

uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

API Documentation:

```
http://127.0.0.1:8000/docs
```

---

### 3. Run the Frontend

Open a new terminal.

```bash
cd Frontend

npm install

npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

## 📸 Screenshots

### Backend

<p align="center">
  <img src="https://github.com/user-attachments/assets/b85402f6-cdd7-4113-9a2f-afd258f1db41" width="700">
</p>

---

### Frontend

#### 1. Home Page

<p align="center">
  <img src="https://github.com/user-attachments/assets/8a02dd88-c6aa-4235-8959-b128de1a84c8" width="500">
</p>

#### 2. Story Generation

<p align="center">
  <img src="https://github.com/user-attachments/assets/555bad3f-44fc-41aa-b755-8f18f9e447ea" width="500">
</p>

#### 3. Story Choices

<p align="center">
  <img src="https://github.com/user-attachments/assets/4fed7590-0152-4e69-bcde-34f26b402503" width="500">
</p>

#### 4. Story Progress

<p align="center">
  <img src="https://github.com/user-attachments/assets/13599015-ecc2-4869-b923-0e00877b525a" width="500">
</p>

#### 5. Story Ending

<p align="center">
  <img src="https://github.com/user-attachments/assets/5af6c640-f3bc-41dc-a6de-a7892b400850" width="500">
</p>
Example:

- Home Page
- Story Generation
- Story Choices
- Generated Adventure

---

## ⚠️ Challenges Faced

- Integrating Google Gemini API
- Handling API quota limits
- Parsing AI-generated JSON responses
- Background task processing
- Connecting React frontend with FastAPI backend
- Managing Git and GitHub repositories

---

## 📚 What We Learned

- Full Stack Web Development
- REST API Development
- AI Integration with Gemini
- LangChain Prompt Engineering
- Database Management
- Git & GitHub
- Debugging Real-World Applications

---

## 🔮 Future Enhancements

- User Authentication
- Save and Resume Stories
- Multiple Story Themes
- Story Sharing
- Dark Mode
- Story History

---

## 👨‍💻 Developed By

**Senthamil Selvan J**

B.Tech Artificial Intelligence & Data Science

Vel Tech Multi Tech Dr. Rangarajan Dr. Sakunthala Engineering College

---

## 📜 License

This project is developed for educational and portfolio purposes only.
