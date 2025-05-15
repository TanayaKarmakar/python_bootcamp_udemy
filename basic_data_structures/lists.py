my_list = [1,2,3,4,5]

print(my_list)

list_mix = ["Tanaya", 36, 67.09]

print(list_mix)

programming_languages = ["C", "C#","Java", "Kotlin", "Python", "Go"]

print(programming_languages[1:])

new_list = programming_languages + list_mix

print(f"New List {new_list}")

new_list.append("AI")

print(f"Updated new list ${new_list}")

popped_item = new_list.pop()

print(f"Popped item {popped_item}\n Updated list {new_list}")

programming_languages.sort()

print(f"Updated new list {programming_languages}")

programming_languages.reverse()

print(f"Updated reversed list {programming_languages}")