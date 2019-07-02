inventory = {
    'wold': 500,
    'pouch': ['flint','twine','gemstone'],
    'backpack':[ 'xylophone','dagger','bedroll','bread loaf']
}
#Add a key to inventory called 'pocket'.
inventory['tui']= []
 #Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'.

lis = ['seashell','strange berry','lint' ]
for v in lis: 
    inventory['tui'].append(v)


#Then .remove('dagger') from the list of items stored under the 'backpack' key.

del inventory['backpack'][1]

print(inventory['backpack'])
#Add 50 to the number stored under the 'gold' key.

inventory['wold']=[inventory['wold']]
for x in range(0,50,1):

    inventory['wold'].append(x)

print(inventory['wold'])


    


    

print(inventory)