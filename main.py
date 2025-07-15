Courses = ["MS Office","React js","Next js","Html","CSS","R","SQL","PHP","WordPress","JSON","Typescript"]
print(Courses[6])

# print(Courses[-3])
# print(Courses[-1])
# print(Courses[2:6])
print(Courses)
# print(f"Size of the list: {len(Courses)}")
#Append
Courses.append("Python")
print(f"After Append {Courses}")
Courses.append("Hadoop")
print(f"After Append {Courses}")
#Insert
Courses.insert(6,"PWD")
print(f"After Insert {Courses}")
Courses.insert(9,"Data Analytics")
print(f"After Insert {Courses}")
# Length
print(f"Size of the list: {len(Courses)}")
# Extend
courses = ["Mongodb","flutter","Nodejs","Vuejs"]
Courses.extend(courses)
print(f"After Extend {Courses}")
# Length
print(f"Size of the list: {len(Courses)}")
#Remove
Courses.remove("Vuejs")
print(f"After Removing Vurejs : {Courses}")
Courses.remove("Html")
print(f"After Removing Html : {Courses}")
# Length
print(f"Size of the list: {len(Courses)}")
# Ascending
Courses.sort()
print(f"Ascending Order : {Courses}")
# Descending
Courses.sort(reverse=True)
print(f"Descending Order : {Courses}")
# Extend
courses_add = ["Urdu","IOT","Networking"]
Courses.extend(courses_add)
print(f"After Extend {Courses}")
# Length
print(f"Size of the list: {len(Courses)}")
#Clear
Courses.clear()
print(f"After Clearing List : {Courses}")
print(f"Size of the list: {len(Courses)}")

