# Dictionaries are Python's implementation of a data structure that is more generally known as an associative array.

# Create dictionaries 
person = {
    'first_name': 'Jane',
    'last_name': 'Doe',
    'age': 30
}
#Get values
print(person['first_name'])
print(person.get('last_name'))

# Add Key/Value
person['phone'] = '254-708685673'

# Get dict keys
print(person.keys())

#Get dict items
print(person.items())