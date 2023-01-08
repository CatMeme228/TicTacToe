class Field():
    def __init__(self):
        self.cells=['_', '_', '_', '_', '_', '_', '_', '_', '_']

    def print(self):
        print(self.cells[0], self.cells[1], self.cells[2])
        print(self.cells[3], self.cells[4], self.cells[5])
        print(self.cells[6], self.cells[7], self.cells[8])

    def setSymdol(self, symbol, y, x):
        self.cells[x*3+y] = symbol


myField= Field()
myField.cells
myField.print()

for i in range(10):
    if myField.cells[0] == myField.cells[1] == myField.cells[2] == '0' or myField.cells[0] == myField.cells[1] == myField.cells[2] == 'x':
        print(myField.cells[0], 'Won')
        exit()
    elif myField.cells[3] == myField.cells[4] == myField.cells[5] == '0' or myField.cells[3] == myField.cells[4] == myField.cells[5] == 'x':
        print(myField.cells[3], 'Won')
        exit()
    elif myField.cells[6] == myField.cells[7] == myField.cells[8] == '0' or myField.cells[6] == myField.cells[7] == myField.cells[8] == 'x':
        print(myField.cells[6], 'Won')
        exit()
    elif myField.cells[0] == myField.cells[3] == myField.cells[6] == '0' or myField.cells[0] == myField.cells[3] == myField.cells[6] == 'x':
        print(myField.cells[0], 'Won')
        exit()
    elif myField.cells[1] == myField.cells[4] == myField.cells[7] == '0' or myField.cells[1] == myField.cells[4] == myField.cells[7] == 'x':
        print(myField.cells[1], 'Won')
        exit()
    elif myField.cells[2] == myField.cells[5] == myField.cells[8] == '0' or myField.cells[2] == myField.cells[5] == myField.cells[8] == 'x':
        print(myField.cells[2], 'Won')
        exit()
    elif myField.cells[0] == myField.cells[4] == myField.cells[8] == '0' or myField.cells[0] == myField.cells[4] == myField.cells[8] == 'x':
        print(myField.cells[0], 'Won')
        exit()
    elif myField.cells[2] == myField.cells[4] == myField.cells[6] == '0' or myField.cells[2] == myField.cells[4] == myField.cells[6] == 'x':
        print(myField.cells[2], 'Won')
        exit()
    elif i == 9:
        print('Draw')

    else:
        inp_Symbol = input()
        inp_x = int(input())
        inp_y = int(input())
        myField.setSymdol(inp_Symbol, inp_y-1, inp_x-1)
        myField.print()