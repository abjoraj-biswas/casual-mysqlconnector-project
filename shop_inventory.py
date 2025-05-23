import mysql.connector as a
def connect_db():
    return a.connect(
        host='localhost',
        user='root',
        password='',
        database='store',
        autocommit=True
    )


def add_product():
    product_name = input('Enter the name of the product:')
    product_price=int(input('Enter the price of each product:'))
    product_quantity=int(input('Enter the quantity of the product:'))
    db=connect_db()
    cursor=db.cursor()
    cursor.execute('insert into inventory(product_name,quantity,price_each_unit) values(%s,%s,%s)',(product_name,str(product_price),str(product_quantity)))
    print('Product added sucessfully')


def update_products():
    product_id=int(input('Enter the id of the product you want to update:'))
    product_name=input("Enter the new product's name :")
    product_price=int(input('Enter the new price of each product:'))
    product_qty=int(input('Enter the new quantity of the product:'))
    db=connect_db()
    cursor=db.cursor()
    cursor.execute('update inventory set product_name=%s,price_each_unit=%s,quantity=%s where product_id=%s',(product_name,product_price,product_qty,product_id))
    print('Product update sucessfully!!')


def delete_product():
    product_id=int(input('Enter the id of the product you want to delete:'))
    db=connect_db()
    cur=db.cursor()
    cur.execute('delete from inventory where product_id=%s',(product_id,))
    print('Product deleted sucessfully!!')


def view_all_products():
    db=connect_db()
    cur=db.cursor()
    cur.execute('select* from inventory')
    rowss=cur.fetchall()
    print('Product_id\tProduct_name    \tQuantity\tprice_each_unit')
    for row in rowss:
        print(row[0],'\t\t',row[1],'\t\t',row[2],'\t\t',row[3])


def search_product():
    product_name=input('Enter the name of the product your want to search:')
    db=connect_db()
    cur=db.cursor()
    cur.execute('Select* from inventory where product_name=%s',(product_name,))
    rowss=cur.fetchall()
    
    if len(rowss)==0:
        print('SORRY!!!,Product not found in the inventory')

    else:
        print('Product found in the inventory!!')
        print('Product_id\tProduct_name         \tquantity   \tprice_each_unit')
        for row in rowss:
            print(row[0],'\t\t',row[1],'\t\t',row[2],'\t\t',row[3])




while True:
    print(''' Welcome to shop inventory system
          1.Add Product
          2.Update product
          3.Delete Product
          4.view all products
          5.search product
          6.Exit
          ''')
    choice=int(input('Enter your choice:'))
    if choice==1:
        add_product()


    elif choice==2:
        update_products()


    elif choice==3:
        delete_product()


    elif choice==4:
        view_all_products()


    elif choice==5:
        search_product()


    elif choice==6:
        print('Thank you for using the shop inventory system!!!')
        break


    else:
        print('Invalid choice, please enter a valid choice!!!')
        continue