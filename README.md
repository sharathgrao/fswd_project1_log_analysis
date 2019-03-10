## Logs Analysis Project - Udacity Full Stack Web Developer Nanodegree

### TASK / PROJECT

You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

#### RUNNING THE PROGRAM
1. To get started, I recommend the user use a virtual machine to ensure they are using the same environment that this project was developed on, running on your computer. You can download [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) to install and manage your virtual machine.
Use `vagrant up` to bring the virtual machine online and `vagrant ssh` to login.

2. Download the data provided by Udacity [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file in order to extract newsdata.sql. This file should be inside the Vagrant folder. 

3. Load the database using `psql -d news -f newsdata.sql`. 

4. Connect to the database using `psql -d news`.

5. Create the Views given below. Then exit `psql`.

6. Now execute the Python file - `python logs_analysis.py`.

### VIEWS FOR THE PROGRAM

#### FOLLOWING VIEWS ARE CREATED FOR QUESTION 2 & QUESTION 3:

##### Question 2 VIEW
```sql
CREATE VIEW article_authors AS
SELECT title, name
FROM articles, authors
WHERE articles.author = authors.id;
```
```sql 
CREATE VIEW article_views AS
SELECT title, count(log.id) as views
FROM articles, log
WHERE log.path = CONCAT('/article/', articles.slug)
GROUP BY articles.title
ORDER BY views desc;
```

##### Question 3 VIEW
```sql
CREATE VIEW logs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as LogCount
FROM log
GROUP BY Date;
```
```sql
CREATE VIEW errorlogs AS
SELECT to_char(time,'DD-MON-YYYY') as Date, count(*) as ErrorCount
FROM log
WHERE STATUS = '404 NOT FOUND'
GROUP BY Date;
```