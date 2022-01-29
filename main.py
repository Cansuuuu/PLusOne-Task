import json
file = open('data.json') #open the json file

#The first function
def getSortedMapleToppedItems(menu):
    items = []
    itemsNames = []
    for item in menu:
        try:
            listOfToppings = item["topping"]
            toppings = iter(listOfToppings)
            while True:
                try:
                    toppingType = next(toppings)
                    if toppingType["type"].lower() == "maple":
                        items.append(item)
                        itemsNames.append(item["name"])
                        break
                except StopIteration:
                    break


        except:
            continue
    sortedItems = sorted(items, key=lambda myItem: myItem['name'])
    sortedItemsNames = sorted(itemsNames)
    return sortedItems, sortedItemsNames

#Output the first function
menu = json.load(file)
sortedItemsM1, sortedItemsNamesM1=getSortedMapleToppedItems(menu)

print((json.dumps(sortedItemsM1, indent=2)))
print("***************************")
print("Item Names Only:")
print(sortedItemsNamesM1)
print("***************************")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-")
#####################################################################################################

#The second way (with filter function)
def secondLevelSort(x):
    if x["type"].lower() == "maple":
        return True
    else:
        return False
    


def firstLevelSort(x):
    if "topping" in x:
        myTestList = filter(secondLevelSort, x["topping"])

        if len(list(myTestList)) != 0:
            return True
        else:
            return False
    else:
        return False
    
    
def sortmyFilteredList(menu):
    initialListItems = list(filter(firstLevelSort, menu))
    initialListItemsNames = [item["name"] for item in initialListItems]
    sortedItems = sorted(initialListItems, key=lambda myItem: myItem['name'])
    sortedItemsNames = sorted(initialListItemsNames)
    return sortedItems, sortedItemsNames

#Output the second function
sortedItemsM1, sortedItemsNamesM1=sortmyFilteredList(menu)
print((json.dumps(sortedItemsM1, indent=2)))
print("***************************")
print("Item Names Only:")
print(sortedItemsNamesM1)
print("***************************")
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-")

#################################################################################################################
#Output of both functions together

#Print the original json file
print("Original File:")
print(json.dumps(menu,indent=2))
print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*")

#Call the funtions.
sortedItemsM1, sortedItemsNamesM1=sortmyFilteredList(menu)
sortedItemsM2, sortedItemsNamesM2 = getSortedMapleToppedItems(menu)
methods=[{'SortedItems':sortedItemsM1,'SortedNames':sortedItemsNamesM1},{'SortedItems':sortedItemsM2,'SortedNames':sortedItemsNamesM2}]
i=0

for method in methods:
    print("Items of method NO."+str(i)+" :")
    print((json.dumps(method["SortedItems"], indent=2)))
    print("***************************")
    print("Item Names Only:")
    print(method["SortedNames"])
    print("***************************")
    i=i+1
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-")
    

