import pandas as pd

def dis_time(n):
    height = 100 # 初始高度
    distance = 0 # 初始总距离
    time = 0 # 初始总时间
    for i in range(n): # 循环计算
        distance = distance + height + height/2  # 总距离加上下落和反弹的高度，反弹的高度是落下高度的一半
        time = time + (2 * height/9.8)**0.5+(2 * (height/2)/9.8)**0.5 # 总时间加上下落和反弹的时间，反弹的高度是落下高度的一半
        height = height/2 # 重新设定初始高度，即为第i次弹起的高度
    result = [distance,time,height] # 返回总距离，总时间，和弹起的高度
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
