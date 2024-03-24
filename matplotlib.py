# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 16:36:51 2023

@author: Chetan Surashe
"""
# python program to draw a line with suitable label
import matplotlib.pyplot as plt
X=range(1,50)
Y=[i*3 for i in X] #list comprehension
print("values of X: ")
print(*range(1,50))
#  *  -->is equivalent to i in range (1,50):
#           print(i,end='')

print("values of Y(thrice of X): ")
print(Y)
#plot lines and/or markers to the Axes.
plt.plot(X,Y)
#Set the X axis label of the current axis.
plt.xlabel('x-axis')
#Set the Y axis label of the current axis.
plt.ylabel('y-axis')
#Set a title
plt.title('Draw a line.')
#Display the figure
plt.show()
###############################################

#python program to draw a line using given
#axis values with suitable label in the 
#x-axis ,y-axis and a title

import matplotlib.pyplot as plt
x=[1,2,3]
y=[2,4,1]

#plot lines and/or makers to the axes
plt.plot(x,y)
#set the x-axis label of the current axis
plt.xlabel('x-axis') 
#set the y-axis label of the current axis
plt.ylabel('y-axis')
#set a title
plt.title('sample graph!')
#display a figure
plt.show() 

###############################################

#python program to add legend in the graph

import matplotlib.pyplot as plt
#line 1 pts.
x1=[10,20,30]
y1=[20,40,10]

#line 2 pts
x2=[10,20,30]
y2=[40,10,30]

#plotting the line 1 pts
plt.plot(x1,y1,label="line 1")
#plotting the line 2 pts
plt.plot (x2,y2,label="line 2")

plt.xlabel('x-axis')
plt.ylabel('y-axis')

#set a title of the current axes
plt.title('Two or more lines on same plot with suitabel legends ')
#show legend on plot
#legend means in the corner red line as line 2 such
#kind of label
plt.legend()
#display the figure
plt.show()

#################################################

#python program to plot 2 or more lines
#with legends,different widths and colors
import matplotlib.pyplot as plt
#line 1 pts.
x1=[10,20,30]
y1=[20,40,10]

#line 2 pts
x2=[10,20,30]
y2=[40,10,30]

#set the x-axis label of the current axis
plt.xlabel('x-axis') 
#set the y-axis label of the current axis
plt.ylabel('y-axis')

#set a title
plt.title('Two or more lines with different width and color with suitabe legends ')

#plotting the line 1 pts
plt.plot(x1,y1,color='blue',linewidth=3,label='line 1-width3')
#plotting the line 2 pts
plt.plot (x2,y2,color='red',linewidth=5,label='line2-width5')
plt.legend()
#display the figure
plt.show()

################################################

#python program to plot 2 or more lines
#with different styles.
import matplotlib.pyplot as plt
#line 1 pts.
x1=[10,20,30]
y1=[20,40,10]

#line 2 pts
x2=[10,20,30]
y2=[40,10,30]

#set the x-axis label of the current axis
plt.xlabel('x-axis') 
#set the y-axis label of the current axis
plt.ylabel('y-axis')


#set a title
plt.title('Two or more lines with different width and color,style with suitabe legends ')

#plotting the line 1 pts
plt.plot(x1,y1,color='blue',linewidth=3,label='line 1-dotted',linestyle='dotted')
#plotting the line 2 pts
plt.plot (x2,y2,color='red',linewidth=5,label='line2-dashed',linestyle='dashed')
plt.legend()
#display the figure
plt.show()

###############################################

import matplotlib .pyplot as plt 

#x-axis values
x=[1,4,5,6,7]
#y axis values
y=[2,6,3,6,3]

#plotting the  pts
plt.plot(x,y,color='red',linestyle='dashdot'
    ,linewidth=3,marker='o',markerfacecolor='blue',
    markersize=12)
#set the y limits for the current axes
plt.ylim(1,8)
#set the x limits for the current axes
plt.xlim(1,8)
#naming the x axis
plt.xlabel('x-axis')
#naming the y axis
plt.ylabel('y-axis')
plt.title('marker graph!')
plt.legend()
plt.show()

#python program to display bar graph
#to display popularity of programming langs.

import matplotlib.pyplot as plt
x = ['Java', 'Python', 'PHP', 'Javascript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 7.7, 6.7, 5.5]  # Added a value for 'C++'
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, popularity, color='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")
plt.xticks(x_pos, x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.show()

################################################

import matplotlib.pyplot as plt

x = ['Java', 'Python', 'PHP', 'Javascript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 7.7, 6.7, 5.5]  # Added a value for 'C++'
y_pos = [i for i, _ in enumerate(x)]  # Use y_pos for positioning bars

plt.barh(y_pos, popularity, color='blue')  # Use barh for horizontal bars
plt.ylabel("Languages")
plt.xlabel("Popularity")
plt.title("Popularity of Programming Languages")
plt.yticks(y_pos, x)  # Use yticks for y-axis labels
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.show()


##############################################

import matplotlib.pyplot as plt
x=['java','python','PHP','Javascript','C#','C++']
popularity=[22.2 ,17.6 ,8.8 ,7.7 ,6.7,5.5]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=(0.4,0.6,0.8,1.0))
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming language")
plt.xticks(x_pos,x)
#turn on the grid
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()

##############################################
import matplotlib.pyplot as plt
x=['java','python','PHP','Javascript','C#','C++']
popularity=[22.2,17.6,8.8,7.7,6.7,6.3]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=['red','black','green','blue','yellow','white'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of programming language")
plt.xticks(x_pos,x)
#turn on the grid
#plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
