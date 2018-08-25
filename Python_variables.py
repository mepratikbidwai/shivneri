#Single assignment
numb = 23;
flt = 100.01;
myChar = "My name is Vicky";

print numb;
print flt;
print myChar;

#multiple assignment
a = b = c = 98;

print ("a is %d, b is %d, c is %d." %(a, b, c));

var1, var2, var3 = 23, 100.01, "My Name is Priya";

print ("var1 is %d, var2 is %f, var3 is %s" %(var1, var2, var3));

#If below line uncommented it will make next statement throw error
#del a;
print ("a is %d" %a);

var4 = 474599L

print ("Long var4 %d" %var4);

#Complex datatype
var5 = 23+34j;

print ("Complex var5 is :",  var5);

#String operations
str1 = "Hello world"
print ("str1[0] - %s" %str1[0])

#print from character 3 to 10
print ("str1[2:9] - %s" %str1[2:9])

str2 = " My name is Computer"

str3 = str1 + ". " + str2;

print ("str1 + str2 is %s" %(str1 + str2))

#Python lists
myList = ['Pratik', '23.5', 'Mumbai', 83, 'Akola', '79']

print ("mylist is :", myList[5]); 

#print 1 to 5 items from list
print ("myList[1:5] is :", myList[1:5]);

