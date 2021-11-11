import json
import os
from pprint import pprint

__item_last_id__=f"db/itemIdDerectory/item_last_id.db"
__item_folder__="db/item"
__customer_folder__= "db/customer"
__customer_last_id__="db/customerIdDerectory/customer_last_id.db"
__order_folder__="db/order"
__order_last_id__=f"db/orderIdDerectory/order_last_id.db"

class Item:

    def save(self):
        if os.path.exists(__item_last_id__):
            with open(f"db/itemIdDerectory/item_last_id.db", "r") as itemLastId:
                last_id_item = json.load(itemLastId)
                self.last_id = last_id_item["id"] + 1

                if self.last_id == 1:
                    id=1
                else:
                     id=self.last_id
        else:
            id=1
        _data_ = {
            "id": id,
            "name": self.name,
            "price": self.price,
            "sellingPrice": self.selling_price
        }
        with open(f"db/item/{id}.db","w") as itemFile:
            print(_data_)
            json.dump(_data_,itemFile)

        _last_id ={
            "id":id
        }


        with open(f"db/itemIdDerectory/item_last_id.db","w") as itemLastId:
            json.dump(_last_id,itemLastId)


    def all(self):
        item_file_names= os.listdir(__item_folder__)
        items=[]
        for item_file_name in item_file_names:
            item =Item()
            values=Item.__get_item_by_path(
                item,f"{__item_folder__}/{item_file_name}")
            items.append(values)
        return items


    def __get_item_by_path(item, path):
        with open(path, "r") as item_file:
            _data_ = json.load(item_file)
            item.id= _data_["id"]
            item.name=_data_["name"]
            item.price=_data_["price"]
            item.sellingPrice=_data_["sellingPrice"]
            return _data_

    def search(self, key, value):
        items = self.all()
        result_items = []
        for item in items:
            print(item["id"])
            item_value = getattr(item, key.__str__())
            print(item_value)
            if item_value == value:
                result_items.append(item)
        return result_items

    def find(self, id):
        Item.__get_item_by_path(self, f"{__item_folder__}/{id}.db")




class Customer:

    def save(self):
        if os.path.exists(__customer_last_id__):
            with open("db/customerIdDerectory/customer_last_id.db", "r") as customerLastId:
                last_id_customer = json.load(customerLastId)
                self.customer_last_id = last_id_customer["id"] + 1

                if self.customer_last_id == 1:
                    id=1
                else:
                     id=self.customer_last_id
        else:
            id=1
        _data_ = {
            "id": id,
            "name": self.name,
            "address": self.address,
            "tel": self.tel
        }
        with open(f"db/customer/{id}.db","w") as customerFile:
            print(_data_)
            json.dump(_data_,customerFile)

        _last_id ={
            "id":id
        }


        with open(f"db/customerIdDerectory/customer_last_id.db","w") as customerLastId:
            json.dump(_last_id,customerLastId)

    def all(self):
        customer_file_names= os.listdir(__customer_folder__)
        customers=[]
        for customer_file_name in customer_file_names:
            customer =Customer()
            values=Customer.__get_customer_by_path(
                customer,f"{__customer_folder__}/{customer_file_name}")
            customers.append(values)
        return customers


    def __get_customer_by_path(customer, path):
        with open(path, "r") as customer_file:
            _data_ = json.load(customer_file)
            customer.id=_data_["id"]
            customer.name=_data_["name"]
            customer.address=_data_["address"]
            customer.tel=_data_["tel"]
            return _data_

    def search(self, key, value):
        customers = self.all()
        result_customers = []
        for customer in customers:
            customer_value = getattr(customer, key)
            print(customer_value)
            if customer_value == value:
                result_customers.append(customer)
        return result_customers

    def find(self, id):
        Customer.__get_customer_by_path(self, f"{__customer_folder__}/{id}.db")



