# coding=utf-8
from tkinter.constants import END
import pyautogui as pg
import datetime  # 引入datetime模块
import time  # 引入time模块
from pyperclip import copy
from time import sleep
import tkinter
import threading


name = "张三"
tel = "13813881338"
campus = "渭水"
building = "1"
number = "1101"
waitingTime = 1.5  # 根据网络状况选择合适的等待时间 网络越差数值越大
Year = 2022
Month = 1
Day = 8
Hour = 12
Min = 0
ScheduledTime = datetime.datetime(Year, Month, Day, Hour, Min)  # 设置预定时间
flag = 1

root = tkinter.Tk()
root.title("长大1951商品限时抢购小程序")
root.geometry("800x450")

YearEntry = tkinter.Entry(root, width=5, textvariable=Year)
YearEntry.place(x=10, y=10)
YearEntry.insert(0, Year)
YearLabel = tkinter.Label(root, width=3, text="年")
YearLabel.place(x=50, y=10)
MonthEntry = tkinter.Entry(root, width=5, textvariable=Month)
MonthEntry.place(x=80, y=10)
MonthEntry.insert(0, Month)
MonthLabel = tkinter.Label(root, width=3, text="月")
MonthLabel.place(x=100, y=10)
DayEntry = tkinter.Entry(root, width=5, textvariable=Day)
DayEntry.place(x=130, y=10)
DayEntry.insert(0, Day)
DayLabel = tkinter.Label(root, width=3, text="日")
DayLabel.place(x=150, y=10)
HourEntry = tkinter.Entry(root, width=5, textvariable=Hour)
HourEntry.place(x=180, y=10)
HourEntry.insert(0, Hour)
HourLabel = tkinter.Label(root, width=3, text="时")
HourLabel.place(x=200, y=10)
MinEntry = tkinter.Entry(root, width=5, textvariable=Min)
MinEntry.place(x=230, y=10)
MinEntry.insert(0, Min)
MinLabel = tkinter.Label(root, width=3, text="分")
MinLabel.place(x=250, y=10)

NameEntry = tkinter.Entry(root, width=30, textvariable=name)
NameEntry.place(x=10, y=40)
NameEntry.insert(0, name)
NameLabel = tkinter.Label(root, width=15, text="姓名")
NameLabel.place(x=220, y=40)

TelEntry = tkinter.Entry(root, width=30, textvariable=tel)
TelEntry.place(x=10, y=70)
TelEntry.insert(0, tel)
TelLabel = tkinter.Label(root, width=15, text="电话号码")
TelLabel.place(x=220, y=70)

CampusEntry = tkinter.Entry(root, width=30, textvariable=campus)
CampusEntry.place(x=10, y=100)
CampusEntry.insert(0, campus)
CampusLabel = tkinter.Label(root, width=15, text="校区")
CampusLabel.place(x=220, y=100)

BuildingEntry = tkinter.Entry(root, width=30, textvariable=building)
BuildingEntry.place(x=10, y=130)
BuildingEntry.insert(0, building)
BuildingLabel = tkinter.Label(root, width=15, text="楼号")
BuildingLabel.place(x=220, y=130)

NumberEntry = tkinter.Entry(root, width=30, textvariable=number)
NumberEntry.place(x=10, y=160)
NumberEntry.insert(0, number)
NumberLabel = tkinter.Label(root, width=15, text="宿舍号")
NumberLabel.place(x=220, y=160)

WaitingTimeEntry = tkinter.Entry(root, width=30, textvariable=waitingTime)
WaitingTimeEntry.place(x=10, y=190)
WaitingTimeEntry.insert(0, waitingTime)
WaitingTimeLabel = tkinter.Label(root, width=15, text="加载等待时间")
WaitingTimeLabel.place(x=220, y=190)

OutputText = tkinter.Text(
    root, width=45, height=17, bg="grey")
# OutputLabel["text"] = OutputText
OutputText.place(x=350, y=10)
OutputText.insert(END, "这是输出信息框，程序运行时的输出信息将会输出到这里")


def ClearOutput():
    global OutputText
    OutputText.delete('1.0', 'end')


def PrintLog(log: str):
    print("完成!")
    OutputText.insert(END, "\n"+log)
    OutputText.see(END)


def PrintVar():
    global Year, Month, Day, Hour, Min, name, tel, campus, building, number, waitingTime
    PrintLog("读入参数:\nYear:{}\nMonth:{}\nDay:{}\nHour:{}\nMin:{}\nname:{}\ntel:{}\ncampus:{}\nbuilding:{}\nnumber:{}\nwaitingTime:{}\n".format(
        Year, Month, Day, Hour, Min, name, tel, campus, building, number, waitingTime))


