test_list = ['magical unicorns',19,'hello',98.98,'world']

running_string = ""
running_sum = 0
list_type = ""

for item in test_list:
    if (type(item) == int):
        running_sum += item
    elif (type(item) == str):
        running_string += " " + item

if (len(running_string) > 0 and running_sum != 0):
    list_type = "mixed"
    print "The list you entered is of", list_type, "type."
    print "Sum:", running_sum
    print "String:", running_string
elif (len(running_string) > 0):
    list_type = "string"
    print "The list you entered is of", list_type, "type."
    print "String:", running_string
elif (running_sum != 0):
    list_type = "integer"
    print "The list you entered is of", list_type, "type."
    print "Sum:", running_sum