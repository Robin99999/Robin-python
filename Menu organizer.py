import re  # do you still need this?

menu = open("menu.txt", "r")
translatedMenu = open("translatedMenu.txt", "w")
X = 0
p = -1
while X < 44: # this number may vary , you should find more genaric way 
    error = False
    t = False #variable name need be meaningful
    p = -1
    str_line = menu.readline()
    z = len(str_line)
    name2 = str_line[0:z - 1]
    x = str_line.find("(")          

    """if x == -1:
        str_line = menu.readline()
        x = str_line.find("(")
        name3 = str_line[0:x]
        name = (name2 + name3)
    else: """
    name = str_line[0:x]   # how about x = -1? 
    z = len(str_line)      # you already did at line 12
    description2 = str_line[x:z-1] # why description2 ? not just description?
    y = str_line.find(")")
    description = str_line[x:y + 1]
    if y == -1: ## if it can't find )
        p = str_line.find(".") ## Checks to see if price is on the same line because that means it has no description
        if p != -1:
            name = str_line[0:p - 1]
            price = str_line[p - 1:z]
            price = price.strip()
        else: ## goes to next line to find description
            str_line = menu.readline()
            y = str_line.find(")")
            if y == -1:
                str_line = menu.readline()
                y = str_line.find(")")
                if y == -1:
                    str_line = menu.readline()
                    y = str_line.find(")")
                else:
                    description3 = str_line[0:y + 1]
                    description = (description2 + " " + description3)
            else:
                description3 = str_line[0:y+1]
                description = (description2 + " " + description3)
    if y != -1: ## if there is a ) carry on
        for character in str_line: ## checks to see if the price in on the line
            if character.isdigit():
                t = True
        if t == False: ##goes to the next line for the price
            str_line = menu.readline()
            z = len(str_line)
            price = str_line[0:z-1]
        if t == True:
            z = len(str_line)
            price = str_line[y+1:z-1]
            price = price.strip()

    if x == -1:
        translatedMenu.write("Format Error\n")
        error = True
    if y == -1:
        translatedMenu.write("Format Error\n")
        error == True
    if error == False:
        if p != -1:
            translatedMenu.write(name + "<em> " + str(price) + "</em>\n")
        else:
            translatedMenu.write(name + "<em> " + str(price) + "</em> <i>" + description + "</i>\n")
    X = X + 1

    ##name = re.search("[(]$", str_line)
    ##print(name.start)
##Calamari of the East <em> 6.75</em> <i>(lightly breaded Calamari)</i>
