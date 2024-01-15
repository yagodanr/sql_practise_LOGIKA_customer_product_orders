from db import DB



class Solution(DB):
    # 4
    def get_total_income(self) -> int:
        self.cur.execute('''
            SELECT SUM(products.price * orders.quantity) AS total_bills
            FROM orders
            INNER JOIN products ON orders.product_id=products.product_id;
        ''')
        
        response = self.cur.fetchone()[0]
        return response
    
    # 5
    def get_grouped_orders_count(self) -> tuple:
        self.cur.execute('''
            SELECT customers.first_name AS customers_name, COUNT(orders.order_id) AS amount_of_orders
            FROM orders
            INNER JOIN customers ON orders.customer_id=customers.customer_id
            GROUP BY customers.first_name
            ORDER BY customers.customer_id ASC;
        ''')
        response = self.cur.fetchall()
        return response
    
    # 6
    def get_average_bill(self) -> int:
        self.cur.execute('''
            SELECT AVG(products.price * orders.quantity) AS average_bill
            FROM orders
            INNER JOIN products ON orders.product_id=products.product_id;
        ''')
        
        response = self.cur.fetchone()[0]
        return response
    
    # 7
    def get_pop_category(self) -> str:
        self.cur.execute('''
            SELECT products.category AS most_popular_category
            FROM orders
            INNER JOIN products ON orders.product_id=products.product_id
            GROUP BY products.category
            ORDER BY COUNT(orders.order_id) DESC 
            LIMIT 1; 
        ''')
        
        response = self.cur.fetchone()[0]
        return response
    
    # 8
    def get_products_grouped_by_category(self) -> tuple:
        self.cur.execute('''
            SELECT category, COUNT(product_id)
            FROM products
            GROUP BY category;
        ''')
        response = self.cur.fetchall()
        return response
    
    # 9
    def update_prices(self, category: str):
        self.cur.execute('''
            UPDATE products
            SET price=price*1.1
            WHERE category=?;                 
        ''', (category, ))
        self.con.commit()
    
    

if __name__ == "__main__":
    db = Solution("sqlite.db")
    print(db.get_all_products())
    db.update_prices("laptop")
    print(db.get_all_products())
    



