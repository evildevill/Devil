# Tool : Wasii ( Facebook cloning tool)
# Author : Waseem Akram ( hackerwasii )
# github : https://github.com/evildevill
# Note : we are not responsible for any misuse
try:
    import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, mechanize, requests
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system('python2 wasi.py')

reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exit():
    print '[!] Exit'
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def wasii(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


banner = '\n\x1b[1;95mTool By Hacker wasii\n We are not responsible for any \nillegal activity\n \n'
def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r[\xe2\x9c\x94] Logging In ' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
id = []

def tlogin():
    os.system('clear')
    print banner
    username = raw_input('[\xf0\x9f\x94\x90] \x1b[1;94mTOOL USERNAME: ')
    if username == 'hacker':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL USERNAME: ' + username + ' (correct)'
    else:
        print '[!] Invalid Username.'
        time.sleep(1)
        tlogin()
    passw = raw_input('[\xf0\x9f\x94\x90]  \x1b[1;94mTOOL PASSWORD: ')
    if passw == 'wasii':
        os.system('clear')
        print banner
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL USERNAME: ' + username + ' (correct)'
        print '[\xe2\x9c\x93]  \x1b[1;91mTOOL PASSWORD: ' + passw + '  (correct)'
        time.sleep(2)
    else:
        print '[!] Invalid Password.'
        time.sleep(1)
        tlogin()
    try:
        toket = open('login.txt', 'r')
        os.system('python2 .wasii.py')
    except (KeyError, IOError):
        methodlogin()
    else:
        print '[!] Invalid Password'
        time.sleep(1)
        tlogin()


def methodlogin():
    os.system('clear')
    print banner
    print '[1] \x1b[1;93m Login With ID/Password.'
    print '[2]  \x1b[1;93mLogin Using Token.( No Identity Problem )'
    print '[3]  \x1b[1;93mExit.'
    print '      '
    hos = raw_input('\n \x1b[1;92mChoose Option >>  ')
    if hos == '':
        print '[!]  Wrong Input'
        exit()
    elif hos == '1':
        login()
    elif hos == '2':
        os.system('clear')
        print banner
        hosp = raw_input('[\xf0\x9f\x94\x91]  \x1b[1;91mGive Token : ')
        tik()
        hopa = open('login.txt', 'w')
        hopa.write(hosp)
        hopa.close()
        print '\n[\xe2\x9c\x93]  \x1b[1;91mLogged In Successfully.'
        time.sleep(1)
        os.system('xdg-open https://www.youtube.com/channel/HackerWasii')
        os.system('python2 .wasii.py')
    elif hos == '0':
        exit()
    else:
        print '[!] \x1b[1;91mWrong Input'
        exit()


def login():
    os.system('clear')
    try:
        tb = open('login.txt', 'r')
        os.system('python2 .wasii.py')
    except (KeyError, IOError):
        os.system('clear')
        print banner
        wasii('[\xf0\x9f\x94\x90] \x1b[1;96mLogin Your Facebook Account')
        wasii('[\xf0\x9f\x94\x90] \x1b[1;96mDonot Use Your Personal Account')
        wasii('[\xf0\x9f\x94\x90] \x1b[1;96mUse a New Facebook Account To Login')
        print '-------------------------------------'
        iid = raw_input('[+] Number/Email: ')
        id = iid.replace(' ', '')
        pwd = raw_input('[+] Password : ')
        tik()
        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + id + '&locale=en_US&password=' + pwd + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        z = json.load(data)
        if 'access_token' in z:
            st = open('login.txt', 'w')
            st.write(z['access_token'])
            st.close()
            print '\n[\xe2\x9c\x93] \x1b[1;91mLogged In Successfully.'
            time.sleep(1)
            os.system('xdg-open https://www.youtube.com/channe/HackerWasii')
            os.system('clear')
            os.system('python2 .wasii.py')
        elif 'www.facebook.com' in z['error_msg']:
            print '[!] \x1b[1;91mUser Must Verify Account Before Login.'
            time.sleep(3)
            login()
        else:
            print '[!]\x1b[1;91mNumber/User Id/ Password Is Wrong !'
            time.sleep(1)
            login()


if __name__ == '__main__':
    tlogin()