# -*- coding: utf-8 -*-


from test_tool import *
from pandas.core.frame import DataFrame
import time


# 当前要用的积分帐户
score = "120"

# 帐户对应的token
token_dic = {
    "120": "09b6b39cf0b216c72a23f13cb5934345b35327744d11b6dc45b71aa7",
    "8120": "8afe6d9ab2accdaf14aac23e9a6b43e5c927cca0e778c4387e8535bb"}

# 各条api语句的重复测试次数
maxiternum = 201

# 将要测试的api语句放在list中
apifun_str_list = [
    "pro.daily( ts_code='600519.SH', start_date='20180701', end_date='20180702')",
    "pro.query('daily', ts_code='600519.SH', start_date='20180701', end_date='20180702')"
]

timecost_list, iter_end_num_list, exceptionstr_list = function_tester1(
    score, token_dic, apifun_str_list, maxiternum)
res_dict = {
    "被测语句": apifun_str_list,
    "迭代次数": iter_end_num_list,
    "迭代用时": timecost_list,
    "错误消息": exceptionstr_list}
res_df = DataFrame(res_dict)

csvfilename = "积分" + score + "_" + \
    time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.csv'

# 测试结果写入到 D://csvdata// 中
res_df.to_csv("D://csvdata//" + csvfilename)
