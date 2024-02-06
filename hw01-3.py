# user input 
statement = input("Enter your statement : ") 

# defining a list which contains vowels 
vowels = ["a", "e", "i", "o", "u","A", "E","I","O","U"]

# removing whitespaces 
statement = statement.replace(" ", "")

# changing lower to upper and upper to lower 
statement = statement.swapcase()

# turning vowels to "." 
for state in statement:
    if state in  vowels:
        statement = statement.replace(state, ".")

print(statement)
