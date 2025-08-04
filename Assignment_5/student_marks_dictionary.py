dict1 = {'Akhil':49,'Alice':65, 'Rohan': 78,'Shubham':83}
#print(dict1)
a = input("Enter the student's name: ").strip()
if a in dict1:
     print("{}'s marks:".format(a),dict1[a])
     #print(dict1.get(a))
else:
     print("Student not found.")
