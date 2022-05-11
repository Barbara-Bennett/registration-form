name = []
height = []
age = []
for i in range(1,11):
     name.append(input('\nName: '))
     height.append(float(input('Height: ')))
     age.append(int(input('Age: ')))
total = len(height)
average = sum(height) / total
smallestHeight = min(height)
smallestName = name[height.index(smallestHeight)]
tallestHeight = max(height)
tallestName = name[height.index(tallestHeight)]
newAge = min(age)
newName = name[age.index(newAge)]
oldAge = max(age)
oldName = name[age.index(oldAge)]
print(f'\nAverage age: {average}')
print(f'Shortest person: {smallestName}')
print(f'Tallest person: {tallestName}')
print(f'Newest person: {newName}')
print(f'Oldest person: {oldName}')
