# ATM Management System

The **ATM Management System** is a Python-based project that simulates basic functionalities of an Automated Teller Machine (ATM). It allows users to perform operations such as account creation, balance inquiries, deposits, and withdrawals. The system utilizes a MySQL database to manage and store user information securely.

## Features

- **Account Creation**: Users can create new accounts by providing necessary details.
- **Balance Inquiry**: Users can check their current account balance.
- **Deposits**: Users can deposit a specified amount into their account.
- **Withdrawals**: Users can withdraw a specified amount from their account, subject to sufficient balance.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.x**: The programming language used for the application.
- **MySQL Server**: The database system to store user data.
- **MySQL Connector for Python**: A Python library to facilitate MySQL database connections.

## Installation

1. **Clone the Repository**:

   bash```
   
   git clone https://github.com/PR0801/ATM-MANAGEMENT-SYSTEM.git
   
   cd ATM-MANAGEMENT-SYSTEM
   
2. **Install Required Python Packages**:

   Ensure you have the MySQL Connector installed. You can install it using pip:

   bash```

   pip install mysql-connector-python

3. **Set Up the Database**:

   a.**Create the Database**: Access your MySQL server and create a new database named atm_management.
   
   sql```
   
   CREATE DATABASE atm_management;
   
   b. **Create Required Tables**:

    Use the TABLE CREATION.py script to set up the necessary tables in the atm_management database.

   bash```

   python
   
   "TABLE CREATION.py"
   
   Configure Database Connection: In the MAIN.PY script, ensure that the database connection parameters (host, user, password, database) are correctly set to match your MySQL server configuration.

5. **Usage**
   
   To start the ATM Management System:
   
   bash```

   python "MAIN.PY"

6. **Contributing**

   Contributions are welcome! If you'd like to enhance the project or fix any issues:

   Fork the repository.
   Create a new branch for your feature or fix.
   Commit your changes with descriptive messages.
   Push the changes to your fork.
   Submit a pull request detailing your changes.

## License

This project is licensed under the MIT License.

## Acknowledgments

Special thanks to all contributors and supporters of this project. Your efforts are greatly appreciated!

**Note: This project is intended for educational purposes and should not be used for actual banking operations.**
