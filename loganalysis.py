# Logs Analysis Project - UDacity Nano Degree
import psycopg2

DBNAME = "news"
query1 = """SELECT *
            FROM article_views
            LIMIT 3;"""

			query2 = """SELECT name, sum(article_views.views) AS views
            FROM article_authors, article_views
            WHERE article_authors.title = article_views.title
            GROUP BY name
            ORDER BY views desc;"""

query3 = """SELECT errorlogs.date, round(100.0*errorcount/logcount,2) as percent
            FROM logs, errorlogs
            WHERE logs.date = errorlogs.date
            AND errorcount > logcount/100;"""

def connect(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

# Views need to be created for Question 2 and Question 3 as instructed on the Views.txt or Readme file.

# 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

def top_three_articles(query):
    results = connect(query)
    print('\n Displaying the most popular articles of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

# 2.  Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

def top_authors(query):
    results = connect(query)
	print('\n Displaying the most popular authors of all time:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' views')
        print(" ")

# 3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. 

def error_percentage(query):
    results = connect(query)
    print('\n The days when more than 1% of requests lead to error:\n')
    for i in results:
        print('\t' + str(i[0]) + ' - ' + str(i[1]) + ' %' + ' errors')
        print(" ")

if __name__ == '__main__':
	#print out the results	by calling the declared functions above
    
	#print the most popular articles of all time
	top_three_articles(query1)
	
	#display the most popular authors of all time by looping through the values
    top_authors(query2)
	
	#display the days when more than 1% of requests lead to errors
    error_percentage(query3)
