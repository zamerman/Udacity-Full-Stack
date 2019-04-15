#!/usr/bin/env python3

#
# project_1
#
# Author: Zachary Amerman
# Date: March 1, 2019
# Revised Date: March 2, 2019
# Program: Full Stack Web Developer Nanodegree
# Python Version: 3.5.2
#

import psycopg2
import sys

# Defining string variables for sql requests
sql_request_1 = '''SELECT
                articles.title,
                pathview.requests AS views
             FROM
                articles,
                pathview
             WHERE
                pathview.path = '/article/' || articles.slug
             ORDER BY
                views DESC
             LIMIT 3'''

sql_request_2 = '''SELECT
                authors.name,
                SUM(pathview.requests) AS views
             FROM
                authors,
                articles,
                pathview
             WHERE
                authors.id = articles.author
                AND pathview.path = '/article/' || articles.slug
             GROUP BY
                authors.name
             ORDER BY
                views DESC;'''

sql_request_3 = '''SELECT
                date_trunc('day', time) AS date,
                SUM(CASE WHEN status != '200 OK' THEN 1 ELSE 0 END)/
                    CAST(COUNT(*) AS REAL)*100 AS request_ratio
             FROM
                log
             GROUP BY
                date
             HAVING
                SUM(CASE WHEN status != '200 OK' THEN 1 ELSE 0 END)/
                    CAST(COUNT(*) AS REAL) > 0.01
             ORDER BY
                request_ratio DESC;'''

# Attempt to connect to the news database and create a cursor
try:
    db = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print('Connection Error!')
    print(e.pgerror)
    print(e.diag.message_detail)
    sys.exit(1)
else:
    print('Connected to Database!')
c = db.cursor()

# Execute the sql requests and store the resulting lists in a variable
# Use a for loop to print results to console
print("\nViews per Article for Top 3 Articles in Descending Order")
c.execute(sql_request_1)
dbdata = c.fetchall()
for item in dbdata:
    print('{article} : {views}'.format(article=item[0], views=item[1]))

print("\nViews per Author in Descending Order")
c.execute(sql_request_2)
dbdata = c.fetchall()
for item in dbdata:
    print('{author} : {views}'.format(author=item[0], views=item[1]))

print("\nRequest error percentages > 1% each day in Descending Order")
c.execute(sql_request_3)
dbdata = c.fetchall()
for item in dbdata:
    print('{date} : {error_ratio}%'.format(date=item[0], error_ratio=item[1]))

# Close the database and cursor
c.close()
db.close()
