from solution import Solution
from time import sleep
import sqlite3


def main():
    db = Solution("sqlite.db")
    
    while True:
        print('''
Що ви хочете зробити?
              
1 - Додавання продуктів:
2 - Додавання клієнтів:
3 - Замовлення товарів:
4 - Сумарний обсяг продажів:
5 - Кількість замовлень на кожного клієнта:
6 - Середній чек замовлення:
7 - Найбільш популярна категорія товарів:
8 - Загальна кількість товарів кожної категорії:
9 - Оновлення цін категорії на 10% більші:
10 - Показати усіх користувачів
11 - Показати усі продукти
12 - Показати усі замовлення(Joined)
0 - Вийти:

        ''')
        command = input("Оберіть ваші дії: ")
        try:
            command = int(command)
        except:
            print("Input має бути числом")
            sleep(2)    
            continue    
        
        if command not in range(0, 12+1):
            print("Введене число є поза межами 0-9")  
            sleep(2)
            continue
        
        
        if command == 0:
            print("Дякуємо за використання програми!")
            break
        elif command == 1:
            product_name = input("Введіть назву продукту: ")
            category = input("Введіть назву категорії до якої належить цей товар: ")
            while True:
                price = input("Введіть ціну продукту: ")
                try:
                    price = int(price)
                    break
                except:
                    print("Ціна має бути числом")
                    
                    
            print(db.add_product(product_name, category, price))
            
        elif command == 2:
            first_name = input("Введіть ім'я: ")
            last_name = input("Введіть прізвище: ")
            email = input("Введіть електронну адресу: ")
                    
            try:        
                print(db.add_customer(first_name, last_name, email))
            except sqlite3.IntegrityError:
                print("Схоже вже є користувач з такою адресою")
                sleep(2)
                continue
             
        elif command == 3:
            customer_email = input("Введіть електронну адресу замовника: ")
            try:
                customer_id = db.get_customer_id_by_email(customer_email)
            except:
                print("Невірна адреса користувача")
                sleep(2)
                continue
            
            product_name = input("Введіть назву продукту: ")
            try:
                product_id = db.get_product_id_by_name(product_name)
            except:
                print("Неправильна назва товару")
                sleep(2)
                continue
                
            quantity = input("Введіть кількість продукту в замовленні: ")
            print(db.add_order(customer_id, product_id, quantity))
            
        elif command == 4:
            print(db.get_total_income())
            sleep(2)
            
        elif command == 5:
            print(db.get_grouped_orders_count())
            sleep(2)
        
        elif command == 6:
            print(db.get_average_bill())
            sleep(2)
            
        elif command == 7:
            print(db.get_pop_category())
            
        elif command == 8:
            print(db.get_products_grouped_by_category())
            
        elif command == 9:
            category = input("Введіть категорію для подорожання")
            db.update_prices(category)
            
        elif command == 10:
            customers = db.get_all_customers()
            for customer in customers:
                for x in customer:
                    print(x, end="\t")
                print()
            sleep(1)
        
        elif command == 11:
            products = db.get_all_products()
            for product in products:
                for x in product:
                    print(x, end="\t")
                print()
            sleep(1)
        
        elif command == 12:
            orders = db.get_all_joined_orders()
            for order in orders:
                for x in order:
                    print(x, end="\t")
                print()
            sleep(1)
            
        
                
            
            
            
            
            

        
    
    
    
if __name__ == "__main__":
    main()