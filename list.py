breakfast_items = ["Frootloops"  , "Raisin Bran",  "Frosted Flakes", "Fruity pebbles", "coco pebbles", "cap'n crunch"]

print(breakfast_items)
print(breakfast_items[2])
breakfast_items.append("frosted mini wheats")
breakfast_items.append("golend grahams")

print(breakfast_items)
breakfast_items.sort()
print(breakfast_items)
breakfast_items.remove(breakfast_items[2])
breakfast_items.remove("coco pebbles")
print(breakfast_items)

total_cereal_ = len(breakfast_items)
print(f"the total items we have for cereal are: (Total_cereal_items)") 