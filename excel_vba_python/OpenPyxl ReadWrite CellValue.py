# Read from and write to an Excel file using the OpenPyxl library.
# The OpenPyxl read the files directly - it doesn't interact with Excel.
# YouTube Video: https://youtu.be/6qo3ly3-_I8
import openpyxl

# Load the file(change the Path to where the file is stored)
book  =  openpyxl.load_workbook(r'c:\sandbox\marks.xlsx')
# Get the worksheet
sheet = book["Results"]

# Print the value at A10 on sheet Results
print(sheet["A10"].value)

# Change the value in cell B15
sheet['B15'] = '9'
# The new value will not appear until you save the file
book.save(r'c:\sandbox\marks.xlsx')