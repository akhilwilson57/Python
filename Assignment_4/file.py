'''
Hardcoding
try:
    file1 = open('sample.txt', 'r')
    reading_file_line1=file1.readline()
    reading_file_line2=file1.readline()
    print("Reading file content:")
    print("Line 1:", reading_file_line1)
    print("Line 2:", reading_file_line2)
    file1.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")'''

try:
    #with open automatically closes the file after reading the contents in the file
    with open('sample.txt','r') as f:
        print("Reading file content:")
        #f is file object iterating over it gives one line at a time
        #enumerate(f,start=1) in i the line number gets stored
        #line.stip prints contents from the file removing the new line space that can
        #be seen in output if you just use line in the placeholder
        for i, line in enumerate(f,start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")




