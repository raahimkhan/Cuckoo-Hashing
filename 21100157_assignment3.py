times_called = 0
max_calls = 11
key_list = []
function_id = 0
total = 0
k = None

cycle_counter = 0

table1 = [-999] * 11
table2 = [-999] * 11

def isdigit(val):
    if val.lstrip('-').isdigit():
        return True
    else:
        return False

def hash1(key, id):
    return (key + id) % 11

def hash2(key, id):
    return int(((key + id)/11) % 11)

def insert(key, table):
    global table1
    global table2
    global times_called
    global max_calls
    global key_list
    global function_id
    global total
    global k
   
    if times_called == max_calls:
        print('Cycle detected! Rehashing keys with new hash functions!')
        
        # Reinitialize hashtables
        for i in range (0, 11):
            table1[i] = -999
            table2[i] = -999
            
        function_id = function_id + 3
        times_called = 0
        total = 0
        
        for data in key_list:
            k = data
            insert(data, 1)
        print('All keys have been rehashed!')
        print('')
        return
        
    else:
        # First check whether key to be inserted is already present in any of the hash tables or not
        h1 = hash1(key, function_id)
        h2 = hash2(key, function_id)
        if table1[h1] == key or table2[h2] == key:
            print(k, ' already present in hash table!')    
            print('')
            return
        
        # If not already present insert in proper table
        if table == 1:
            if table1[h1] != -999:   # Collision. Some key already present at this index in table 1
                temp = table1[h1] # store old key in variable temp
                table1[h1] = key # store new key in place of old key in table 1
                times_called = times_called + 1
                insert(temp, 2) # Re-hash old key in second table
            else: # if empty
                table1[h1] = key
                times_called = 0
                total = total + 1
                print(k, ' added successfully!')
                print('')
                return
                
        elif table == 2:
            if table2[h2] != -999:
                temp = table2[h2]
                table2[h2] = key
                times_called = times_called + 1
                insert(temp, 1)
            else:
                table2[h2] = key
                times_called = 0
                total = total + 1
                print(k, ' added successfully!')
                print('')
                return 
            
def print_tables():
    global table1
    global table2
    
    print ('table1: ', end =" ")
    for i in range (0, 11): 
        if i == 10:
            if table1[i] == -999:
                print ('empty')
            else:
                print (table1[i])
        else:    
            if table1[i] == -999:
                print ('empty ', end =" ")
            else:
                print (table1[i], ' ', end =" ")
    
    print ('table2: ', end =" ")
    for i in range (0, 11): 
        if i == 10:
            if table2[i] == -999:
                print ('empty')
            else:
                print (table2[i])
        else:    
            if table2[i] == -999:
                print ('empty ', end =" ")
            else:
                print (table2[i], ' ', end =" ")
 
def lookup(key):
    global table1
    global table2
    
    h1 = hash1(key, function_id)
    h2 = hash2(key, function_id)
    
    if table1[h1] == key:
        print(key, ' is present in table1[', h1, ']')
        print('')
    elif table2[h2] == key:
        print(key, ' is present in table2[', h2, ']')
        print('')
    else:
        print(key, ' is not present in either of the two hash tables')
        print('')

def delete(key):
    global table1
    global table2
    global total
    
    h1 = hash1(key, function_id)
    h2 = hash2(key, function_id)
    
    if table1[h1] == key:
        table1[h1] = -999
        print('Element ', key, ' deleted successfully')
        total = total - 1
        key_list.remove(key)
        print('')
    elif table2[h2] == key:
        table2[h2] = -999
        print('Element ', key, ' deleted successfully')
        total = total - 1
        key_list.remove(key)
        print('')
    else:
        print('Element ', key, ' not present in any of the hash tables')
        print('')

def main():
    global key_list
    global total
    global k
    while True:
        truth = False
        truth2 = False
        print('Press 1 to insert key')
        print('Press 2 to search key')
        print('Press 3 to delete key')
        print('Press 4 to print hash tables')
        print('Press 0 to quit')
        print('')
        
        while truth != True:
            user_input = input('Enter your choice : ')
            truth = isdigit(user_input)
            if truth == False:
                print('Numerics only please! Enter again.')
                
        print('')
        
        if user_input == '0':
            print('Allah Hafiz!')
            break
        
        elif user_input == '1':
            while truth2 != True:
                k = input('Enter key to be inserted (one at a time) : ')
                truth2 = isdigit(k)
                if truth2 == False:
                    print('Numerics only please! Enter again.')
                    
            k = int(k)
        
            if total == 11:
                print('Limit reached! Cannot add more')
                print('')
            else:
                key_list.append(k)
                key_list = list(dict.fromkeys(key_list))
                insert(k, 1)
        
        elif user_input == '2':
            while truth2 != True:
                k = input('Enter key to be searched : ')
                truth2 = isdigit(k)
                if truth2 == False:
                    print('Numerics only please! Enter again.')
                    
            k = int(k)
            lookup(k)
            
        elif user_input == '3':
            while truth2 != True:
                k = input('Enter key to be deleted : ')
                truth2 = isdigit(k)
                if truth2 == False:
                    print('Numerics only please! Enter again.')
                    
            k = int(k)
            delete(k)
            
        elif user_input == '4':
            print_tables()
            print('')
        
        else:
            print('Invalid choice! Please enter again')
            print('')
  
main()
   