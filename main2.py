file_read = open('file for file handling in python.txt', 'r')
print("file in read mode------------------")
print(file_read.read())
file_read.close()

file_write = open('file for file handling in python.txt', 'w')
file_write.write("file in write mode i will fill a 100 pages!!!")
file_write.write("hi i am the devastater!!!. i am 1000 years old")
file_write.close()

file_append = open('file for file handling in python.txt', 'a')
file_append.write("\n file i append mode ..h..a..h..a..")
file_append.write("\n hi i am the controler i can control everything. i am 2700 years old")
file_append.close()