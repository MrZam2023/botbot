CREATE_USER_TABLE_QUERY = """ 
        CREATE TABLE IF NOT EXISTS telegram_users
        (ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER, 
        USERNAME CHAR(50),
        FIRST_NAME CHAR(50),
        LAST_NAME CHAR(50),
        UNIQUE(TELEGRAM_ID)
        )
"""


INSERT_USER_QUERY = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)"""


class Database:
    def sql_insert_user_command(self, telegram_id, username, first_name, last_name):

        pass