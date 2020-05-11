import openpyxl

path = "/home/deadman/Documents/blank.xlsx"

workbook = openpyxl.load_workbook(path)
sheet=workbook.active

for r in range (1,6):
    sheet.cell(row=r,column=6).value="welcpme"
    
workbook.save(path)        





