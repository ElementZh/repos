#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Element Zhang

# encoding: utf-8
import datetime
from dateutil.parser import parse
import datetime
import os
import MySQLdb
import csv
def this_thursday():
    thursday = datetime.date.today()
    delta = datetime.timedelta(days=1)
    thursday=thursday-delta
    return thursday
print(this_thursday())
this_thursday=this_thursday().strftime("%Y-%m-%d")
def last_friday():
    friday = datetime.date.today()
    sigma = datetime.timedelta(days=7)
    friday = friday - sigma
    return friday
print(last_friday())
print type(last_friday())
last_friday=last_friday().strftime("%Y-%m-%d")

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "00128955", "test", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
ss = this_thursday
print type(ss)
sql = "select * from dcp_api_gw_stat where DATE_FORMAT(call_date,'%Y-%m-%d')<="+"'"+ss+"'"
cursor.execute(sql)
#sql = "select * from dcp_api_gw_stat where DATE_FORMAT(start_time,'%Y-%m-%d') < '2022-02-16'"



cursor.execute(sql)
#sql = "SELECT * FROM dcp_api_gw_stat \
#       WHERE id = %s" % (id_ver)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      username = row[1]
      customer_no = row[2]
      request_id = row[3]
      success_num = row[4]
      fail_num = row[5]
      call_date = row[6]
      # Print result
      print "id=%s,username=%s,customer_no=%s,request_id=%s,success_num=%s,fail_num=%s,call_date=%s" % \
             (id, username, customer_no,  request_id,success_num,fail_num,call_date )
except:
   print "Error: unable to fecth data"

# 关闭数据库连接
db.close()




