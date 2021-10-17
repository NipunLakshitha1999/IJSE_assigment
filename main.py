
__item_last_id__=f"db/item/item_last_id.db"

import json
import os


class Item:



    def save(self):
        if os.path.exists(__item_last_id__):
            with open(f"db/item/item_last_id.db", "r") as itemLastId:
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
        },
        with open(f"db/item/{id}.db","w") as itemFile:
            json.dump(_data_,itemFile)

        _last_id ={
            "id":id
        }


        with open(f"db/item/item_last_id.db","w") as itemLastId:
            json.dump(_last_id,itemLastId)

def item_create(name, price, selling_price):
    item = Item()
    item.name = name
    item.price = price
    item.selling_price = selling_price
    item.save()

if __name__ == "__main__":
    section_name=input("Enter Section Name(Item/Order/Customer)")

    if section_name == "Item":
        print("Plz Enter Item Details:-")
        item_name=input("Item Name")
        item_price=input("Item Price")
        item_selling_price=input("Item Selling Price")
    item_create(item_name,item_price,item_selling_price)


    if section_name == "Order":
        print("Order")

    if section_name == "Customer":
        print("Customer")