class Order:
    def save(self):
        if os.path.exists(__order_last_id__):
            with open(f"db/orderIdDerectory/order_last_id.db", "r") as orderLastId:
                last_id_order = json.load(orderLastId)
                self.last_id = last_id_order["id"] + 1

                if self.last_id == 1:
                    id=1
                else:
                     id=self.last_id
        else:
            id=1
        _data_ = {
            "id": id,
            "customerId":self.customerId,
            "itemId": self.itemId,
            "itemName": self.itemName,
            "totQTY": self.totQTY,
            "totPrice":self.totPrice
        }
        with open(f"db/order/{id}.db","w") as orderFile:
            print(_data_)
            json.dump(_data_,orderFile)

        _last_id ={
            "id":id
        }

        with open(f"db/orderIdDerectory/order_last_id.db","w") as orderLastId:
            json.dump(_last_id,orderLastId)


    def all(self):
        order_file_names= os.listdir(__order_folder__)
        orders=[]
        for order_file_name in order_file_names:
            order =Order()
            valus=Order.__get_order_by_path(
                order,f"{__order_folder__}/{order_file_name}")
            orders.append(valus)
        return orders


    def __get_order_by_path(order, path):
        with open(path, "r") as order_file:
            _data_ = json.load(order_file)
            return _data_

    def search(self, key, value):
        orders = self.all()
        result_orders = []
        for order in orders:
            order_value = getattr(order, key)
            print(order_value)
            if order_value == value:
                result_orders.append(order)
        return result_orders

    def find(self, id):
        Order.__get_order_by_path(self, f"{__order_folder__}/{id}.db")


def item_create(name, price, selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.selling_price = selling_price
    item.save()

def item_all():
    item=Item()
    items=item.all()
    pprint(items.__str__())

def item_search(key,value):
    item = Item()
    results = item.search(key,value)
    pprint(results.__str__())

def item_view(id):
    item=Item()
    item.find(id)
    pprint(item.name.__str__())


def customer_create(name,address,tel):
    customer = Customer()
    customer.name=name
    customer.address= address
    customer.tel=tel
    customer.save()

def customer_all():
    customer = Customer()
    customers = customer.all()
    pprint(customers)

def customer_search(key,value):
    customer = Customer()
    results = customer.search(key,value)
    pprint(results)

def customer_view(id):
    customer = Customer()
    customer.find(id)
    pprint(customer.name.__str__)


def order_create(customerId,itemId,itemName,totQTY,totPrice):
    order = Order()
    order.customerId=customerId
    order.itemId = itemId
    order.itemName = itemName
    order.totQTY=totQTY
    order.totPrice=totPrice
    order.save()


def order_all():
    order = Order()
    orders = order.all()
    pprint(orders)


def order_search(key, value):
    order = Order()
    results = order.search(key, value)
    pprint(results)


def order_view(id):
    order = Order()
    order.find(id)
    pprint(order.id.__str__)


if __name__ == "__main__":
    section_name=input("Enter Section Name(Item/Order/Customer)")

    if section_name == "Item":
        sub_section_item=input("Plz enter All/Save/Serach/View")

        if sub_section_item == "Save":
            print("Plz Enter Item Details:-")
            item_name=input("Item Name")
            item_price=input("Item Price")
            item_selling_price=input("Item Selling Price")
            item_create(item_name,item_price,item_selling_price)

        elif sub_section_item == "All":
            item_all()

        elif sub_section_item== "Search":
            key=input("Key")
            value=input("Value")
            item_search(key,value)

        elif sub_section_item== "View":
            id=input("Plz input Id")
            item_view(id)



    if section_name == "Order":
        sub_section_order = input("Plz enter All/Create/Serach/View")

        if sub_section_order == "Create":
            od_customer_id =input("customer id")
            od_item_id=input("item id")
            od_item_name=input("item name")
            od_item_tot_QTY=input("tot QTY")
            od_itm_tot_price=input("tot price")
            order_create(od_customer_id,od_item_id,od_item_name,od_item_tot_QTY,od_itm_tot_price)

        elif sub_section_order == "All":
            order_all()

        elif sub_section_order== "View":
            id=input("Plz input Id")
            order_view(id)
        elif sub_section_order=="Search":
            key=input("key")
            value=input("value")
            order_search(key,value)

    if section_name == "Customer":
        sub_section_customer=input("Plz enter All/Create/Serach/View")

        if sub_section_customer == "Create":
            print("Plz Enter Customer Details:-")
            customer_name=input("Customer Name")
            customer_address=input("Customer Address")
            customer_tel=input("Customer Tel")
            customer_create(customer_name,customer_address,customer_tel)

        elif sub_section_customer == "All":
            customer_all()

        elif sub_section_customer== "Search":
            key=input("Key")
            value=input("Value")
            customer_search(key,value)

        elif sub_section_customer== "View":
            id=input("Plz input Id")
            customer_view(id)


