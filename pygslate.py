import re
import requests
from ctypes import c_int
import random
import urllib.parse
import json

'''
Copyright (c) 2023 Arthure Antony

Pygslate - Proof of Concept Disclaimer

This software, Pygslate, is a proof of concept project created for educational and research purposes. 
It is not intended for use in any unethical, illegal, or malicious activities. 
The author(s) of this software disclaim any responsibility for the misuse or unethical use of this code.

Intended Use:
Pygslate is intended to demonstrate concepts related to reverse engineering Google's browser-based translation. 
It is suitable for educational and research purposes only.

Limitations:
1. This software should not be used to engage in any activities that violate ethical standards or laws.
2. The author(s) do not endorse, support, or condone any unethical or illegal use of this software.
3. Users are solely responsible for their use of Pygslate and must adhere to applicable laws and ethical guidelines.

By using Pygslate, you agree to these terms and limitations. The author(s) disclaim any liability for any consequences resulting from the use or misuse of this software.

'''
class Translator:
    def __init__(self):
        self.session = requests.Session()

        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_4_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; CrOS x86_64 13904.41.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.167 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"]

        self.session.headers.update({
            'User-Agent': random.choice(self.user_agents)
        })

    def _someMoreBitWiseFunction(self, a):
        b = []
        d = 0
        while d < len(a):
            e = ord(a[d])
            if 128 > e:
                b.append(e)

            else:
                if 2048 > e:
                    b.append(e >> 6 | 192)

                else:
                    if (55296 == (e & 64512)) and d + 1 < len(a) and 56320 == (ord(a[d + 1]) & 64512):
                        d += 1
                        e = 65536 + ((e & 1023) << 10) + (ord(a[d]) & 1023)
                        b.append(e >> 18 | 240)
                        c += 1
                        b.append(e >> 12 & 63 | 128)

                    else:
                        b.append(e >> 12 | 224)

                        b.append(e >> 6 & 63 | 128)

                    b.append(e & 63 | 128)

            d += 1
        return b

    def _getCTTk(self):
        regex = "(c._ctkk=\'\d+.?\d+\';)"
        data = self.session.get(
            "https://translate.googleapis.com/translate_a/element.js")
        data = re.findall(regex, data.text)
        if data:
            tk = data[0].replace("c._ctkk='", '').replace("';", "")
        return tk

    def _someBitWiseFunction(self, a, b):
        c = 0
        while (c < len(b)-2):

            d = b[c+2]

            if "a" <= d:
                d = ord(d[0]) - 87
            else:
                d = int(d)

            if "+" == b[c+1]:
                d = a >> d
            else:
                d = a << d

            if "+" == b[c]:
                a = (a + d) & 4294967295
            else:
                a = a ^ d

            c += 3
        return c_int(a).value

    def _getTK(self, a):
        b = self._getCTTk().split('.')
        c = int(b[0]) | 0
        a = self._someMoreBitWiseFunction(a)
        d = c
        e = 0
        while (e < len(a)):
            d += a[e]
            d = self._someBitWiseFunction(d, "+-a^+6")
            e += 1
        d = self._someBitWiseFunction(d, "+-3^+b+-f")
        d ^= int(b[1]) | 0
        d = c_int(d).value
        if 0 > d:
            d = (d & 2147483647) + 2147483648
        b = d % 1E6
        b = int(b)
        return str(b) + '.' + str(b ^ c)

    def translate(self, text, sl='auto', tl='en'):
        tk = self._getTK("".join(text))
        url = f"https://translate.googleapis.com/translate_a/t?anno=3&client=te_lib&format=html&v=1.0&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&logld=vTE_20230926&sl={sl}&tl={tl}&tc=0&tk={tk}"
        data = {"q": text}
        res = self.session.post(url, data=data)
        if res.status_code == 200:
            data = json.loads(res.text)
            for i in range(len(data)):
                data[i] = urllib.parse.unquote(data[i])
                data[i] = re.sub(r'(<i>).*(<\/i>)+?', '', data[i])
                data[i] = data[i].replace("<b>", "").replace("</b>", "")
                data[i] = data[i].lstrip().rstrip()
            return data
        else:
            print("Something went wrong")
            return None
