# CS-430 Project
instance_no = '02'      # change the variable as per your instance no: For eg. instance05 ---> change to '05'
ip_filename = "instance"+str(instance_no)+".txt"
with open(ip_filename) as data:
    ip_data = data.read()

a =''
values =[]

for val in ip_data:
    if val != "\n" and val !=' ':
        a = a+val
    elif val == "\n":
        values.append(a)
        a = ''
    elif val == ' ':
        values.append(a)
        a = ''
values.append(a)
if a =='':      # if there is extra space in the input file at the end.
    length = len(values)-1
else:
    length = len(values)
print(values)

ip_data = values[1:length]
n=int(values[0])
x_cord = []
y_cord = []
x_cord1= []  # for storing sorted values
y_cord1= []  # for storing sorted values

for i in range(len(ip_data)):
    if i%2 == 0 :
        x_cord.append(int(ip_data[i]))
        x_cord1.append(int(ip_data[i]))
    else:
        y_cord.append(int(ip_data[i]))
        y_cord1.append(int(ip_data[i]))

print("No of Co-ordinates\t"+str(n))
print("X-cordiantes\t"+str(x_cord))
print("Y-cordiantes\t"+str(y_cord))



# sorting coordinates based on X-axis
x_cord1.sort()

print("\nAfter Sorting along x-coordinates")
print("X-cordiantes\t"+str(x_cord1))



# Sorting co-ordinates based on y-axis
y_cord1.sort()


print("\nAfter Sorting along y-coordinates")
print("Y-cordiantes\t"+str(y_cord1))

# Adding Vertical/horizontal lines after each x/y-coordiante

ver_lines =[]
hor_lines =[]
ver_line =0
hor_line =0
selected_line=0
selected_axis =''
co_ordiantes =[]

# Separating x-coordinates with vertical lines

for i in range(n-1):
    if x_cord1[i] != x_cord1[i+1]:
        line = (x_cord1[i]+x_cord1[i+1])/2
        ver_lines.append(str(line))
        for j in range(i+1,n):
            var = []
            var.append(str(i))
            var.append(str(j))
            co_ordiantes.append(var)


# Separating y-coordinates with horizontal lines
for i in range(n-1):
    if y_cord1[i] != y_cord1[i+1]:
        line = (y_cord1[i]+y_cord1[i+1])/2
        hor_lines.append(str(line))


# printing the vertical and horizontal lines formed
lines=[]
h =len(hor_lines)
v =len(ver_lines)
no_lines =h+v
lines.append(no_lines)
for val in hor_lines:
    lines.append(val)

for val in ver_lines:
    lines.append(val)

print("********  Before Optimization *********")
for i in range(h+v+1):
    print(lines[i])


result= []
final_result =[]

# ***************Optimization************************
# Checking numbers of points separated for each vertical and horizontal line
print("*******  After Optimization **********")

def points_seperated(point,axis, line):         # function to check line separates points or not
    if axis == 'v':                       # vertical line
        if(x_cord[int(point[0])] < float(line) and x_cord[int(point[1])] < float(line))  or (x_cord[int(point[0])] > float(line) and x_cord[int(point[1])] >float(line)) :
            return 0
        else:
            return 1

    elif axis =='h':                      #  horizontal line
        if(y_cord[int(point[0])] < float(line) and y_cord[int(point[1])] < float(line))  or (y_cord[int(point[0])] > float(line) and y_cord[int(point[1])] >float(line)) :
            return 0  # line dosent separates points
        else:
            return 1  # line  separates points





while len(co_ordiantes)>0:
    score = 0
    for val in ver_lines:
        # define separation
        ans = 0
        for i in co_ordiantes:          # calculate the maximum points separated by each vertical line
            if points_seperated(i, 'v', val) == 1:
                ans = ans + 1
        x =ans

        if x > score:
            score = x
            selected_line = val
            selected_axis = 'v'
    for val in hor_lines:
        # define separation
        ans = 0
        for i in co_ordiantes:          # calculate the maximum points separated by each vertical line
            if points_seperated(i, 'h', val) == 1:
                ans = ans + 1
        x = ans

        if x > score:
            score = x
            selected_line = val
            selected_axis = 'h'
    print("-----")
    print(score)
    print(selected_axis)
    print(selected_line)
    if selected_axis =='v':
        result.append("v "+selected_line)
    else:
        result.append("h "+selected_line)

    # deleting co-ordiantes lines
    temp_coordinates =[]                        # to store co-ordiantes that gets separated by the  selected line
    for val in co_ordiantes:
       if points_seperated(val,selected_axis, selected_line) ==1:
           temp_coordinates.append(val)
    for val in temp_coordinates:
        co_ordiantes.remove(val)


final_result.append(len(result))
for val in result:
    final_result.append(val)
print(final_result)


# Writing o/p to the txt file
op_filename = "greedy_solution"+str(instance_no)+".txt"
f =open(op_filename,"w")
for i in final_result:
    f.write(str(i))
    f.write("\n")

f.close()