def paste():
    pg.hotkey("ctrl", "v")


def PastTime() -> bool:
    global ScheduledTime
    rest = (ScheduledTime - datetime.datetime.now()).days
    print("PastTime Function:{}".format(ScheduledTime))
    print("PastTime Function Now:{}".format(datetime.datetime.now()))
    rest = ScheduledTime - datetime.datetime.now()
    rest=rest.days-304 # why this number? i don't know, maybe magic.
    print(rest)
    return rest < 0


def ResTime():
    global ScheduledTime
    return ScheduledTime - datetime.datetime.now()


def go():
    global waitingTime, name, tel, campus, building, number
    pg.click(x=1128, y=860)  # 点击结算
    sleep(waitingTime)  # 等待加载结算页面
    pg.click(x=926, y=310)  # 点击姓名
    copy(name)
    paste()  # 粘贴姓名
    pg.press("tab")
    copy(tel)
    paste()  # 粘贴电话号
    pg.press("tab")
    copy(campus)
    paste()  # 粘贴渭水
    pg.press("tab")
    copy(building)  # 输入楼号
    paste()
    pg.press("tab")
    copy(number)  # 输入宿舍号
    paste()
    pg.click(x=1115, y=941)  # 点击立即支付
    PrintLog("完成抢购!请微信扫码完成支付!")
    # PrintVar()
    # print(pg.position())


def check():
    global Year, Month, Day, Hour, Min, name, tel, campus, building, number, waitingTime
    try:
        Year = int(YearEntry.get())
        Month = int(MonthEntry.get())
        Day = int(DayEntry.get())
        Hour = int(HourEntry.get())
        Min = int(MinEntry.get())
        name = NameEntry.get()
        tel = TelEntry.get()
        campus = CampusEntry.get()
        building = BuildingEntry.get()
        number = NumberEntry.get()
        waitingTime = float(WaitingTimeEntry.get())
        PrintLog("读入参数:\nYear:{}\nMonth:{}\nDay:{}\nHour:{}\nMin:{}\nname:{}\ntel:{}\ncampus:{}\nbuilding:{}\nnumber:{}\nwaitingTime:{}\n".format(
            Year, Month, Day, Hour, Min, name, tel, campus, building, number, waitingTime))
        return False
    except ValueError:
        PrintLog("输入值有误")
        return True
    except:
        PrintLog("出错了，联系作者吧!")
        return True


def run():
    global ScheduledTime, flag
    flag = 1
    while not PastTime():
        if ResTime().seconds > 60:
            PrintLog("距离计时结束还有{:d}秒".format(ResTime().seconds))
            sleep(1)
        elif ResTime().seconds > 10:
            PrintLog("距离计时结束还有{:d}秒{:d}微秒".format(
                ResTime().seconds,  ResTime().microseconds))
            sleep(1)
        else:
            PrintLog("距离计时结束还有{:d}秒{:d}微秒".format(
                ResTime().seconds, ResTime().microseconds))
            sleep(0.05)  # sleep for 50 microsecond
        if flag == 0:
            PrintLog("触发停止")
            flag = 1
            raise SystemError
    go()


def main():
    tsk = []
    if check():
        return 1
    else:
        global ScheduledTime, Year, Month, Day, Hour, Min
        ScheduledTime = datetime.datetime(
            Year, Month, Day, Hour, Min)  # 设置预定时间
        tsk.append(threading.Thread(target=run))
        tsk[-1].start()


def stop():
    global flag
    flag = 0


WarningText = "注意:\n1:点击“开始抢购”按钮前，请先打开长大1951微信小程序，保持小程序的默认位置不要移动，将需要的物资放入购物袋并勾选，维持在购物车内等待结算的画面\n2:根据网络状况选择合适的等待时间,网络越差数值越大(默认为1)\n"

SubmitButton = tkinter.Button(
    root, width=25, height=3, text="开始抢购", command=main)
SubmitButton.place(x=10, y=250)
StopButton = tkinter.Button(root, width=10, text="停止", command=stop)
StopButton.place(x=250, y=250)
ClearOutputButton = tkinter.Button(
    root, width=10, text="清空输出", command=ClearOutput)
ClearOutputButton.place(x=250, y=290)

WarningMessage = tkinter.Message(root, width=750, text=WarningText)
WarningMessage.place(x=10, y=330)

if __name__ == '__main__':
    # main()
    # go()
    root.mainloop()
