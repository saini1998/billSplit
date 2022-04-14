
import os
os.system('clear')

def enterChoice():
    choice = input("Enter(r for reenter item price): ")
    return choice

def handleChoice(choice, item):
    if choice == 'r':
            return 'continue'
    
    if choice == 'all':
            price = (float(item)) / 4
            for person in hisab:
                hisab[person] += price
            return
    else: 
        if len(choice) == 1:
            if choice in hisab:
                price = float(item)
                hisab[choice] += price
                return

        elif len(choice) == 0:
            return "take choice again"

        else: 
            fewSplit = list(choice)
            l = len(fewSplit)
            if ( len(set(fewSplit)) == l ):
                if set(fewSplit).issubset(['a', 'b', 'j', 'n']):
                    price = (float(item)) / (l)
                    for fs in fewSplit:
                        hisab[fs] += price
                    return
                else:
                    return "take choice again"
                
            else:
                return "take choice again"




flatmates = ['aaryaman', 'bansal', 'naman', 'janghala', 'all']

hisab = {
    'a': 0,
    'b': 0,
    'n': 0,
    'j': 0
}

numberOfItems = 0
totalPrice = 0

print("ab tak ka hisab: ", hisab)

numberOfBills = int(input('Enter number of bills: '))
billi = 0

while numberOfBills>0:
    for key in hisab:
        hisab[key] = 0
    print()
    print("Bill ", billi + 1)
    billi += 1
    storeName = input("Enter store name: ")
    numberOfItems = 0
    totalPrice = 0
    while True:
        print()
        item = input("Enter item (x for end): ")
        if item == 'x':
            break

        print("divide between ", " ".join(f for f in flatmates))
        
        choice = enterChoice()
        action = handleChoice(choice, item)

        if action == 'continue':
            numberOfItems -= 1
            totalPrice -= float(item)
            continue

        if action == "take choice again":
            choice = enterChoice()
            action = handleChoice(choice, item)

        numberOfItems += 1
        totalPrice += float(item)

    print()
    print(storeName, " split with ", numberOfItems, " items and ", round(totalPrice, 2), " as total amount is as follow: ")
    for f in range(0, len(flatmates) - 1):
        amount = hisab[flatmates[f][0]]
        ramount = round(amount,2)
        print(flatmates[f], " ", ramount )

    numberOfBills -= 1

