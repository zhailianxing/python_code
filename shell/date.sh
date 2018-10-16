#! /bin/sh
# 功能： 获取指定日期的后几天。  博客地址:https://blog.csdn.net/SunnyYoona/article/details/51685280
# 
function nextDayOfDay()
{
    start=$1
    days=$2
    startDay=`date +'%Y%m%d' -d ${start}`
    echo "日期 -----> "${startDay}
    declare -i index  # 定义一个变量index,类型为int(i)
    index=0
    while [ ${index} -lt ${days} ]
        do
            date=`date -d "${startDay} ${index} days" +"%Y%m%d"`
            echo ${index}" ------> "${date}
            index=${index}+1
            done
}
nextDayOfDay $1 $2
