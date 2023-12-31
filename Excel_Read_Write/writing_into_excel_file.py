import openpyxl

# File -> Workbook -> Sheets -> Rows -> Cells
path = "C:\\Users\\Shuvo\\Desktop\\testdata.xlsx"
workbook = openpyxl.load_workbook(path)
# sheet = workbook.active # if there is only 1 sheet in the excel file
sheet = workbook["Data"]

for r in range(1, 6):
    for c in range(1, 4):
        sheet.cell(r, c).value = "Welcome"

# """To store multiple data into rows and columns"""
# data =[('Emp Id', 'Emp Name', 'Designation'),
#        (1, 'XYZ', 'Manager'),
#        (2, 'ABC', 'Consultant')]
# for i in data:
#     sheet.append(i)

workbook.save(path)