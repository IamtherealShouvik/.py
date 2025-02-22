print('Praveen\'s tab') #valid
print("Praveen's tab") #valid
#print('Praveen's tab') #invalid
print('''Praveen's tab''') #valid
print("C:\documents\print.py")
print("C:\documents\next.py") #\d & \n are treated as esc seq.s
print("C:\\documents\\next.py") #valid
print("text *10") #prints the line once
print("text "*10) #prints 10 times
print(r"C:\documents\next.py")
'''
This triple quotes can be used for multi-line 
comments alongside the normal hashtag symbol
at the beginning of every line. It won't be printed.
'''