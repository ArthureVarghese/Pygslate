# Pygslate
Pygslate: A Python-based Google Translate reverse engineering project for Fast and Unlimited Translation (Proof of Concept).

---

### Pygslate - Proof of Concept Disclaimer

This software, Pygslate, is a proof of concept project created for educational and research purposes. It is not intended for use in any unethical, illegal, or malicious activities. The author(s) of this software disclaim any responsibility for the misuse or unethical use of this code.

**Intended Use:**
Pygslate is intended to demonstrate concepts related to reverse engineering Google's browser-based translation. It is suitable for educational and research purposes only.

**Limitations:**
1. This software should not be used to engage in any activities that violate ethical standards or laws.
2. The author(s) do not endorse, support, or condone any unethical or illegal use of this software.
3. Users are solely responsible for their use of Pygslate and must adhere to applicable laws and ethical guidelines.

By using Pygslate, you agree to these terms and limitations. The author(s) disclaim any liability for any consequences resulting from the use or misuse of this software.

##### I highly recommend using the [Official Google Translate API](https://cloud.google.com/translate/docs).

---

### Notes: 
* There is an issue with translation when source language is not English

        This is due to the encoding of characters 
        (might fix later.. but not sure since this is just a proof of concept)

* I tried to keep this relatively simple than all other implementations. Since i'm a learner, ignore my flaws!
---

## Useful Resources 

- [Telegram Google Translate Bypass by Dan Petrov](https://danpetrov.xyz/programming/2021/12/30/telegram-google-translate.html)
- [Google Translate API Hacking by David Vielhuber](https://vielhuber.de/en/blog/google-translation-api-hacking/)

---

## The Idea and Work-Around

Since most of the Google Translate implementations are based on web-based translations, bulk translations are limited along with rate limiting. This led me to think about how the Chrome browser implements webpage translations. Since a webpage might contain a lot of words, it offered a potential work-around for bulk translation along with no (probably... didn't happen in my tests) rate limiting.

A quick search on GitHub led me to [gpytranslate](https://github.com/DavideGalilei/gpytranslate). I found some useful resources (mentioned above) there. The blog and gists by [David Vielhuber](https://github.com/vielhuber) provided a very good idea about browser-based translation. The only problem was, it was dated to 2020. The URLs had changed, and the functions and parameters had changed.

So, starting from scratch, the first attempt was to generate the token (refer to the resources). Finding the right functions and parameters from the JavaScript file was not so hard (even though some functions and function names along with parameters had changed, the structure was somewhat similar to David Vielhuber's findings). Also, some required functions were not shown in the gists.

After finding and filtering out the necessary parts, it was time to convert it into Python. This was a bit of work since the functions were written in a way to obscure their meaning at a glance. Another problem was the 32-bit signed integers.
* The `int` type in Python is not limited to 32-bit signed integers by default. Python can automatically switch to arbitrary precision integers when needed.

* JavaScript, on the other hand, has strict rules for 32-bit integers.

So, when bitwise operations are performed, if the value exceeds the 32-bit range, JavaScript wraps around to negative values, but Python instead increases its precision to a higher bit. To tackle this, Python's `ctypes` was used.

After this, it was time to find the seed value. Luckily, Google hadn't changed the variable name (one of the inner functions was to generate the name of this variable) or the JavaScript file location (again, thanks to David Vielhuber). So, using `requests` and `re` to extract the value, the solution became whole.

Also, for the sake of avoiding rate limiting at any cost, I added 20 user-agents that are randomly selected for a session (thanks to [Dan Petrov](https://github.com/danirukun)'s Blog). Please don't ask why not a proxy...?

## Why Not the Existing Ones?

There are very few Python implementations of this. Among them, most are outdated and complex (one at a time rather than a list of items). Most of them don't support bulk translation and get rate-limited, etc.

---

# Usage

by specifying Source Language and Target Language

```
>>> from pygslate import Translator
>>> translator = Translator()
>>> translator.translate(['Hello World'],sl='en',tl='es')
['Hola Mundo']
>>> translator.translate(['This is','Easy bulk','translation'],sl='en',tl='es')
['Esto es', 'Fácil a granel', 'traducción']

```

---

## Thanks 

1. [David Vielhuber](https://github.com/vielhuber)
2. [Dan Petrov](https://github.com/danirukun)
3. [Davide Galilei](https://github.com/DavideGalilei)