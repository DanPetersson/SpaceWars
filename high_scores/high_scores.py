#!/usr/bin/env python3

import sqlite3
import time
import random
from datetime import datetime

 
from sqlite3 import Error
 
""" 
def sql_connection(db_file_name = 'high_scores.db'):
    try:
        con = sqlite3.connect(db_file_name)
        return con
    except Error:
        print(Error)
 
def create_sql_table(con):
    cursor_object = con.cursor()
    cursor_object.execute("create table if not exists high_score_table(time_stamp integer PRIMARY KEY, name text, score integer, date)")
    con.commit()


def insert_sql_table(con, time_stamp, name, score, date):
    cursor_object = con.cursor()
    cursor_object.execute('INSERT INTO high_score_table(time_stamp, name, score, date) VALUES(?, ?, ?, ?)', (time_stamp, name, score, date))
    con.commit()

def print_sql_table(con):
    cursor_object = con.cursor()
    cursor_object.execute('SELECT * FROM high_score_table')
    rows = cursor_object.fetchall()
    for row in rows:
        print(row)

def get_top_5_sql(con):
	# Not tested and need to understand better
    cursor_object = con.cursor()
    cursor_object.execute('select * from high_score_table')
    cursor_object.execute('where score = (SELECT max(score) FROM high_score_table)')
    cursor_object.execute('order by score desc')
    cursor_object.execute('limit 3')
    rows = cursor_object.fetchall()
    print(rows)
    return rows

def get_top_5_list(con):
    
    def take_score(elem):
        return elem[2]

    cursor_object = con.cursor()
    cursor_object.execute('SELECT * FROM high_score_table')
    rows = [row for row in cursor_object.fetchall()]
    rows.sort(key=take_score, reverse=True)
    if len(rows) < 5:
        return rows
    else:
    	return(rows[:5])

def drop_sql_table(con):
    cursor_object = con.cursor()
    cursor_object.execute('drop table if exists high_score_table')
"""
#-----------------------------------------------------------------

def high_scores_connect_to_db(db_file_name = 'high_scores.db'):
    try:
        db_connection = sqlite3.connect(db_file_name)
        return db_connection
    except Error:
        print(Error)

def high_scores_create_table(db_connection):
    cursor_object = db_connection.cursor()
    cursor_object.execute("create table if not exists high_score_table(time_stamp integer PRIMARY KEY, name text, score integer, date)")
    db_connection.commit()


def high_scores_update_db(db_connection, name, score):

    def insert_sql_table(con, time_stamp, name, score, date):
        cursor_object = con.cursor()
        cursor_object.execute('INSERT INTO high_score_table(time_stamp, name, score, date) VALUES(?, ?, ?, ?)', (time_stamp, name, score, date))
        con.commit()
    
    now = datetime.now()
    time_stamp = int(datetime.timestamp(now))
    #insert_sql_table(db_connection, time_stamp, name, score, now.date())
    cursor_object = db_connection.cursor()
    cursor_object.execute('INSERT INTO high_score_table(time_stamp, name, score, date) VALUES(?, ?, ?, ?)', (time_stamp, name, score, now.date()))
    db_connection.commit()



def high_scores_top_list(db_connection, length=5, name='*'):
    '''
    def high_scores_top_list(lenght=5, name='*')
    returns a sorted list of tops scores from db of lenght=length
    '''
    def take_score(elem):
        ''' score is the third element in the row '''     
        return elem[2]

    cursor_object = db_connection.cursor()
    cursor_object.execute('SELECT * FROM high_score_table')
    rows = [row for row in cursor_object.fetchall()]
    rows.sort(key=take_score, reverse=True)
    if len(rows) < length:
        return rows
    else:
        return(rows[:length])

def high_scores_db_delete(db_connection):
    cursor_object = db_connection.cursor()
    cursor_object.execute('drop table if exists high_score_table')
    db_connection.commit()


def test():
    print('This is printout from high_scores test function! => import successful!')

#-----------------------------------------------------------------

if __name__ == '__main__':

    con = sql_connection()
    create_sql_table(con)

    now = datetime.now()
    time_stamp = int(datetime.timestamp(now))
    insert_sql_table(con, time_stamp, 'Dan', random.randint(1,200), now.date())
    time.sleep(1)

    now = datetime.now()
    time_stamp = int(datetime.timestamp(now))
    insert_sql_table(con, time_stamp, 'Dan', random.randint(1,200), now.date())

    #print_sql_table(con)

    top_5_list = get_top_5_list(con)
    print(top_5_list)

    #drop_sql_table(con)

    con.close()

    """ How to get the highest values:
    select * 
    from your_table
    where product_price = (SELECT max(product_price) FROM your_table)
    order by id desc
    limit 1
    """
