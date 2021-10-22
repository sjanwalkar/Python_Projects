# Python_Projects

Project to build a python program using Greedy method or Dynamic Programming to seperate points projected on x-y plane with lines parallel to X and Y axis 
The project builds a Greedy method in O(n^4) time complexity to provide the optimal solution i.e. least numbers of lines required to isolate each points.

# How the Program works.

We have a set of points each with with X & Y coordinates. <br />
•	Start by separating the x-coordinates and y-coordinates.<br />
•	Sort the x and y coordinates.<br />
•	Form connection between each point in x and y coordinate and store those connection in co_ordinate array, so co_ordinate array contains [(0,1),(0,2)(0,3)…(1,2)..(n-1,n)] such that each point is connected to every other point.<br />
•	Create points using distance formula between adjacent x and y coordinate points (this points acts as line separating points).<br />
•	Now, for each separating point created (using distance formula) check which point separates the maximum number of x and y coordinates using the co_ordinate array and store its result.<br />
•	For each iteration store the separating point which maximizes the result for x and y coordinate. If the result is for x-coordinate means vertical line else horizontal line<br />
•	Remove the connections between points in co_ordinate array which gets separated by the selected line after each iteration.<br />
•	Repeat this process till all the connection in the co_ordinate array is removed.<br />

• This is a GREEDY ALGORITHM

# Pseudo Code
1.	Read input file in ip_data
2.	Extract number of points ‘n’, x-coordinates & y-coordinates from ip_data
3.	Sort x_coord and y_coord.			# x-coordinate & y-coordinate
4.	Create a list of ver_lines and  hor_lines by calculating distance between points
5.	For i in range(n-1):
6.	 	ver_lines.append(x_coord[i]+x_coord[i+1]/2)      #These points represent imaginary lines
7.	 	hor_lines.append(y_coord[i]+y_coord[i+1]/2)
8.	Create a list of co_ordinates which contains all indexes for traversal to each point in 
x_coord and y_coord to every other point.
For i in range(n-1)
	For j in range(i+1,n)
		co_ordinate.append(i,j)  		# (0,1),(0,2)…(1,2)…(2,3)….so on
Till now we have created vertical and horizontal lines between each pair of x_coord and y_coord and stored it in ver_lines and hor_lines. These lines separate each point in the plane.
Consider values in ver_lines and hor_lines represents a vertical/horizontal line on that particular coordinate respectively. E.g- ver_lines[1] = 2.5, means a vertical line on x=2.5


# Time for optimization
1.	Initialize selected_line= 0, selected_axis=’ ‘
2.	Run till co_ordinate != Null
3.	 	Initialize score=0
4.	 	For v in ver_lines :
5.	 		For c in co_ordinate:
6.	  			If line v separates x_coord[c[0]] and x_coord[c[1]]	# Function call
7.					Increment score
8.				Else:
9.					Return False
10.	 		If current score > previous score
11.	 			Update score
12.	 			 selected_line= v
13.	 			selected_axis = ‘vertical’
14.		For h in hor_lines :
15.	 		For c in co_ordinate:
16.	  			If line v separates y_coord[c[0]] and y_coord[c[1]]	# Function call
17.					Increment score
18.				Else:
19.					Return False
20.	 		If current score > previous score 
21.	 			Update score
22.	 			selected_line = h
23.	 			selected_axis = ‘horizontal’
24.	 	If selected_axis = ‘vertical’			# storing the result
25.	 		result.append(‘v’+selected_line)
26.	 	Else:
27.	 		result.append(‘h’+selected_line)
28.	 	For c in co_ordinates:			# updating coordinates which separates points
29.	 		If selected axis =’vertical’
30.	 			If selected_line seperates x_coord[c[0]] and x_coord[c[1]]
31.	 				Remove c from co_ordinate
32.	 		Else:
33.	 			If selected_line seperates y_coord[c[0]] and y_coord[c[1]]
34.	 				Remove c from co_ordinate
35.		
36.	Finally save result in a file.	


# Running Time Analysis
As written in the pseudocode and the actual program, the optimization code consists of outer WHILE loop which has 2 inner FOR loops(Outer FOR and Inner FOR Loop) .

The WHILE Loop runs till it doesn’t become NIL which will takes maximum of ‘n’ runs for n elements, the outer FOR loop runs for each vertical and horizontal line, so if we have 10 x-coordinated the number of lines require to separate them is (n-1) lines
Therefore, the outer FOR loop runs for (n-1) time

The Inner FOR loop will run for each co-ordinate in the co_ordinate array, so it will run for n(n+1)/2 time =n^2
 run time(Optimization) =O(n*(n-1)*n^2) =O(n4)
Process of separating X, Y coordinates  takes O(n)and Sorting will take O(n^2) time and Creating co_ordinate array will take O(n^2) time 
So, to compute total run time:
Run_time(Seperating X & Y coordinates)+Run_time(Sorting)+Run_time(Creating co_ordinate array) + Run_time(optimization i.e. while loop)

= O(n)+O(n^2) +O(n^2) + O(n^4) = O(n4)





