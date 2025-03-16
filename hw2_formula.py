import pandas as pd

def dis_time(n):
    distance = 300-300/(2**n) # 总距离，解析式计算
    bounce = 100*(0.5**n) # 弹起高度，解析式计算
    time = ((200/9.8)**0.5)*(1+(2**0.5)*(1-0.5**(n/2))/(1-0.5**0.5)-0.5**(n/2)) # 总时间，解析式计算
    result = [distance, time, bounce] # 返回总距离，总时间，和弹起的高度
    return result

def main():
    while True:
        times = input("请输入弹地次数：")
        try:
            num = pd.to_numeric(times)  # 将输入转换为数值型
            if num % 1 == 0:  # 判断是否为整数
                if num > 0: # 判断是否是正整数
                    num = int(num) # 转化为整数型
                    result = dis_time(num) # 调用函数
                    # 输出结果，保留4位小数
                    print("第",num,"次掉下并反弹到最高点时，反弹高度为",round(result[2],4),"米","此时球一共经过",round(result[0],4),"米","运动时间为",round(result[1],4),"秒")
                    break # 检测到合法输入才停止
                else:
                    print("错误，检测到输入为非正整数：请输入一个有效的正整数")
            else:
                print("错误，检测到输入为小数：请输入一个正整数")
        except ValueError:  # 捕获非数字输入的错误
            print("错误，检测到输入为非数字：请输入一个有效的正整数")


if __name__ == "__main__":
    main()
