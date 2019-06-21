#!/bin/bash
#author: timor
#desc: 生成一个随机时间的at计划任务，执行博牛签到，这样它就会每天不固定时间签到

h=`expr $RANDOM % 24`
m=`expr $RANDOM % 60`

echo 'cd /opt/bobit;python run.py'|at $h:$m
atq
