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

print(inventory)