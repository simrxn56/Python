# 📚 Library Management System

A clean, extensible, and modular **Python-based Library Management System** designed for small to medium-scale educational institutions and public libraries. This project uses **CSV files as a lightweight database** to manage book inventories, member registration, and borrowing/returning transactions via a command-line interface (CLI).

---

## ✅ Features

- 👥 Member registration with auto-generated IDs  
- 📖 Add, borrow, and return books  
- 🧾 Transaction logging (`entry.csv`)  
- 📚 Real-time inventory update (`book.csv`)  
- 🛡️ Basic input validation and error handling  
- 🔍 Easy to read, extensible OOP design  

---

## 📦 Project Structure

```bash
library-management/
│
├── library.py        # Core application logic
├── book.csv          # Book inventory database
├── entry.csv         # Member transaction history
├── README.md         # Documentation
```

---

## 🛠️Tech Stack

| Technology | Purpose |
| --- | --- |
| Python 3.x | Core programming language |
| CSV |  Lightweight data storage |
| datetime | Borrow/return due tracking |

---

## 🚀 Getting Started

### 🔧 Prequisites
Ensure you have Python 3 installed:
```bash
python --version
```

### 📂 Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/simrxn56/my-python-projects.git
   cd my-python-projects/library
   ```
   
2. Ensure `book.csv` and `entry.csv` exist in the `library/` directory. If not, create them using the following sample structure:
   
   `book.csv`
   ```csv
   id,title,author,status
   1,The Alchemist,Paulo Coelho,Available
   ```

   `entry.csv`
   ```csv
   typr,date,member id,member name,book name,book id,remarks
   ```
   
3. Run the application:
   ```bash
   python library.py
   ```

---

## 💻 Application Flow

Upon running the script, the user is prompted with options:

- **A.** Register as a new library member
* **B.** Borrow books
+ **C.** Return books
- **D.** Add new books
* **E.** Exit the system

The system performs file I/O operations and appends transaction records accordingly

---

## 📌 Design Highlights

- **Object-Oriented Design (OOP):** Encapsulation and abstraction through th `Library` class
* **Scalable Structure:** Modular functions enable easy transition to database (e.g., SQLite, PostgreSQL)
+ **Minimal Dependencies:** Works out-of-the-box on any standard Python environment
- **Robust logging:** All book-related actions are recorded for auditing

---

## ⚠️ Known Limitations

| **Issue** | **Description** |
| --- | --- |
|Hardcoded File Paths | Must be changed to relative paths for portability |
| No Authentication | No login or tole-based access |
| In-Memory Member List | Members are not saved between sessions |
| Duplicate Member Names | No enforcement of unique names for members |

---

## 🔄 Suggested Improvements

| **Feature** | **Description** |
| --- | --- |
| Replace CSV with SQLite/PostgreSQL | Improve performance and scalability |
| Use `argparse` for CLI | Better user control via terminal arguments |
| Create Web UI | Use Flask or Django for a user-friendly interface |
| Member Persistence | Save and load member data using files or DB |
| Add Unit Tests | Ensure reliability with test automation |
| Add Logging | Track usage and errors with `logging` module |

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for more information.

---

🤝 Contributing

We welcome contributions! Please follow these steps:
1. Fork the repository
2. Create a new feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request
