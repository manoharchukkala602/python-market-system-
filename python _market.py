products =[]
cart =[]
def find_product(pid):
    for p in products :
        if p["id"] ==pid:
            return p
    return None
def add_product():
    try:
        pid =int(input("Enter your id of products:"))
        name =input("Enter the product name:")
        price =float(input("Enter the product price"))
        qty =float(input("Enter the quantity of product:"))
        if price <= 0 or  qty <= 0:
        
            print("sorry its not purchuse")
            return
        if find_product(pid):
            print("product already exist")
            return
        product ={
            "id":pid,
            "name":name,
            "price":price,
            "qty":qty,
            }
        products.append(product)
        print("your product is add successfully")
    except ValueError:
        print("invalid")
def view_product():
    if not products:
        print("no products are not in list")
    else:
        print(product["id"])
        print(product["name"])
        print(product["price"])
        print(product["qty"])

def buy_product():
    try:
        pid =int(input("Enter the product id :"))
        product =find_product(pid)
        if not product :
            print("your product is already exist")
            return
        qty =float(input("Enter your quatity of the product:"))
        if pid <=0 and  qty <= 0:
            print("invalid product")
            return
        if qty >product["qty"]:
            print("sorry insufficient qty")

            return
        product["qty"] -=qty
        print("your purchuse successfully")

        item ={
            "id" :product["id"],
            "name":product["name"],
            "price":product["price"],
            "qty":qty,
            "total":product["price"] * qty,
            }
        cart.append(item)
        print("product added successfully ")
    except ValueError:
        print("invalid")
def generate_bill():
    if not products:
        print("sorry no product")
    grand_total =0
    for item in cart:
        print("name",item["name"])
        print("price",item["price"])
        print("quantity",item["qty"])
        print("total",item["total"])
    grand_total +=item["total"]
    print("____Total  Bill____")
    print("grand total", grand_total)
    print("payment successfully")
while True:
    print("___welcome to my market___")
    print("1.find product")
    print("2. add product")
    print("3. view product")
    print("4.buy product")
    print("5.genearate bill")
    choice = input("enter your choice (1-5):")
    if choice == "1":
        find_product()
    elif choice =="2":
        add_product()
    elif choice =="3":
        view_product()
    elif choice =="4":
        buy_product()
    elif choice =="5":
        generate_bill()
        break
    else:
        print("thank you ")

            

