# import psycopg2


# db = psycopg2.connect(
#     database = 'You basename',
#     password='You password',
#     user='postgres',
#     host='localhost'
# )

# cursor = db.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS users(
#    user_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#    name VARCHAR(40),
#    lastname VARCHAR(40),
#    contact VARCHAR(15) UNIQUE
# )''')

# cursor.execute('''INSERT INTO users(name, lastname, contact)
# VALUES (%s, %s, %s)
# ON CONFLICT DO NOTHING''',('Odilbek', 'Murodaov', '12112133132'))



# db.commit()
# db.close()


import psycopg2

class DataBase:
    def __init__(self):
        self.database = psycopg2.connect(
            database='Payshanba',
            password='1996',
            user='postgres',
            host='localhost'

        )

    def menager(self, sql, *args, commit:bool=False,
                                fetchone:bool=False,
                                fetchall:bool=False):
        with self.database as db:
            with db.cursor() as cursor:
                cursor.execute(sql, args)
                if commit:
                    return db.commit()
                elif fetchone:
                    return cursor.fetchone()
                elif fetchall:
                    return cursor.fetchall()

    def create_table_categories(self):
        sql = '''CREATE TABLE IF NOT EXISTS categories(
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR(60) UNIQUE
        )'''
        self.menager(sql, commit=True)


    def insert_category(self, category_name):
        sql = '''INSERT INTO categories(category_name)
        VALUES (%s) ON CONFLICT DO NOTHING'''
        self.menager(sql, (category_name,), commit=True)


    def get_all_categories(self):
        sql = '''SELECT * FROM categories'''
        return self.menager(sql, fetchall=True)


db = DataBase()
# db.create_table_categories()
# categories = ['kompyuter', 'televizor', 'smartfon']
# for category in categories:
#    db.insert_category(category)



# print(db.get_all_categories())


