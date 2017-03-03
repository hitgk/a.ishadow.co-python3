
import warnings
warnings.filterwarnings("ignore")

from urllib.request import urlopen
from bs4 import BeautifulSoup


def main():
    """ 无输入参数，返回一个字符串 ，包含三个密码，以空格格式分隔开"""
    try:
        html = urlopen("http://a.ishadow.co/")
    except HTTPError as e:
        print(str(e))
    else:
        try:
            html = urlopen("http://a.ishadow.co/")
        except HTTPError as e:
            print(str(e))
    bsobj=BeautifulSoup(html)


    passwall=""
    print(bsobj.findAll('h4')[2])

    nameList = bsobj.findAll( "div",{"class":"col-sm-4 text-center"})[0:3]  #取有前三个密码的前四段
    for name in nameList:
        try:
            namesPassw=name.findAll('h4')[2].get_text()
            (names,passw)=namesPassw.split(":",1)
            print(passw)
            passwall +=(str(passw)+" ")
        except :
            #fayoujian shuo youbianhua
            pass
    return passwall
        #print(name.findAll('h4')[2].get_text())
 
if __name__=="__main__":
    main()
    print("\r\npress ENTER to exit()")
    input()
