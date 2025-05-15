myfile = open('test.txt')

file_content = myfile.read()

print(file_content)

myfile.seek(0)

file_content1 = myfile.read()

print("\n\n")

print(file_content1)

myfile.seek(0)

lines = myfile.readlines()

print(lines)

myfile.close()


with open('test.txt') as file:
    content = file.read()
    print(f"current line : {content}")