# Leaderboard
The leaderboard is an interactive scoreboard that displays scores of either individual assigments or totals for all students in a specified course. Below is a screenshot of what to expect when using the leaderboard.

![](https://i.imgur.com/wDxun8o.png)

Select the course and under the <b>COLUMN</b> drop down menu on the right you will select either <b>TOTAL</b>, or an <b>Individual Assignment</b>.

Just below the drop down menus the course information is displayed with information on the selected course's term as well as the number of students enrolled.

A bar graph is displayed for the selected course and assignment which displays students scores compared to other students Click on a specific bar to display that student's information.

# Code Example

![](https://i.imgur.com/pWfqZaJ.png)

The above picture is a snapshot from the main class in our application. The first bit that it shows is to receive arguments from the command line. <br>

The second part is the initialization of the JFrame to create the Graphical User Interface <br>

To handle the data there is a FileSource interface that supports .csv and .json files as well as a WebSource interface that supports .json files. The data that gets displayed in the BarChart is rearranged and reorganized when needed to be in complience with the data types that functions need to work as intended.

# Testing

To test the application, you use the .ROBOT files that were included with each feature that was given to use by our professor. To run the tests, you execute the command "gradle runrobot" command within the root folder.<br>

Here is an example of one of the robot tests.

![](https://i.imgur.com/jbcwxbW.png)

# Motive for this project

This was a project made by myself and 5 other group members. We developed this applicaiton in my Software Engineering 1 class at Jacksonville State University. This was our first experience working together as part of a group using the agile process scrum. We were tasked with adding 7 features over the semester, all of which, we passed.

# Libraries and Resources

Gradle Build Tool<br>
Maven Repositories<br>
'org.json:json:20160810'<br>
'com.googlecode.json-simple:json-simple:1.1.1'<br>
'org.jfree:jfreechart:1.0.19'<br>
'gradle.plugin.org.roboscratch.gradle:gradle-robot:0.1.1'<br>
'org.robotframework:swinglibrary:1.9.6'<br>
'org.robotframework:javalib-core:1.2.1'<br>
'net.sf.opencsv:opencsv:2.3'
