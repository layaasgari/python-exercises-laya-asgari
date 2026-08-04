a=input('Please entre your first and last name: ')
space_index=a.find(' ')
first_name=a[0]
last_name=a[space_index + 1:]
print(first_name,'.',last_name)