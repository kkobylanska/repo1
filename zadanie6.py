#ZADANIE 6
for i in range(1,5):
    print(i*"*")

#ZADANIE 6 cz.2
def choinka(x):
    rzad = "  *  \n"
    for i in range(x):
        rzad += " *** \n"
        rzad += "*****\n"
    rzad += "  *  \n  *  "
    return rzad
print(choinka(3))
