'''file1 = open("output.txt", 'w')
write = input("Enter text to write to the file: ")
file1.write(write + "\n")
print("Data successfully written to output.txt.")
file1.close()


file1 = open("output.txt", 'a')
append = input("Enter additional text to append to the file: ")
file1.write(append + "\n")
print("Data successfully appended.")
file1.close()

file1 = open("output.txt", 'r')
content = file1.read()
print("Final content of output.txt: ")
print(content)'''


with open("output.txt", 'w') as file:
    write = input("Enter text to write to the file: ")
    file.write(write + "\n")
    print("Data successfully written to output.txt.")

with open("output.txt", "a") as file:
    append = input("Enter additional text to append: ")
    file.write(append + "\n")
    print("Data successfully appended.")

with open("output.txt", 'r') as file:
    content = file.read()
    print("Final content of output.txt: ")
    print(content)

