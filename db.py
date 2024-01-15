import sqlite3




class DB:
    def __init__(self, db_name: str):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        
    def __del__(self):
        self.cur.close()
        self.con.close()
        
    def create_tables(self):
        self.cur.execute(
            '''CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL
            );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS customers ( 
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE 
            );''')

        self.cur.execute('''CREATE TABLE IF NOT EXISTS orders ( 
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                order_date DATE NOT NULL,
                
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
                FOREIGN KEY (product_id) REFERENCES products(product_id) 
            );''')
        
        
    def add_product(self, product_name: str, category: str, price: int):
        self.cur.execute('''
            INSERT INTO products(name, category, price)
            VALUES
                (?, ?, ?);
            ''',
            (product_name, category, price))
        self.con.commit()

        self.cur.execute("SELECT * FROM products ORDER BY product_id DESC LIMIT 1;")
        response = self.cur.fetchone()
        return response 

        
    def add_customer(self, first_name: str, last_name: str, email: str):
        self.cur.execute('''
            INSERT INTO customers(first_name, last_name, email)
            VALUES
                (?, ?, ?);
            ''',
            (first_name, last_name, email))
        self.con.commit()

        self.cur.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1;")
        response = self.cur.fetchone()
        return response 
    
    def add_order(self, customer_id: int, product_id: int, quantity: int, order_date: str):
        self.cur.execute('''
            INSERT INTO orders(customer_id, product_id, quantity, order_date)
            VALUES
                (?, ?, ?, ?);
            ''',
            (customer_id, product_id, quantity, order_date))
        self.con.commit()

        self.cur.execute("SELECT * FROM customers ORDER BY customer_id DESC LIMIT 1;")
        response = self.cur.fetchone()
        return response
    
    
    
    def get_all_products(self):
        self.cur.execute("SELECT * FROM products;")
        response = self.cur.fetchall()
        return response
    
    def get_all_customers(self):
        self.cur.execute("SELECT * FROM customers;")
        response = self.cur.fetchall()
        return response
    
    def get_all_joined_orders(self):
        self.cur.execute('''SELECT * FROM orders
            INNER JOIN products ON orders.product_id=products.product_id
            INNER JOIN customers ON orders.customer_id=customers.customer_id;''')
        
        response = self.cur.fetchall()
        return response

    
    
    

if __name__ == "__main__":
    db = DB("sqlite.db")
    db.create_tables()
    
    
    def init_products(db: DB):
        db.add_product("Mac", "laptop", 1500)
        db.add_product("Legion", "laptop", 1000)
        db.add_product("IPad", "tablet", 400)
        db.add_product("Samsung", "tablet", 200)
        db.add_product("HyperX Alloy FPS", "keyboard", 70)
        db.add_product("ESport", "keyboard", 100)
        db.add_product("Corsair", "keyboard", 180)
        db.add_product("Logitec", "keyboard", 180)

        print(db.get_all_products())    
    # init_products(db)
        
    def init_customers(db: DB):
        db.add_customer("Mark", "Levyi", "mark@gmail.com")
        db.add_customer("Pavel", "Pravyi", "pavel@gmail.com")
        db.add_customer("Bob", "Dylan", "bob@gmail.com")
        db.add_customer("Josh", "Maizer", "josh@gmail.com")
        db.add_customer("Gregory", "Meinster", "gregory@gmail.com")
        
        print(db.get_all_customers())
    # init_customers(db)
    
    def init_orders(db: DB):
        db.add_order(1, 1, 2, "2023-03-25")
        db.add_order(2, 2, 1, "2023-03-26")
        db.add_order(3, 3, 3, "2023-03-23")
        db.add_order(4, 4, 4, "2023-03-25")
        db.add_order(5, 5, 5, "2023-03-25")
        db.add_order(1, 6, 6, "2023-05-12")
        db.add_order(2, 7, 7, "2023-05-16")
        db.add_order(3, 8, 8, "2023-12-12")
        
        print(db.get_all_joined_orders())
    # init_orders(db)

    
    