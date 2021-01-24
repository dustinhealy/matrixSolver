# rows = int(input("How many rows are in your matrix?\n"))
# columns = int(input("How many columns are in your matrix?\n"))
# matrix = [[0 for rows in range(rows)] for columns in range(columns)] 
# count = 0
# rowStrings = [None] * rows
# while count < rows:
#     rowStrings[count] = input("Enter row\n")
#     count += 1
from fractions import Fraction
def divide(numberedRows, startingNumber: int):
    length = len(numberedRows)
    count = 0
    while count < length:
        numberedRows[count] = Fraction(numberedRows[count] / startingNumber)
        count += 1
    return numberedRows

count = 0
rows = []
numberedRows = []
while True:
    q = input("Enter Row (Enter empty row when done)\n")
    if q == "":
        print ("{} rows entered".format(count))
        break
    rows.append(q)
    count += 1
x = 0
while x < count:
    numberedRows.append(list(map(int, rows[x].split())))
    print (numberedRows[x])
    x += 1
x = 0
y = 0
while x < len(numberedRows):
    if numberedRows[x][x] != 1:
        print("\n{}".format(divide(numberedRows[x], numberedRows[x][x])))
        while y < len(numberedRows):
            if numberedRows[x][y] != 0 and x != y:
                subtract(numberedRows(x), numberedRows)
    x += 1