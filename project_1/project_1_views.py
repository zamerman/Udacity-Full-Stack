#!/usr/bin/env python3

#
# project_1
#
# Author: Zachary Amerman
# Date: March 2, 2019
# Program: Full Stack Web Developer Nanodegree
# Python Version: 3.5.2
#
# This program sets up the views that will be used by the main program to
# collect our desired information.
#

import psycopg2
import sys

# variables to store our SQL commands to create views
sql_view_request = ''' CREATE VIEW pathview AS
             SELECT
                path,
                COUNT(*) as requests
             FROM
                log
             GROUP BY
                path
             '''

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

# Execute the SQL commands to create our required view and commit changes
c.execute(sql_view_request)
db.commit()

# Close database and cursor
c.close()
db.close()
