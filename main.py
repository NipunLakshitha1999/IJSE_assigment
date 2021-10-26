
__item_last_id__=f"db/itemIdDerectory/item_last_id.db"
__item_folder__="db/item"
__customer_folder="db/cutomer"
__customer_last_id__="db/customerIdDerectory/customer_last_id.db"
import json
import os
from pprint import pprint


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
            Item.__get_item_by_path(
                item,f"{__item_folder__}/{item_file_name}")
            items.append(item)
        return items


    def __get_item_by_path(item, path):
        with open(path, "r") as item_file:
            _data_ = json.load(item_file)

    def search(self, key, value):
        items = self.all()
        result_items = []
        for item in items:
            item_value = getattr(item, key)
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
        print("Order")

    if section_name == "Customer":
        sub_section_item=input("Plz enter All/Create/Serach/View")

        if sub_section_item == "Create":
            print("Plz Enter Customer Details:-")
            customer_name=input("Customer Name")
            customer_address=input("Customer Address")
            customer_tel=input("Customer Tel")
            customer_create(customer_name,customer_address,customer_tel)


