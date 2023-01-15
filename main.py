from bs4 import BeautifulSoup
import requests

def main():
    url = 'https://invoice.etax.nat.gov.tw/index.html' # 统一发票中奖号
    resp = requests.get(url)
    resp.encoding = 'utf-8' # 使用与网页相对应的编码格式, 避免乱码
    soup = BeautifulSoup(resp.text, 'html.parser') # 通过html dom解析器采集数据

    data = soup.select('.container-fluid .etw-tbiggest')
    prize_s = data[0].get_text().strip() # 特别奖, 使用strip()避免出现换行符\n
    prize_1 = data[1].get_text().strip() # 特奖
    prize_2 = [data[2].get_text().strip(), data[3].get_text().strip(), data[4].get_text().strip()] # 头奖

    while True: # 实现一直输入号码并对奖
        try:
            # 对奖程序
            number = input('请输入发票号码:')

            if number == prize_s: 
                print('对中 1,000 萬元')
            elif number == prize_1: 
                print('对中 200 萬元')

            for v in prize_2:
                if number == v:
                    print('对中 20 萬元')
                    break
                elif number[-7:] == v[-7:]: # 获取后面7位数字
                    print('对中 4 萬元')
                    break
                elif number[-6:] == v[-6:]:
                    print('对中 1 萬元')
                    break
                elif number[-5:] == v[-5:]:
                    print('对中 4 千元')
                    break
                elif number[-4:] == v[-4:]:
                    print('对中 1 千元')
                    break
                elif number[-3:] == v[-3:]:
                    print('对中 2 百元')
                    break
        except:
            break

if __name__ == '__main__': # 主入口
    main()