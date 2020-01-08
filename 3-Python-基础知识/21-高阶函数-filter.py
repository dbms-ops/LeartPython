# -*-coding:utf-8-*-
#!/data1/Python2.7/bin/python2.7
#
# 高阶函数 filter(fn.lsd):
#   fn: 表示函数；
#   lsd：表示一个参数序列
#   用于过滤序列，将传入的函数作用于 lsd 序列的每个元素，根据返回的结果是 True 还是 False，决定是否保留该元素；;
# 

# 保留脚本中的偶数，并且删除里面的基数


def func(num):
    if num % 2 == 0:
        return True
    return False

def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    result = filter(func, list1)
    print result



if __name__ == '__main__':
    main()
    