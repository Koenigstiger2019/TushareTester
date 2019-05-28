import tushare as ts
import time


def function_tester1(score, token_dic, apifun_str_list, iternum):
    ts.set_token(token_dic[score])

    print(ts.__version__)
    pro = ts.pro_api()
    timecost_list = []
    iter_end_num_list = []
    exceptionstr_list = []
    for apifun_str in apifun_str_list:
        timecost, iter_end_num, exceptionstr = tsapitest_corefun(
            apifun_str, iternum, pro)
        timecost_list.append(timecost)
        iter_end_num_list.append(iter_end_num)
        exceptionstr_list.append(exceptionstr)

    return timecost_list, iter_end_num_list, exceptionstr_list


# @tsapitest_timer
def tsapitest_corefun(testargstr, iternum, pro):
    start_t = time.time()
    exceptionstr = "No Exception Report"
    iter_end_num = 0
    try:
        for iter_end_num in range(1, iternum + 1):
            eval(testargstr)
    except BaseException as e_base:
        end_t = time.time()
        exceptionstr = e_base.__str__()
        print(exceptionstr)
        time.sleep(60)
        timecost = end_t - start_t
        return timecost, iter_end_num, exceptionstr
    else:
        end_t = time.time()
        timecost = end_t - start_t
    print("time cost is", timecost)
    return timecost, iter_end_num, exceptionstr
