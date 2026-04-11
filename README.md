# 🐦 TWEET

> A Twitter-like social media web application built with **Django** — post tweets, manage your account, and interact with content in a clean, modern interface.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-green?logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 Authentication | Register, Login, Logout using Django's built-in auth |
| 📝 Tweets | Create and delete your own tweets |
| 👤 User Profiles | View tweets per user |
| 📷 Image Upload | Attach images to tweets via Pillow |
| 🎨 Custom UI | Modern, styled frontend with Django templates & custom CSS |
| 🛡️ CSRF Protected | All forms secured by Django's CSRF middleware |

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2 |
| Frontend | HTML5, CSS3, Django Templates |
| Database | SQLite (dev) |
| Static Files | WhiteNoise |
| Server | Gunicorn |
| Image Handling | Pillow |
| Env Config | python-dotenv |

---

## 📁 Project Structure

```
TWEET/
├── project_tweet/          # Django project config
│   ├── settings.py         # App settings (env-aware)
│   ├── urls.py             # Root URL configuration
│   ├── wsgi.py             # WSGI entry point
│   └── asgi.py             # ASGI entry point
│
├── tweet/                  # Main app
│   ├── models.py           # Tweet data model
│   ├── views.py            # CRUD views
│   ├── forms.py            # Tweet form
│   ├── urls.py             # App-level URLs
│   ├── admin.py            # Admin panel config
│   └── templates/          # App-specific templates
│
├── templates/              # Shared templates (login, register, etc.)
│   └── registration/
│
├── static/                 # CSS, JS, images
│   └── css/styles.css
│
├── manage.py               # Django management CLI
├── requirements.txt        # Python dependencies
├── Procfile                # Gunicorn start command (Render/Heroku)
├── build.sh                # Render build script
└── .env                    # Local environment variables (not committed)
```

---

## ⚙️ Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/TWEET.git
cd TWEET
```

### 2. Create a virtual environment & activate it

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```bash
cp .env.example .env
```

Edit `.env` with your values:

```env
SECRET_KEY=your-very-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1
```

### 5. Run migrations & start the server

```bash
python manage.py migrate
python manage.py runserver
```

Visit http://127.0.0.1:8000 🚀

---

## 🌍 Deployment (Render)

This project is configured to deploy on [Render](https://render.com) with zero extra configuration.

### Steps

1. Push your code to GitHub.
2. Go to [Render Dashboard](https://dashboard.render.com) → **New Web Service**.
3. Connect your GitHub repository.
4. Set the following:

| Setting | Value |
|---|---|
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn project_tweet.wsgi:application` |
| **Python Version** | `3.12` |

5. Add these **Environment Variables** in Render:

| Variable | Value |
|---|---|
| `SECRET_KEY` | generate a new 50-char random key |
| `DEBUG` | `False` |
| `ALLOWED_HOSTS` | `your-app-name.onrender.com` |
| `PYTHON_VERSION` | `3.12.0` |

6. Click **Deploy** — Render runs `build.sh` which installs deps, collects static files, and migrates the DB.

> **Note:** Render's free tier uses SQLite on an ephemeral disk. Data resets on each deploy. For persistent data, add a **PostgreSQL** database from the Render dashboard and set `DATABASE_URL`.

---

## 🔑 Environment Variables Reference

| Variable | Required | Default | Description |
|---|---|---|---|
| `SECRET_KEY` | ✅ prod | insecure dev key | Django secret key |
| `DEBUG` | ❌ | `True` | Set to `False` in production |
| `ALLOWED_HOSTS` | ✅ prod | `localhost 127.0.0.1` | Space-separated allowed host names |

---

## 🧑‍💻 Development Commands

```bash
# Run dev server
python manage.py runserver

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser (admin)
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic
```

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙋 Author

Built with ❤️ by **Srijan** — feel free to fork, star, and contribute!
