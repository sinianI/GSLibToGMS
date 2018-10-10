import numpy as np
import xlsxwriter


def get_value(filename):
    file = open(filename, 'r')

    value=[]

    for line in file:

        value.append(line)

    return value


value = get_value('lantest.txt')
print(value)

list_para = value[0].split(' ')


x = np.asanyarray(list_para[0], int)
y = np.asanyarray(list_para[1], int)
z = np.asanyarray(list_para[2], int)
r = np.asanyarray(list_para[3], int)

print(x)
print(y)

list_data = value[3:]

print(list_data)

myarray = np.asanyarray(list_data,float)


a = np.reshape(myarray, (x, 38))

b = np.flip(a, 0)

print(b)

workbook = xlsxwriter.Workbook('GMSVer.xlsx')
worksheet = workbook.add_worksheet()


cols, rows = b.shape


for col in range(cols):
    for row in range(rows):

                worksheet.write(col, row, b[col][row])

workbook.close()



