import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # ✅ Your MySQL username
            password="root",      # ✅ Your MySQL password
            database="rationdb",  # ✅ Your database name
            port=3307            # ✅ Explicitly specify port
        )

        if connection.is_connected():
            print("✅ Connected to MySQL database!")
            return connection
        else:
            print("❌ Connection failed!")
            return None

    except mysql.connector.Error as err:
        print("❌ Error while connecting to MySQL:", err)
        return None
