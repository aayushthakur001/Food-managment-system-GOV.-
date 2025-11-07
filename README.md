# 🥖 Ration Card Management System using MySQL

A **Python–MySQL based application** designed to **digitize and automate** the core operations of government ration depots.  
This project aims to bring **transparency, efficiency, and accountability** to food distribution under India’s **Public Distribution System (PDS)**.

---

## 📖 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Technologies Used](#-technologies-used)
- [Database Design](#-database-design)
- [Modules](#-modules)
- [Setup and Installation](#-setup-and-installation)
- [Sample Output](#-sample-output)
- [Advantages](#-advantages)
- [Future Scope](#-future-scope)
- [Project Structure](#-project-structure)
- [Conclusion](#-conclusion)
- [Author](#-author)
- [License](#-license)

---

## 🧩 Overview

The **Ration Card Management System** is a **console-based software solution** developed using **Python** and **MySQL** to manage ration depot operations such as:
- Beneficiary registration  
- Food stock management  
- Ration distribution tracking  

By replacing traditional paper-based record systems, this project enhances **data accuracy**, **reduces redundancy**, and supports **real-time monitoring** of distribution and stock levels.

The project showcases how **digital transformation** can modernize essential public services and improve transparency and governance in welfare distribution.

---

## 🚀 Features

✅ **CRUD Operations:** Create, Read, Update, Delete functionalities for all modules  
✅ **Beneficiary Management:** Add, modify, or delete ration cardholder details  
✅ **Inventory Management:** Track and update food stock levels  
✅ **Distribution Management:** Record and monitor ration allotments  
✅ **Centralized Database:** All data stored in MySQL for security and easy retrieval  
✅ **Error Handling:** Exception management during database connectivity  
✅ **Scalable Architecture:** Can be extended into GUI or web-based platforms  

---

## 🧠 System Architecture

The system follows a **modular architecture** divided into key modules:
1. **Database Connection Module (`db_connection.py`)** – Establishes a secure connection to MySQL.  
2. **Beneficiary Module (`beneficiary.py`)** – Handles all CRUD operations for beneficiaries.  
3. **Main Application (`main.py`)** – Provides a menu-driven interface for user interaction.

Each module is designed for independent functionality and reusability, ensuring easy maintenance and scalability for future development.

---

## 🛠 Technologies Used

| Component | Technology | Description |
|------------|-------------|-------------|
| Programming Language | **Python 3.11+** | Core development and logic implementation |
| Database | **MySQL** | Backend for storing beneficiary, stock, and distribution records |
| Connector | **mysql-connector-python** | Connects Python application with MySQL database |
| IDE | **VS Code / PyCharm** | Development and testing environment |

---

## 🗄 Database Design

The system uses a **relational schema** with the following primary tables:

### 1. `Beneficiary`
| Field | Type | Description |
|-------|------|-------------|
| id | INT (PK) | Unique beneficiary ID |
| name | VARCHAR(100) | Beneficiary name |
| card_no | VARCHAR(50) | Ration card number |
| family_size | INT | Number of family members |
| category | VARCHAR(20) | APL/BPL classification |

### 2. `FoodItem`
| Field | Type | Description |
|-------|------|-------------|
| id | INT (PK) | Unique item ID |
| item_name | VARCHAR(50) | Food item name |
| unit_price | DECIMAL(10,2) | Price per unit |
| stock_kg | DECIMAL(10,2) | Available stock (kg) |

### 3. `Distribution`
| Field | Type | Description |
|-------|------|-------------|
| id | INT (PK) | Unique transaction ID |
| beneficiary_id | INT (FK) | Linked to Beneficiary ID |
| item_id | INT (FK) | Linked to Food Item ID |
| quantity_kg | DECIMAL(10,2) | Quantity distributed |
| total_cost | DECIMAL(10,2) | Computed total |
| date | DATE | Date of distribution |

These tables maintain **referential integrity** and support **one-to-many relationships** between beneficiaries and distributions, and between food items and distributions.

---

## ⚙️ Modules

### 🧍‍♂️ Beneficiary Management
Handles adding, viewing, updating, and deleting beneficiary details.

### 🍚 Food Item Management
Tracks stock levels and updates available inventory.

### 📦 Distribution Module
Records transactions between depots and beneficiaries.

### 🧮 Database Connectivity
Ensures secure, reusable connections to MySQL for all modules.

---

## 🧰 Setup and Installation

### Prerequisites
- Python 3.11+
- MySQL Server
- MySQL Workbench (optional for visualization)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/aayushthakur001/Food-managment-system-GOV
   cd Food-managment-system-GOV
# 🧾 Ration Depot Management System (Python + MySQL)

## 2️⃣ Install Required Python Packages
```bash
pip install mysql-connector-python
```

---

## 3️⃣ Set Up the MySQL Database

### 🧩 Steps
1. Open **MySQL Workbench**
2. Create a new database (e.g., `ration_db`)
3. Import tables as per the schema in the project report

---

## 4️⃣ Update Connection Credentials

In **`db_connection.py`**, update the connection details:
```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="ration_db"
)
```

---

## 5️⃣ Run the Application
```bash
python main.py
```

---

## 🖥 Sample Output
```bash
✅ Connected to MySQL database!

===== RATION DEPOT MANAGEMENT =====
1. Add Beneficiary
2. View All Beneficiaries
3. Update Beneficiary
4. Delete Beneficiary
5. Exit

(1, 'Amit Sharma', 'RC1234', 4, 'BPL')
(2, 'Pooja Patel', 'RC1235', 3, 'APL')
```

---

## 🌟 Advantages

- Centralized digital data management  
- Eliminates manual records  
- Reduces human error  
- Secure and structured storage  
- Easily maintainable modular code  
- Scalable for future development  
- Efficient CRUD operation handling  
- Real-time updates and data retrieval  

---

## 🔮 Future Scope

- 🧑‍💼 User Authentication & Roles (Admin, Operator)  
- 🌐 Web Interface (Flask/Django)  
- 📊 Report Generation and Data Visualization  
- 📱 Notification System (SMS/Email)  
- ☁️ Cloud-based Multi-Depot Synchronization  
- 💾 Automated Backup & Restore System  
- 📈 Data Analytics for Stock and Distribution Trends  

---

## 📁 Project Structure
```
Food-managment-system-GOV/
│
├── db_connection.py        # Database connection handler
├── beneficiary.py          # Beneficiary CRUD operations
├── food_item.py            # Food item management module (optional)
├── distribution.py         # Distribution management module (optional)
├── main.py                 # Menu-driven main application
├── requirements.txt        # Dependencies (optional)
└── README.md               # Project documentation
```

---

## 🏁 Conclusion
The **Ration Card Management System** demonstrates the successful use of **Python–MySQL integration** to streamline real-world administrative processes.  
It eliminates the inefficiencies of manual record-keeping by providing a **fully automated, scalable, and data-driven management solution**.  

This project not only fulfills its technical objectives but also promotes **digital governance and transparency** in public food distribution systems.  
Future enhancements such as **web deployment**, **authentication**, and **real-time reporting** can elevate it into a full-scale **e-Governance application**.

---

## 👤 Author
**Ayush Kumar Thakur**  
🎓 University Institute of Computing, Chandigarh University  
📧 [GitHub Profile](#)  
📅 October 2025  

---

## 🧾 License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute it with proper attribution.

```
MIT License

Copyright (c) 2025 Ayush Kumar Thakur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

⭐ **If you find this project helpful, consider giving it a star on GitHub!**
