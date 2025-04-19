# 🔍 Follow-Tracker

**Follow-Tracker** is a Python-based automation tool that automates browser interactions using Selenium to collect data from your followers and following lists on INSTAGRAM, then compares them to highlight non-followers.

---

## 🚀 Features

- ✅ **Automated Login**: Log in securely using your Instagram credentials.
- 🔄 **Smart Scrolling**: Dynamically scrolls through Instagram’s infinite follower/following lists to fetch all data.
- 🔍 **Accurate Comparison**: Compares both lists to find users who don’t follow you back.
- 📄 **Clean Output**: Displays a list of non-followers on the terminal.
- 🌐 **Modular & Maintainable Codebase**

---

## 🧑‍💻 Tech Stack

- **Language**: Python
- **Automation**: Selenium
- **Browser Support**: Chrome (via ChromeDriver)
- **Others**: BeautifulSoup (Optional for HTML parsing), Time module

---

## 📦 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/oshinrastogi/Follow-Tracker.git
cd Follow-Tracker
```

## Create Virtual Environment (Optional but Recommended)
python -m venv venv

## Install Dependencies
```bash
pip install selenium BeautifulSoup pandas
```
## Download ChromeDriver
- Make sure the ChromeDriver version matches your Chrome browser version.
- Either place it in the project directory or add its path to your system environment variables.
- VS Code may automatically detect and add path to ChromeDrive

## Run the Script
```
python unfollower_checker.py
```

## Disclaimer
- This project is intended strictly for educational and personal use only.
- Instagram’s front-end is highly dynamic. HTML structures and class names may change frequently, which can break automation. Always inspect the current UI before use.
- This tool does not use the Instagram API, and operates by simulating real-user interactions via browser automation.
- This project does not store your credentials. All actions are performed within your local machine.
- Use this tool responsibly. Do not violate Instagram’s Terms of Service.

  




