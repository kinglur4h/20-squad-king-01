# -*- coding: utf-8 -*-

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
from gtts import gTTS
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from googletrans import Translator
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, six, ast, pytz, urllib, urllib3, urllib.parse, traceback, atexit, subprocess

#ririn = LINE("TOKENMU")
kifli = LINE("EzEmnJS0d2zW9BBD9ERe.+r+jAIdxZWQoBO38ex8YVG.CRhGS9FuBLAJ+uxKPmnRmJKLTHcrjLHxoiidl1o87PA=")

kifliPoll = OEPoll(kifli)
KAC=[kifli] 
kifliMid = kifli.profile.mid
#aMid = dk1.profile.mid

responsename = kifli.getProfile().displayName
#responsename2 = dk1.getProfile().displayName
#responsename3 = dk2.getProfile().displayName

kifliProfile = kifli.getProfile()
#aProfile = dk1.getProfile()

kifliSettings = kifli.getSettings()
#aSettings = dk1.getSetting

botStart = time.time()

print ("╔═════════════════════════\n║╔════════════════════════\n║╠❂➣ DK BERHASIL LOGIN\n║╚════════════════════════\n╚═════════════════════════")

msg_dict = {}

wait = {
    "autoAdd": True,
    "autoJoin": True,
    "autoLeave": False,
    "autoRead": False,
    "autoRespon": True,
    "autoResponPc": False,
    "autoJoinTicket": True,
    "SpamInvite":True,
    "Timeline":False,
    "Invite":True,
    "autoBlock":True,
    "checkContact": False,
    "checkPost": False,
    "checkSticker": False,
    "changePictureProfile": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "leaveRoom": True,
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    },
    "Protectcancel": True,
    "Protectgr": True,
    "Protectinvite": True,
    "Protectjoin": False,
    "setKey": False,
    "sider": False,
    "unsendMessage": True
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

read = {
    "ROM": {},
    "readPoint": {},
    "readMember": {},
    "readTime": {}
}

list_language = {
    "list_textToSpeech": {
        "id": "Indonesia",
        "af" : "Afrikaans",
        "sq" : "Albanian",
        "ar" : "Arabic",
        "hy" : "Armenian",
        "bn" : "Bengali",
        "ca" : "Catalan",
        "zh" : "Chinese",
        "zh-cn" : "Chinese (Mandarin/China)",
        "zh-tw" : "Chinese (Mandarin/Taiwan)",
        "zh-yue" : "Chinese (Cantonese)",
        "hr" : "Croatian",
        "cs" : "Czech",
        "da" : "Danish",
        "nl" : "Dutch",
        "en" : "English",
        "en-au" : "English (Australia)",
        "en-uk" : "English (United Kingdom)",
        "en-us" : "English (United States)",
        "eo" : "Esperanto",
        "fi" : "Finnish",
        "fr" : "French",
        "de" : "German",
        "el" : "Greek",
        "hi" : "Hindi",
        "hu" : "Hungarian",
        "is" : "Icelandic",
        "id" : "Indonesian",
        "it" : "Italian",
        "ja" : "Japanese",
        "km" : "Khmer (Cambodian)",
        "ko" : "Korean",
        "la" : "Latin",
        "lv" : "Latvian",
        "mk" : "Macedonian",
        "no" : "Norwegian",
        "pl" : "Polish",
        "pt" : "Portuguese",
        "ro" : "Romanian",
        "ru" : "Russian",
        "sr" : "Serbian",
        "si" : "Sinhala",
        "sk" : "Slovak",
        "es" : "Spanish",
        "es-es" : "Spanish (Spain)",
        "es-us" : "Spanish (United States)",
        "sw" : "Swahili",
        "sv" : "Swedish",
        "ta" : "Tamil",
        "th" : "Thai",
        "tr" : "Turkish",
        "uk" : "Ukrainian",
        "vi" : "Vietnamese",
        "cy" : "Welsh"
    },
    "list_translate": {    
        "af": "afrikaans",
        "sq": "albanian",
        "am": "amharic",
        "ar": "arabic",
        "hy": "armenian",
        "az": "azerbaijani",
        "eu": "basque",
        "be": "belarusian",
        "bn": "bengali",
        "bs": "bosnian",
        "bg": "bulgarian",
        "ca": "catalan",
        "ceb": "cebuano",
        "ny": "chichewa",
        "zh-cn": "chinese (simplified)",
        "zh-tw": "chinese (traditional)",
        "co": "corsican",
        "hr": "croatian",
        "cs": "czech",
        "da": "danish",
        "nl": "dutch",
        "en": "english",
        "eo": "esperanto",
        "et": "estonian",
        "tl": "filipino",
        "fi": "finnish",
        "fr": "french",
        "fy": "frisian",
        "gl": "galician",
        "ka": "georgian",
        "de": "german",
        "el": "greek",
        "gu": "gujarati",
        "ht": "haitian creole",
        "ha": "hausa",
        "haw": "hawaiian",
        "iw": "hebrew",
        "hi": "hindi",
        "hmn": "hmong",
        "hu": "hungarian",
        "is": "icelandic",
        "ig": "igbo",
        "id": "indonesian",
        "ga": "irish",
        "it": "italian",
        "ja": "japanese",
        "jw": "javanese",
        "kn": "kannada",
        "kk": "kazakh",
        "km": "khmer",
        "ko": "korean",
        "ku": "kurdish (kurmanji)",
        "ky": "kyrgyz",
        "lo": "lao",
        "la": "latin",
        "lv": "latvian",
        "lt": "lithuanian",
        "lb": "luxembourgish",
        "mk": "macedonian",
        "mg": "malagasy",
        "ms": "malay",
        "ml": "malayalam",
        "mt": "maltese",
        "mi": "maori",
        "mr": "marathi",
        "mn": "mongolian",
        "my": "myanmar (burmese)",
        "ne": "nepali",
        "no": "norwegian",
        "ps": "pashto",
        "fa": "persian",
        "pl": "polish",
        "pt": "portuguese",
        "pa": "punjabi",
        "ro": "romanian",
        "ru": "russian",
        "sm": "samoan",
        "gd": "scots gaelic",
        "sr": "serbian",
        "st": "sesotho",
        "sn": "shona",
        "sd": "sindhi",
        "si": "sinhala",
        "sk": "slovak",
        "sl": "slovenian",
        "so": "somali",
        "es": "spanish",
        "su": "sundanese",
        "sw": "swahili",
        "sv": "swedish",
        "tg": "tajik",
        "ta": "tamil",
        "te": "telugu",
        "th": "thai",
        "tr": "turkish",
        "uk": "ukrainian",
        "ur": "urdu",
        "uz": "uzbek",
        "vi": "vietnamese",
        "cy": "welsh",
        "xh": "xhosa",
        "yi": "yiddish",
        "yo": "yoruba",
        "zu": "zulu",
        "fil": "Filipino",
        "he": "Hebrew"
    }
}

try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
wait["myProfile"]["displayName"] = kifliProfile.displayName
wait["myProfile"]["statusMessage"] = kifliProfile.statusMessage
wait["myProfile"]["pictureStatus"] = kifliProfile.pictureStatus
coverId = kifli.getProfileDetail()["result"]["objectId"]
wait["myProfile"]["coverId"] = coverId

def restartBot():
    print ("[ INFO ] BOT RESTART")
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
def logError(text):
    kifli.log("[ ERROR ] {}".format(str(text)))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = "{}, {} - {} - {} | {}".format(str(hasil), str(inihari.strftime('%d')), str(bln), str(inihari.strftime('%Y')), str(inihari.strftime('%H:%M:%S')))
    with open("logError.txt","a") as error:
        error.write("\n[ {} ] {}".format(str(time), text))

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                kifli.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]
            
def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@dee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    kifli.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if wait["setKey"] == True:
        if pesan.startswith(wait["keyCommand"]):
            cmd = pesan.replace(wait["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
    
def helpmessage():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpMessage =   "🔑" + key + " [Ⓓⓚ~ⒷⓄⓣ☯t]\n" + \
	                "🔑❂͜͡➣" + key + " 🅿🆄🅱🅻🅸🅲 ✪] " + "\n" + \
	                "🔑❂͜͡➣ " + key + "ʜᴇʟᴘ " + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴛᴛs " + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴛʀᴀɴsʟᴀᴛᴇ " + "\n" + \
	                "🔑❂͜͡➣ " + key + "═〚 ʙᴏᴛ 〛☢" + "\n" + \
	                "🔑❂͜͡➣ " + key + "Creator" + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴏᴡɴᴇʀ" + "\n" + \
	                "🔑❂͜͡➣ " + key + " ═〚 sᴇʟғ 〛☢" + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴍᴇ" + "\n" + \
	                "🔑❂͜͡➣ " + key + "Tagall" + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴍʏᴍɪᴅ" + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴍʏɴᴀᴍᴇ" + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴍʏʙɪᴏ" + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴍʏᴘɪᴄᴛᴜʀᴇ" + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴍʏᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ" + "\n" + \
	                "🔑❂͜͡➣ " + key + "ᴍʏᴄᴏᴠᴇʀ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "Dkbot" + "\n" + \
                    "🔰❂͜͡➣ " + key + "═〚 ɢʀᴏᴜᴘ ]" + "\n" + \
	                "🔰❂͜͡➣ " + key + "Harga" + "\n" + \
                    "🔰❂͜͡➣ " + key + "Promo" + "\n" + \
                    "🔰❂͜͡➣ " + key + "Kibar" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɢʀᴏᴜᴘɪᴅ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɢʀᴏᴜᴘɴᴀᴍᴇ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɢʀᴏᴜᴘᴍᴇᴍʙᴇʀʟɪsᴛ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɢʀᴏᴜᴘɪɴғᴏ" + "\n" + \
	                "👾❂͜͡➣ " + key + "  ═〚 sᴘᴇᴄɪᴀʟ 〛☢" + "\n" + \
	                "👾❂͜͡➣ " + key + "ʟᴜʀᴋɪɴɢ" + "\n" + \
	                "👾❂͜͡➣ " + key + "ʟᴜʀᴋɪɴɢ「ᴏɴ/ᴏғғ/ʀᴇsᴇᴛ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "═〚 ᴍᴇᴅɪᴀ 〛☢" + "\n" + \
	                "👮❂͜͡➣ " + key + "ᴄʜᴇᴄᴋʟᴏᴄᴀᴛɪᴏɴ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "ᴄʜᴇᴄᴋᴘʀᴀʏᴛɪᴍᴇ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "ᴄʜᴇᴄᴋᴡᴇᴀᴛʜᴇʀ「ʟᴏᴄᴀᴛɪᴏɴ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "ᴄʜᴇᴄᴋᴡᴇʙsɪᴛᴇ「ᴜʀʟ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "ɪɴsᴛᴀɪɴғᴏ 「ᴜsᴇʀɴᴀᴍᴇ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "sᴇᴀʀᴄʜɪᴍᴀɢᴇ 「sᴇᴀʀᴄʜ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "sᴇᴀʀᴄʜʟʏʀɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "sᴇᴀʀᴄʜᴍᴜsɪᴄ 「sᴇᴀʀᴄʜ」" + "\n" + \
	                "👮❂͜͡➣ " + key + "sᴇᴀʀᴄʜʏᴏᴜᴛᴜʙᴇ「sᴇᴀʀᴄʜ」" + "\n" + \
	                "👮❂͜͡➣ " + key + " [ADMIN]" + "\n" + \
	                "👮❂͜͡➣ " + key + "〚 ᴘʀᴏᴛᴇᴄᴛ 〛☢" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴘʀᴏᴄᴀɴᴄᴇʟ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴘʀᴏɢʀ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴘʀᴏɪɴᴠɪᴛᴇ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴘʀᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」" + "\n" + 	                "🔰❂͜͡➣ "  + key + "sᴘ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴘᴇᴇᴅ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴇᴛ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴀᴛᴜs" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴀʙꜱᴇɴ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴅk" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ʀᴇꜱᴘᴏɴ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴄʜᴇᴄᴋᴄᴏɴᴛᴀᴄᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴄʜᴇᴄᴋᴘᴏsᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴄʜᴇᴄᴋsᴛɪᴄᴋᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "═〚 ɢʀᴏᴜᴘ 〛☢" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ʙᴀɴ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴜɴʙᴀɴ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ʙᴀɴ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴜɴʙᴀɴ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ʙʟᴀᴄᴋʟɪsᴛ 「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ʙᴀɴʟɪsᴛ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴄᴇᴋʙᴀɴ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴄʟᴇᴀʀ ʙᴀɴ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴋɪʟʟ ʙᴀɴ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɴᴋ 「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴇᴀʟ 「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴄʜᴀɴɢᴇɢʀᴏᴜᴘᴘɪᴄᴛᴜʀᴇ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɢʀᴏᴜᴘᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɪɴᴠɪᴛᴇ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ɪɴᴠɪᴛᴇɢᴄ「ᴀᴍᴏᴜɴᴛ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "═〚 sᴘᴇᴄɪᴀʟ 〛☢" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴍɪᴍɪᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴍɪᴍɪᴄᴀᴅᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴍɪᴍɪᴄᴅᴇʟ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴍɪᴍɪᴄʟɪsᴛ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sɪᴅᴇʀ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴇᴀʟᴄᴏɴᴛᴀᴄᴛ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴇᴀʟᴍɪᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴇᴀʟɴᴀᴍᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴇᴀʟʙɪᴏ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴇᴀʟᴘɪᴄᴛᴜʀᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴇᴀʟᴠɪᴅᴇᴏᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴛᴇᴀʟᴄᴏᴠᴇʀ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + "ᴍʏᴋᴇʏ" + "\n" + \
	                "🔰❂͜͡➣ " + key + "sᴇᴛᴋᴇʏ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "🔰❂͜͡➣ " + key + " ✪ 🅾🆆🅽🅴🆁 ✪" + "\n" + \
	                "🔰═〚 ᴘʀᴏᴛᴇᴄᴛ 〛☢" + "\n" + \
	                "🔰❂➣ " + key + "sᴇᴛᴘʀᴏ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "🔰" + key + "═〚 ʙᴏᴛ 〛☢" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴅᴍɪɴᴀᴅᴅ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴅᴍɪɴᴅᴇʟ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ʙᴀᴄᴋᴜᴘᴘʀᴏғɪʟᴇ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ʙʏᴇ ᴀʟʟ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ʙʏᴇ ᴅɴᴀ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴄᴏᴍᴇ ᴅɴᴀ" +  "\n" + \
	                "😈❂͜͡➣ " + key + "ᴄʀᴀsʜ" +  "\n" + \
	                "😈❂͜͡➣ " + key + "ᴄʜᴀɴɢᴇʙɪᴏ:「ǫᴜᴇʀʏ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴄʜᴀɴɢᴇɴᴀᴍᴇ:「ǫᴜᴇʀʏ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴄʟᴏɴᴇᴘʀᴏғɪʟᴇ「ᴍᴇɴᴛɪᴏɴ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴄʜᴀɴɢᴇᴘɪᴄᴛᴜʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴇɴᴅᴄʜᴀᴛ" +  "\n" + \
	                "😈❂͜͡➣ " + key + "ɢʀᴏᴜᴘʟɪsᴛ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ʀᴇsᴛᴀʀᴛ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ʀᴇsᴛᴏʀᴇᴘʀᴏғɪʟᴇ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ʀᴜɴᴛɪᴍᴇ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴜᴛᴏᴀᴅᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴜᴛᴏᴊᴏɪɴᴛɪᴄᴋᴇᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴜᴛᴏʟᴇᴀᴠᴇ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴜᴛᴏʀᴇᴀᴅ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴀᴜᴛᴏʀᴇsᴘᴏɴᴘᴄ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴜɴsᴇɴᴅᴄʜᴀᴛ「ᴏɴ/ᴏғғ」" + "\n" + \
	                "═" + key + "〚 sᴇʀᴠᴇʀ ɪɴғᴏ 〛☢" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴄᴘᴜ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ɪғᴄᴏɴғɪɢ" + "\n" + \
	                "😈❂͜͡➣ " + key + "ᴋᴇʀɴᴇʟ" + "\n" + \
	                "😈❂͜͡➣ " + key + "sʏsᴛᴇᴍ" + "\n" + \
	                "😈════════╗" + "\n" + \
	                "                ᴄʀᴇᴅɪᴛs ʙʏ : ᴅ̶ᴇ̶ᴇ̶ ✯" + "\n" + \
	                "😈════════╝" + "\n" + \
	                "😈════════╗" + "\n" + \
	                "😈                   ✰ ᴅk ʙᴏᴛ  ✰" + "\n" + \
                    "😈════════╝"
    return helpMessage

def helptexttospeech():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTextToSpeech =  "╔════════════════════╗" + "\n" + \
                        "                    ✰ ᴅk ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "          ◄]·✪·ᴛᴇxᴛᴛᴏsᴘᴇᴇᴄʜ·✪·[►" + "\n" + \
                        "╠════════════════════╝ " + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜ : ᴄʜɪɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜʏᴜᴇ : ᴄʜɪɴᴇsᴇ (ᴄᴀɴᴛᴏɴᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴀᴜ : ᴇɴɢʟɪsʜ (ᴀᴜsᴛʀᴀʟɪᴀ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜᴋ : ᴇɴɢʟɪsʜ (ᴜᴋ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴᴜs : ᴇɴɢʟɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ (ᴄᴀᴍʙᴏᴅɪᴀɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴇs : sᴘᴀɴɪsʜ (sᴘᴀɪɴ)" + "\n" + \
                        "╠❂➣ " + key + "ᴇsᴜs : sᴘᴀɴɪsʜ (ᴜs)" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "               ᴄʀᴇᴅɪᴛs ʙʏ : Dzulkifli ✯" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "           ✰ ᴅK ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "sᴀʏ-ɪᴅ reza.p.i.p"
    return helpTextToSpeech

def helptranslate():
    if wait['setKey'] == True:
        key = wait['keyCommand']
    else:
        key = ''
    helpTranslate = "╔════════════════════╗" + "\n" + \
                        "                     ✰ ᴅK ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "             ◄]·✪·ᴛʀᴀɴsʟᴀᴛᴇ·✪·[►" + "\n" + \
                        "╠════════════════════╝" + "\n" + \
                        "╠❂➣ " + key + "ᴀғ : ᴀғʀɪᴋᴀᴀɴs" + "\n" + \
                        "╠❂➣ " + key + "sǫ : ᴀʟʙᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴍ : ᴀᴍʜᴀʀɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ᴀʀ : ᴀʀᴀʙɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ʜʏ : ᴀʀᴍᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴀᴢ : ᴀᴢᴇʀʙᴀɪᴊᴀɴɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴜ : ʙᴀsǫᴜᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʙᴇ : ʙᴇʟᴀʀᴜsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɴ : ʙᴇɴɢᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ʙs : ʙᴏsɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʙɢ : ʙᴜʟɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴇʙ : ᴄᴇʙᴜᴀɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɴʏ : ᴄʜɪᴄʜᴇᴡᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)" + "\n" + \
                        "╠❂➣ " + key + "ᴢʜᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)" + "\n" + \
                        "╠❂➣ " + key + "ᴄᴏ : ᴄᴏʀsɪᴄᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴄs : ᴄᴢᴇᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴀ : ᴅᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɴʟ : ᴅᴜᴛᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇɴ : ᴇɴɢʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ᴇᴛ : ᴇsᴛᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғɪ : ғɪɴɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʀ : ғʀᴇɴᴄʜ" + "\n" + \
                        "╠❂➣ " + key + "ғʏ : ғʀɪsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢʟ : ɢᴀʟɪᴄɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴀ : ɢᴇᴏʀɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴅᴇ : ɢᴇʀᴍᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴇʟ : ɢʀᴇᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴜ : ɢᴜᴊᴀʀᴀᴛɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴛ : ʜᴀɪᴛɪᴀɴ ᴄʀᴇᴏʟᴇ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀ : ʜᴀᴜsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴀᴡ : ʜᴀᴡᴀɪɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴡ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠❂➣ " + key + "ʜɪ : ʜɪɴᴅɪ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴍɴ : ʜᴍᴏɴɢ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "ɪɢ : ɪɢʙᴏ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴀ : ɪʀɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ɪᴛ : ɪᴛᴀʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴊᴡ : ᴊᴀᴠᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴋɴ : ᴋᴀɴɴᴀᴅᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴋ : ᴋᴀᴢᴀᴋʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴍ : ᴋʜᴍᴇʀ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴏ : ᴋᴏʀᴇᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴋᴜ : ᴋᴜʀᴅɪsʜ (ᴋᴜʀᴍᴀɴᴊɪ)" + "\n" + \
                        "╠❂➣ " + key + "ᴋʏ : ᴋʏʀɢʏᴢ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴏ : ʟᴀᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴀ : ʟᴀᴛɪɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴠ : ʟᴀᴛᴠɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟᴛ : ʟɪᴛʜᴜᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʟʙ : ʟᴜxᴇᴍʙᴏᴜʀɢɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɢ : ᴍᴀʟᴀɢᴀsʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍs : ᴍᴀʟᴀʏ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʟ : ᴍᴀʟᴀʏᴀʟᴀᴍ" + "\n" + \
                        "╠❂➣ " + key + "ᴍᴛ : ᴍᴀʟᴛᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɪ : ᴍᴀᴏʀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʀ : ᴍᴀʀᴀᴛʜɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴍɴ : ᴍᴏɴɢᴏʟɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴍʏ : ᴍʏᴀɴᴍᴀʀ (ʙᴜʀᴍᴇsᴇ)" + "\n" + \
                        "╠❂➣ " + key + "ɴᴇ : ɴᴇᴘᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘs : ᴘᴀsʜᴛᴏ" + "\n" + \
                        "╠❂➣ " + key + "ғᴀ : ᴘᴇʀsɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴘʟ : ᴘᴏʟɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴘᴀ : ᴘᴜɴᴊᴀʙɪ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ʀᴜ : ʀᴜssɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴍ : sᴀᴍᴏᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ɢᴅ : sᴄᴏᴛs ɢᴀᴇʟɪᴄ" + "\n" + \
                        "╠❂➣ " + key + "sʀ : sᴇʀʙɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴛ : sᴇsᴏᴛʜᴏ" + "\n" + \
                        "╠❂➣ " + key + "sɴ : sʜᴏɴᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴅ : sɪɴᴅʜɪ" + "\n" + \
                        "╠❂➣ " + key + "sɪ : sɪɴʜᴀʟᴀ" + "\n" + \
                        "╠❂➣ " + key + "sᴋ : sʟᴏᴠᴀᴋ" + "\n" + \
                        "╠❂➣ " + key + "sʟ : sʟᴏᴠᴇɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "sᴏ : sᴏᴍᴀʟɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴇs : sᴘᴀɴɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "sᴜ : sᴜɴᴅᴀɴᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "sᴡ : sᴡᴀʜɪʟɪ" + "\n" + \
                        "╠❂➣ " + key + "sᴠ : sᴡᴇᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛɢ : ᴛᴀᴊɪᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴀ : ᴛᴀᴍɪʟ" + "\n" + \
                        "╠❂➣ " + key + "ᴛᴇ : ᴛᴇʟᴜɢᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʜ : ᴛʜᴀɪ" + "\n" + \
                        "╠❂➣ " + key + "ᴛʀ : ᴛᴜʀᴋɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ" + "\n" + \
                        "╠❂➣ " + key + "ᴜʀ : ᴜʀᴅᴜ" + "\n" + \
                        "╠❂➣ " + key + "ᴜᴢ : ᴜᴢʙᴇᴋ" + "\n" + \
                        "╠❂➣ " + key + "ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ" + "\n" + \
                        "╠❂➣ " + key + "ᴄʏ : ᴡᴇʟsʜ" + "\n" + \
                        "╠❂➣ " + key + "xʜ : xʜᴏsᴀ" + "\n" + \
                        "╠❂➣ " + key + "ʏɪ : ʏɪᴅᴅɪsʜ" + "\n" + \
                        "╠❂➣ " + key + "ʏᴏ : ʏᴏʀᴜʙᴀ" + "\n" + \
                        "╠❂➣ " + key + "ᴢᴜ : ᴢᴜʟᴜ" + "\n" + \
                        "╠❂➣ " + key + "ғɪʟ : ғɪʟɪᴘɪɴᴏ" + "\n" + \
                        "╠❂➣ " + key + "ʜᴇ : ʜᴇʙʀᴇᴡ" + "\n" + \
                        "╠════════════════════╗" + "\n" + \
                        "              ᴄʀᴇᴅɪᴛs ʙʏ : ©ᴅ̶zulkifli✯" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "╔════════════════════╗" + "\n" + \
                        "   ✰ ᴅK ʙᴏᴛ ✰" + "\n" + \
                        "╚════════════════════╝" + "\n" + \
                        "ᴄᴏɴᴛᴏʜ : " + key + "ᴛʀ-ɪᴅ reza.p.i.p"
    return helpTranslate
    
def kifliBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] Succes")
            return

        if op.type == 5:
            print ("[ 5 ] Add Contact")
            if wait["autoAdd"] == True:
                kifli.findAndAddContactsByMid(op.param1)
            kifli.sendMessage(op.param1, "╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅɴᴀ ʙᴏᴛ ✰\n╚════════════════════╝\n       ʜᴀʟʟᴏ, ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅ ᴍᴇ\n\n                    ᴏᴘᴇɴ ᴏʀᴅᴇʀ :\n               ✪ sᴇʟғʙᴏᴛ ᴏɴʟʏ ✪\n            ✪ sᴇʟғʙᴏᴛ + ᴀssɪsᴛ ✪\n                ✪ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ✪\n              「ᴀʟʟ ʙᴏᴛ ᴘʏᴛʜᴏɴ з」\n\n         ᴍɪɴᴀᴛ ᴘᴄ ᴀᴋᴜɴ ᴅɪ ʙᴀᴡᴀʜ :\n        [line.me/ti/p/ppgIZ0JLDW]")

        if op.type == 13:
            print ("[ 13 ] Invite Into Group")
            if kifliMid in op.param3:
                if wait["autoJoin"] == True:
                    kifli.acceptGroupInvitation(op.param1)
                dan = kifli.getContact(op.param2)
                tgb = kifli.getGroup(op.param1)
                kifli.sendMessage(op.param1, "ʜᴀʟᴏ, ᴛʜx ғᴏʀ ɪɴᴠɪᴛᴇ ᴍᴇ")
                kifli.sendContact(op.param1, op.param2)
                kifli.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
                
        if op.type == 15:
        	dan = kifli.getContact(op.param2)
        	tgb = kifli.getGroup(op.param1)
        	kifli.sendMessage(op.param1, "Astaga Ad yg left 「{}」, Coba Di japri Kak {} Rujuk Dia lghy\nSmoga Balik\nN Jdi Teman Baik Ya\nAmin 😘😘😘".format(str(dan.displayName),str(tgb.name)))
        	kifli.sendContact(op.param1, op.param2)
        	kifli.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        	
        if op.type == 17:
        	dan = kifli.getContact(op.param2)
        	tgb = kifli.getGroup(op.param1)
        	sendMention(op.param1, "Hallo @!         ,\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ {} \nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴄʜᴇᴄᴋ ɴᴏᴛᴇ ʏᴀ \nSmoga Anda betah\nAmin 😘😘😘".format(str(tgb.name)),[op.param2])
        	kifli.sendContact(op.param1, op.param2)
        	kifli.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))

        if op.type == 22:
            if wait["leaveRoom"] == True:
                kifli.leaveRoom(op.param1)

        if op.type == 24:
            if wait["leaveRoom"] == True:
                kifli.leaveRoom(op.param1)


        if ["Timeline"] == False:
          if msg.contentType == 26:
              ret_ = "[ INFORMASI TIMELINE ]\n"
              if msg.contentMetadata["serviceType"] == "GB":
                  contact = kifli.getContact(user).displayName
                  auth = "\nPenulis : {}".format(str(contact.displayName))
              else:
                  auth = "\nPenulis : {}".format(str(msg.contentMetadata["serviceName"]))
                  ret_ += auth
              if "stickerId" in msg.contentMetadata:
                  stck = "\n Stiker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                  ret_ += stck
              if "mediaOid" in msg.contentMetadata:
                  object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                  if msg.contentMetadata["mediaType"] == "V":
                      if msg.contentMetadata["serviceType"] == "GB":
                          ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                          murl = "\n\nLink Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                      else:
                          ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                          murl = "\n\nLink Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                      ret_ += murl
                  else:
                      if msg.contentMetadata["serviceType"] == "GB":
                          ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                      else:
                          ourl = "\n\nLink Objek : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                  ret_ += ourl
              if "text" in msg.contentMetadata:
                  dia = kifli.getContact(user)
                  zx = ""
                  zxc = ""
                  zx2 = []
                  xpesan = 'Pengirim: '
                  ardian = str(dia.displayName)
                  pesan = ''
                  pesan2 = pesan+"@dzul1991ji\n"
                  xlen = str(len(zxc)+len(xpesan))
                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                  zx = {'S':xlen, 'E':xlen2, 'M':dia.mid}
                  zx2.append(zx)
                  kata = "\n\nText Type : {}".format(str(msg.contentMetadata["text"]))
                  purl = "\n\nLink Post : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                  ret_ += purl
                  ret_ += kata
                  zxc += pesan2
                  pesan = xpesan + zxc + ret_ + ""
                  kifli.sendMessage(kirim, pesan, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                  url = msg.contentMetadata["postEndUrl"]
                  kifli.likePost(url[25:58], url[66:], likeType=1001)

        if op.type == 26:
            try:
                print ("[ 26 ] SEND MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                setKey = wait["keyCommand"].title()
                if wait["setKey"] == False:
                    setKey = ''
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != ririn.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if msg.contentType == 0:
                        if text is None:
                            return
                        else:
                            cmd = command(text)
                            if cmd == "help":
                                helpMessage = helpmessage()
                                kifli.sendMessage(to, str(helpMessage))
                                #ririn.sendContact(to, "u0ed04a119f41615a8382c3b341b9720d")
                            elif cmd == "tts":
                                helpTextToSpeech = helptexttospeech()
                                kifli.sendMessage(to, str(helpTextToSpeech))
                                kifli.sendContact(to, "u0ed04a119f41615a8382c3b341b9720d")
                            elif cmd == "translate":
                                helpTranslate = helptranslate()
                                kifli.sendMessage(to, str(helpTranslate))
                                kifli.sendContact(to, "u0ed04a119f41615a8382c3b341b9720d")
                            elif cmd.startswith("changekey:"):
                                sep = text.split(" ")
                                key = text.replace(sep[0] + " ","")
                                if " " in key:
                                    kifli.sendMessage(to, "ᴅᴏɴ'ᴛ ᴛʏᴘᴏ ʙʀᴏ")
                                else:
                                    wait["keyCommand"] = str(key).lower()
                                    kifli.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴋᴇʏ [ {} ]".format(str(key).lower()))
                            elif cmd == "sp":
                            	kifli.sendMessage(to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                            	sp = int(round(time.time() *1000))
                            	kifli.sendMessage(to,"ᴍʏ sᴘᴇᴇᴅ : %sms" % (sp - op.createdTime))
                            elif cmd == "speed":
                            	start = time.time()
                            	kifli.sendMessage(to, "❂➣ ʟᴏᴀᴅɪɴɢ...")
                            	elapsed_time = time.time() - start
                            	kifli.sendMessage(to, "ᴍʏ sᴘᴇᴇᴅ : %sms" % (elapsed_time))
                            elif cmd == "runtime":
                                timeNow = time.time()
                                runtime = timeNow - botStart
                                runtime = format_timespan(runtime)
                                kifli.sendMessage(to, "ʀᴜɴɴɪɴɢ ɪɴ.. {}".format(str(runtime)))
                            elif cmd == "restart":
                                kifli.sendMessage(to, "ʙᴏᴛ ʜᴀᴠᴇ ʙᴇᴇɴ ʀᴇsᴛᴀʀᴛ")
                                restartBot()
                            elif cmd == "respon":
                            	kifli.sendMessage(to,responsename)
                            	random.choice(KAC).sendMessage(to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                            elif cmd == "absen":
                            	kifli.sendContact(to, kifliMid)
                            	random.choice(KAC).sendMessage(to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                            elif cmd == "dna":
                            	kifli.sendMessage(to,"ᴀʟʀᴇᴀᴅʏ ᴏɴ")
                            	random.choice(KAC).sendMessage(to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                            elif cmd == "kibar":
                            	kifli.sendMessage(to,"█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
 "ASSALAMUALAIKUM\n"
"  ╭━Ⓓ✒Ⓡ✒ⒼⓄ✒Ⓝ✒\n"
"  ╰╮┏━┳┳┓┏┳┳┓┏┳┳┳┓\n"
"  ┏┻╋━┻┻┫┣┻┻┫┣┻┻┻┫\n"
"  ┃HLO▪┃KMI DTANG LGI┃\n"
"  ┗ⓞⓞ┻┻ⓞ━━ⓞ┻┻ⓞ━╯\n"
"UNTUK MENGGUSUR\nROOM KALIAN\n"
"..  (҂`_´)\n"
   " <,︻╦̵̵̿╤━ ҉     ~  •"
"█۞███████]▄▄▄▄▃●●\n"
"▂▄▅█████████▅▄▃▂…"
"[████████████████]\n"
"◥⊙⊙▲⊙▲⊙▲⊙▲⊙▲⊙\n"
"╭━╮╭━╮\n"
"┃┃╰╯┃┃\n"
"┃╭╮╭╮┣┳━╮╭━━┳━━┳┳━╮\n"
"┃┃┃┃┃┣┫╭╮┫╭╮┃╭╮┣┫╭╯\n"
"┃┃┃┃┃┃┃┃┃┃╰╯┃╰╯┃┃┃\n"
"╰╯╰╯╰┻┻╯╰┻━╮┣━╮┣┻╯\n"
"╱╱╱╱╱╱╱╱╱╭━╯┣━╯┃\n"
"╱╱╱╱╱╱╱╱╱╰━━┻━━╯\n"
"👿━━━━━━━━━━━━━👿"
"Ⓣⓜⓟⓐ Ⓑⓐⓢⓐ_Ⓑⓐⓢⓘ\n"
"Ⓡⓐⓣⓐ ⓖⓐ ⓡⓐⓣⓐ\n" 
"Ⓨⓖ ⓟⓝⓣⓘⓝⓖ ⓚⓘⓑⓐⓡ\n"
"Ⓣⓐⓝⓖⓚⓘⓢ Ⓖⓞⓑⓛⓞⓚ\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗╔═╗╔══╗╔═╦═╗\n"
	"╚╗╔╝║╦╝║╔╗║║║║║║\n"
	"━║║━║╩╗║╠╣║║║║║║\n"
	"━╚╝━╚═╝╚╝╚╝╚╩═╩╝\n"
"👿━━━━━━━━━━━━━👿\n"
	"╔══╗         ╔╦╗\n"
	"╚╗╗║         ║╔╝\n"
	"╔╩╝║         ║╚╗\n"
	"╚══╝         ╚╩╝\n"
"👿━━━━━━━━━━━━━👿\n"        
"Ⓓⓡⓐⓖⓞⓝ_Ⓚⓘⓛⓛⓔⓡ\n"
"Ⓟⓤⓝⓨⓐ👿━━👿Ⓡⓐⓣⓐ Ⓝⓘ\n" 
"Ⓜⓐⓗ━👿━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
		"╔═╗╔══╗╔══╗╔══╗\n"
		"║╬║║╔╗║╚╗╔╝║╔╗║\n"
		"║╗╣║╠╣║━║║━║╠╣║\n"
		"╚╩╝╚╝╚╝━╚╝━╚╝╚╝\n"
		"━━━━━━━━━━━━━━━\n"
">>>Ⓑⓨⓔ_Ⓑⓨⓔ ⒼⒸ Ⓛⓐⓚⓝⓐⓣ>><\nⒹⓝⓓⓐⓜ Ⓒⓐⓡⓘ Ⓚⓜⓘ\n<<<<<<<<<>>\nhttp://line.me/ti/p/~reza.p.i.p\nhttp://line.me/ti/p/~reza.p.i.p")
                            	#random.choice(KAC).sendMessage(to,"ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇᴅ")
                            elif cmd == "harga":
                            	kifli.sendMessage(to,"╭══════════\n║⚫─[     DAFTAR HARGA     ]─⚫ \n║SELFBOT ONLY = 75K /BLN\n║2 ASSIST = 100K /BLN\n║5 ASSIST = 200K /BLN\n║10 ASSIST = 300K /BLN\n║\n║PROTECT ANTIJS\n║\n║2 BOT + ANTIJS = 150K /BLN\n║5 BOT + ANTIJS = 300K /BLN\n║10 BOT + ANTIJS = 500K /BLN\n║\n║═ই\═ANDA BERMINAT\n║ SILAHKAN ADD CONTACT \n║ DIBAWAH INI   \n║\n║http://line.me/ti/p/~reza.p.i.p\n║       TERIMA KASIH      \n║\n╰════════════")
                            	kifli.sendContact(to, mid)
                            elif cmd == "dkbot":
                            	kifli.sendMessage(to,"╚☆Ⓢⓘⓐⓟ☆╗\n╚Ⓚⓞⓜⓐⓝⓓⓝ╮╗")
                            elif cmd == "promo":
                            	kifli.sendMessage(to,"──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\nCat Bot\nPasang Vip smulle  n nmbahkan follower➣ꜱᴇʟꜰʙᴏᴛ + ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 2 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 3 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 4 ᴀꜱɪꜱᴛ\n➣1 ᴀᴋᴜɴ ᴜᴛᴀᴍᴀ + 5 ᴀꜱɪꜱᴛ\n➣ʙᴏᴛᴘʀᴏᴛᴇᴄᴛ 3-30 ʙᴏᴛ ᴀꜱɪꜱᴛ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ\n➣ʜʀɢᴀ ʙɪꜱᴀ ɴᴇɢᴏ\n─────────┅┅─────────\n  ✯❇͜͡❇͜͡C͜͡r͜͡e͜͡a͜͡t͜͡o͜͡r✯͜͡$͜͡ë͜͡I͜͡F͜͡-͜͡฿͜͜͡͡o͜͡t͜͡ ͜͡❇͜͡❇✯\nline.me/ti/p/~reza.p.i.p\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")
#buat cek token

                            elif cmd == "owner":
                                try:
                                	arr = []
                                	owner = "u0ed04a119f41615a8382c3b341b9720d"
                                	creator = kifli.getContact(owner)
                                	ret_ = "╔════════════════"
                                	ret_ += "\n╠✪➣  ✰ ᴅK ʙᴏᴛ ✰"
                                	ret_ += "\n╠══✪〘ᴏᴡɴᴇʀ ʟɪsᴛ〙✪═══"
                                	ret_ += "\n╠✪ ᴏᴡɴᴇʀʟɪsᴛ : : {}".format(creator.displayName)
                                	ret_ += "\n╠════════════════"
                                	ret_ += "\n╠✪〘 line.me/ti/p/~reza.p.i.p"
                                	ret_ += "\n╚════════════════"
                                	kifli.sendMessage(msg.to,"ᴡᴀɪᴛɪɴɢ ғᴏʀ ᴏᴡɴᴇʀʟɪsᴛ DK-BOT...")
                                	kifli.sendMessage(msg.to, str(ret_))
                                	kifli.sendContact(to, "u0ed04a119f41615a8382c3b341b9720d")
                                except Exception as e:
                                	kifli.sendMessage(msg.to, str(e))

                            elif msg.text in "kickall":
                               if msg.toType == 2:
                                  group = kifli.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  for x in nama:
                                         if x not in org["Friend"]:
                                             try:
                                                 kifli.kickoutFromGroup(msg.to,[x])
                                             except:
                                                 print ("imit")

                            elif cmd == "creator":
                                try:
                                	arr = []
                                	owner = "u0ed04a119f41615a8382c3b341b9720d"
                                	creator = kifli.getContact(owner)
                                	ret_ = "╔════════════════"
                                	ret_ += "\n╠✪➣  ✰ ᴅK ʙᴏᴛ ✰"
                                	ret_ += "\n╠══✪〘Creator〙✪═══"
                                	ret_ += "\n╠✪ Creatorʟɪsᴛ : : {}".format(creator.displayName)
                                	ret_ += "\n╠════════════════"
                                	ret_ += "\n╠✪〘 line.me/ti/p/~reza.p.i.p"
                                	ret_ += "\n╚════════════════"
                                	kifli.sendMessage(msg.to,"ᴡᴀɪᴛɪɴɢ Knalin Creator pelindung rom kami...")
                                	kifli.sendMessage(msg.to, str(ret_))
                                	kifli.sendContact(to, "u0ed04a119f41615a8382c3b341b9720d")
                                except Exception as e:
                                	kifli.sendMessage(msg.to, str(e))

#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "timeline on":
                                wait["autoAdd"] = True
                                kifli.sendMessage(to, "Check post\nset to done")
                            elif cmd == "timeline off":
                                wait["autoAdd"] = False
                                kifli.sendMessage(to, "Check post set to off\nDone")
                            elif cmd == "autoadd on":
                                wait["autoAdd"] = True
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ Di Aktifkan\nDone")
                            elif cmd == "autoadd off":
                                wait["autoAdd"] = False
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ᴀᴅᴅ di ᴏғғkan\nDone")
                            elif cmd == "autojoin on":
                                wait["autoJoin"] = True
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ᴊᴏɪɴ Di ᴏɴ kan\nDone")
                            elif cmd == "autojoin off":
                                wait["autoJoin"] = False
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ᴊᴏɪɴ ᴏɴ tlah di  ᴏғғ kan\nDone")
                            elif cmd == "autoleave on":
                                wait["autoLeave"] = True
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ di ᴏɴ kan\nDone")
                            elif cmd == "autoleave off":
                                wait["autoLeave"] = False
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ di ᴏғғ kan\nDone")
                            elif cmd == "autoresponpc on":
                                wait["autoResponPc"] = True
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ғᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴀᴛ ᴏɴ")
                            elif cmd == "autoresponpc off":
                                wait["autoResponPc"] = False
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ғᴏʀ ᴘᴇʀsᴏɴᴀʟ ᴄʜᴀᴛ ᴏғғ")
                            elif cmd == "autorespon on":
                                wait["autoRespon"] = True
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ Di ᴏɴ kan\nDone")
                            elif cmd == "autorespon off":
                                wait["autoRespon"] = False
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ Telah di ᴏғғ kan\nDone")
                            elif cmd == "autoread on":
                                wait["autoRead"] = True
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ Di ᴏɴ kan\nDone ")
                            elif cmd == "autoread off":
                                wait["autoRead"] = False
                                kifli.sendMessage(to, "ᴀᴜᴛᴏ ʀᴇᴀᴅ Telah di ᴏғғ kan\nDone")
                            elif cmd == "autojointicket on":
                                wait["autoJoinTicket"] = True
                                kifli.sendMessage(to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏɴ\nOk My Bos")
                            elif cmd == "autoJoinTicket off":
                                wait["autoJoin"] = False
                                kifli.sendMessage(to, "ᴊᴏɪɴ ʙʏ ᴛɪᴄᴋᴇᴛ ᴏғғ\nOk My Bos")
                            elif cmd == "contact on":
                                wait["checkContact"] = True
                                kifli.sendMessage(to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏɴ\nOk My Bos")
                            elif cmd == "contact off":
                                wait["checkContact"] = False
                                kifli.sendMessage(to, "ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ ᴏғғ\nOk My Bos")
                            elif cmd == "checkpost on":
                                wait["checkPost"] = True
                                kifli.sendMessage(to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏɴ\nDone")
                            elif cmd == "checkpost off":
                                wait["checkPost"] = False
                                kifli.sendMessage(to, "ᴄʜᴇᴄᴋ ᴘᴏsᴛ ᴏғғ\nDone")
                            elif cmd == "checksticker on":
                                wait["checkSticker"] = True
                                kifli.sendMessage(to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏɴ\nDone")
                            elif cmd == "checksticker off":
                                wait["checkSticker"] = False
                                kifli.sendMessage(to, "ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ ᴏғғ\nDone")
                            elif cmd == "unsendchat on":
                                wait["unsendMessage"] = True
                                kifli.sendMessage(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏɴ\nJelas On My Bos")
                            elif cmd == "unsendchat off":
                                wait["unsendMessage"] = False
                                kifli.sendMessage(to, "ᴜɴsᴇɴᴅ ᴍᴇssᴀɢᴇ ᴏғғ")
                            elif cmd == "status":
                                try:
                                    ret_ = "╔═════[ ·✪·sᴛᴀᴛᴜs·✪· ]═════╗"
                                    if wait["autoAdd"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴀᴅᴅ 「⚫」"
                                    if wait["autoJoin"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ᴊᴏɪɴ 「⚫」"
                                    if wait["autoLeave"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʟᴇᴀᴠᴇ 「⚫」"
                                    if wait["autoJoinTicket"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴊᴏɪɴ ᴛɪᴄᴋᴇᴛ 「⚫」"
                                    if wait["autoRead"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇᴀᴅ 「⚫」"
                                    if wait["autoRespon"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ 「⚫」"
                                    if wait["autoResponPc"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴀᴜᴛᴏ ʀᴇsᴘᴏɴ ᴘᴄ 「⚫」"
                                    if wait["checkContact"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴄᴏɴᴛᴀᴄᴛ 「⚫」"
                                    if wait["Timeline"] == False: ret_ += "\n╠❂➣  [ ᴏɴ ]  Check Post Timeline 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ]  Check Post 「⚫」"
                                    if wait["checkPost"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ ᴘᴏsᴛ 「⚫」"
                                    if wait["checkSticker"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴄʜᴇᴄᴋ sᴛɪᴄᴋᴇʀ 「⚫」"
                                    if wait["setKey"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] sᴇᴛ ᴋᴇʏ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] sᴇᴛ ᴋᴇʏ 「⚫」"
                                    if wait["unsendMessage"] == True: ret_ += "\n╠❂➣ [ ᴏɴ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚪」"
                                    else: ret_ += "\n╠❂➣ [ ᴏғғ ] ᴜɴsᴇɴᴅ ᴍsɢ 「⚫」"
                                    ret_ += "\n╚═════[ ✯ ᴅk ʙᴏᴛ ✯ ]═════╝"
                                    kifli.sendMessage(to, str(ret_))
                                    kifli.sendContact(to, "u0ed04a119f41615a8382c3b341b9720d")
                                except Exception as e:
                                    kifli.sendMessage(msg.to, str(e))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "crash":
                                kifli.sendContact(to, "u0ed04a119f41615a8382c3b341b9720d',")
                            elif cmd.startswith("changename:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 20:
                                    profile = kifli.getProfile()
                                    profile.displayName = string
                                    kifli.updateProfile(profile)
                                    kifli.sendMessage(to,"ᴄʜᴀɴɢᴇ ɴᴀᴍᴇ sᴜᴄᴄᴇs :{}".format(str(string)))
                            elif cmd.startswith("changebio:"):
                                sep = text.split(" ")
                                string = text.replace(sep[0] + " ","")
                                if len(string) <= 500:
                                    profile = kifli.getProfile()
                                    profile.statusMessage = string
                                    kifli.updateProfile(profile)
                                    kifli.sendMessage(to,"ᴄʜᴀɴɢᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs :{}".format(str(string)))
                            elif cmd == "me":
                                kifli.sendContact(to, sender)
                            elif cmd == "mymid":
                                kifli.sendMessage(to, "[ ᴍɪᴅ ]\n{}".format(sender))
                            elif cmd == "myname":
                                contact = kifli.getContact(sender)
                                kifli.sendMessage(to, "[ ᴅɪsᴘʟᴀʏ ɴᴀᴍᴇ ]\n{}".format(contact.displayName))
                            elif cmd == "mybio":
                                contact = kifli.getContact(sender)
                                ririn.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(contact.statusMessage))
                            elif cmd == "mypicture":
                                contact = kifli.getContact(sender)
                                ririn.sendImageWithURL(to,"http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            elif cmd == "myvideoprofile":
                                contact = kifli.getContact(sender)
                                kifli.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/{}/vp".format(contact.pictureStatus))
                            elif cmd == "mycover":
                                channel = kifli.getProfileCoverURL(sender)          
                                path = str(channel)
                                kifli.sendImageWithURL(to, path)
                            elif cmd.startswith ('invitegc '):
                            	if msg.toType == 2:
                                    sep = text.split(" ")
                                    strnum = text.replace(sep[0] + " ","")
                                    num = int(strnum)
                                    kifli.sendMessage(to, "sᴜᴄᴄᴇs ɪɴᴠɪᴛᴇ ɢʀᴏᴜᴘ ᴄᴀʟʟ")
                                    for var in range(0,num):
                                        group = kifli.getGroup(to)
                                        members = [mem.mid for mem in group.members]
                                        kifli.inviteIntoGroupCall(to, contactIds=members)
                            elif cmd.startswith("cloneprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = kifli.getContact(ls)
                                        kifli.cloneContactProfile(ls)
                                        kifli.sendMessage(to, "ᴄʟᴏɴᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs : {}".format(contact.displayName))
                            elif cmd == "restoreprofile":
                                try:
                                    kifliProfile = ririn.getProfile()
                                    kifliProfile.displayName = str(wait["myProfile"]["displayName"])
                                    kifliProfile.statusMessage = str(wait["myProfile"]["statusMessage"])
                                    kifliProfile.pictureStatus = str(wait["myProfile"]["pictureStatus"])
                                    kifli.updateProfileAttribute(8, ririnProfile.pictureStatus)
                                    kifli.updateProfile(ririnProfile)
                                    coverId = str(wait["myProfile"]["coverId"])
                                    kifli.updateProfileCoverById(coverId)
                                    kifli.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs, ᴡᴀɪᴛ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇs")
                                except Exception as e:
                                    kifli.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")
                                    logError(error)
                            elif cmd == "backupprofile":
                                try:
                                    profile = kifli.getProfile()
                                    wait["myProfile"]["displayName"] = str(profile.displayName)
                                    wait["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                    wait["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                    coverId = kifli.getProfileDetail()["result"]["objectId"]
                                    wait["myProfile"]["coverId"] = str(coverId)
                                    kifli.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs")
                                except Exception as e:
                                    kifli.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")
                                    logError(error)
                            elif cmd.startswith("stealmid "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    ret_ = "[ Mid User ]"
                                    for ls in lists:
                                        ret_ += "\n{}".format(str(ls))
                                    kifli.sendMessage(to, str(ret_))
                            elif cmd.startswith("stealname "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = kifli.getContact(ls)
                                        kifli.sendMessage(to, "[ Display Name ]\n{}".format(str(contact.displayName)))
                            elif cmd.startswith("stealbio "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = kifli.getContact(ls)
                                        kifli.sendMessage(to, "[ sᴛᴀᴛᴜs ᴍᴇssᴀɢᴇ ]\n{}".format(str(contact.statusMessage)))
                            elif cmd.startswith("stealpicture"):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = kifli.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}".format(contact.pictureStatus)
                                        kifli.sendImageWithURL(to, str(path))
                            elif cmd.startswith("stealvideoprofile "):
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    lists = []
                                    for mention in mentionees:
                                        if mention["M"] not in lists:
                                            lists.append(mention["M"])
                                    for ls in lists:
                                        contact = kifli.getContact(ls)
                                        path = "http://dl.profile.line.naver.jp/{}/vp".format(contact.pictureStatus)
                                        kifli.sendVideoWithURL(to, str(path))
                            elif cmd.startswith("stealcover "):
                                if kifli != None:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            channel = kifli.getProfileCoverURL(ls)
                                            path = str(channel)
                                            kifli.sendImageWithURL(to, str(path))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == 'groupcreator':
                                group = kifli.getGroup(to)
                                GS = group.creator.mid
                                ririn.sendContact(to, GS)
                            elif cmd == 'groupid':
                                gid = kifli.getGroup(to)
                                kifli.sendMessage(to, "[ɢʀᴏᴜᴘ ɪᴅ : : ]\n" + gid.id)
                            elif cmd == 'grouppicture':
                                group = kifli.getGroup(to)
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                kifli.sendImageWithURL(to, path)
                            elif cmd == 'groupname':
                                gid = kifli.getGroup(to)
                                kifli.sendMessage(to, "[ɢʀᴏᴜᴘ ɴᴀᴍᴇ : ]\n" + gid.name)
                            elif cmd == 'groupticket':
                                if msg.toType == 2:
                                    group = kifli.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        ticket = kifli.reissueGroupTicket(to)
                                        kifli.sendMessage(to, "[ ɢʀᴏᴜᴘ ᴛɪᴄᴋᴇᴛ ]\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                                    else:
                                        kifli.sendMessage(to, "ᴛʜᴇ ǫʀ ɢʀᴏᴜᴘ ɪs ɴᴏᴛ ᴏᴘᴇɴ ᴘʟᴇᴀsᴇ ᴏᴘᴇɴ ɪᴛ ғɪʀsᴛ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ {}openqr".format(str(wait["keyCommand"])))
                            elif cmd == 'groupticket on':
                                if msg.toType == 2:
                                    group = kifli.getGroup(to)
                                    if group.preventedJoinByTicket == False:
                                        kifli.sendMessage(to, "ᴀʟʀᴇᴀᴅʏ ᴏᴘᴇɴ")
                                    else:
                                        group.preventedJoinByTicket = False
                                        kifli.updateGroup(group)
                                        kifli.sendMessage(to, "sᴜᴄᴄᴇs ᴏᴘᴇɴ ǫʀ ɢʀᴏᴜᴘ")
                            elif cmd == 'groupticket off':
                                if msg.toType == 2:
                                    group = kifli.getGroup(to)
                                    if group.preventedJoinByTicket == True:
                                        kifli.sendMessage(to, "ᴀʟʀᴇᴀᴅʏ ᴄʟᴏsᴇᴅ")
                                    else:
                                        group.preventedJoinByTicket = True
                                        kifli.updateGroup(group)
                                        kifli.sendMessage(to, "sᴜᴄᴄᴇs ᴄʟᴏsᴇ ǫʀ ɢʀᴏᴜᴘ")
                            elif cmd == 'groupinfo':
                                group = kifli.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "ɴᴏᴛ ғᴏᴜɴᴅ"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "ᴄʟᴏsᴇᴅ"
                                    gTicket = "ɴᴏʟ'"
                                else:
                                    gQr = "ᴏᴘᴇɴ"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(ririn.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╔════[ ·✪ɢʀᴏᴜᴘ ɪɴғᴏ✪· ]════╗"
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɴᴀᴍᴇ : {}".format(str(group.name))
                                ret_ += "\n╠❂➣ ɢʀᴏᴜᴘ ɪᴅ : {}".format(group.id)
                                ret_ += "\n╠❂➣ ᴄʀᴇᴀᴛᴏʀ :  {}".format(str(gCreator))
                                ret_ += "\n╠❂➣ ᴍᴇᴍʙᴇʀ : {}".format(str(len(group.members)))
                                ret_ += "\n╠❂➣ ᴘᴇɴᴅɪɴɢ : {}".format(gPending)
                                ret_ += "\n╠❂➣ ǫʀ ɢʀᴏᴜᴘ : {}".format(gQr)
                                ret_ += "\n╠❂➣ ᴛɪᴄᴋᴇᴛ ɢʀᴏᴜᴘ : {}".format(gTicket)
                                ret_ += "\n╚═════[ ✯ ᴅk ʙᴏᴛ ✯ ]═════╝"
                                kifli.sendMessage(to, str(ret_))
                                kifli.sendImageWithURL(to, path)
                            elif cmd == 'memberlist':
                                if msg.toType == 2:
                                    group = kifli.getGroup(to)
                                    ret_ = "╔══[ ᴍᴇᴍʙᴇʀ  ʟɪsᴛ ]══✪"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n╠❂➣ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(group.members)))
                                    kifli.sendMessage(to, str(ret_))
                            elif cmd == 'grouplist':
                                    groups = kifli.groups
                                    ret_ = "╔═[ ✯ ɢʀᴏᴜᴘ  ʟɪsᴛ ✯ ]═✪"
                                    no = 0 + 1
                                    for gid in groups:
                                        group = kifli.getGroup(gid)
                                        ret_ += "\n╠❂➣ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                                        no += 1
                                    ret_ += "\n╚═══[ ᴛᴏᴛᴀʟ : {} ]═══✪".format(str(len(groups)))
                                    kifli.sendMessage(to, str(ret_))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅɴᴀ ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd == "changepictureprofile":
                                wait["changePictureProfile"] = True
                                kifli.sendMessage(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                            elif cmd == "changegrouppicture":
                                if msg.toType == 2:
                                    if to not in wait["changeGroupPicture"]:
                                        wait["changeGroupPicture"].append(to)
                                    kifli.sendMessage(to, "sᴇɴᴅ ᴘɪᴄᴛᴜʀᴇ")
                            elif cmd == 'tagall':
                                group = kifli.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Zero \n'
                                    kifli.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                                    kifli.sendMessage(to, "Total {} Mention".format(str(len(nama))))
                            elif"Cekpm @" in msg.text:
                                _name = msg.text.replace("Cek pm @","")
                                _nametarget = _name.rstrip(' ')
                                gs = kifli.getGroup(msg.to)
                                for g in gs.members:
                                    if _nametarget == g.displayName:
                                       kifli.sendText(msg.to,"ᴋᴜɴᴊᴜɴɢɪ ʟɪɴᴋ ᴋᴀᴍɪ ʜᴛᴛᴘ://sᴘᴀᴍ.ᴄᴏᴍ/ʀᴇʏᴘʀᴏ 😂")
                                    
                            elif cmd == "sider on":
                            	try:
                            		del cctv['point'][msg.to]
                            		del cctv['sidermem'][msg.to]
                            		del cctv['cyduk'][msg.to]
                            	except:
                            		pass
                            	cctv['point'][msg.to] = msg.id
                            	cctv['sidermem'][msg.to] = ""
                            	cctv['cyduk'][msg.to]=True
                            	wait["Sider"] = True
                            	kifli.sendMessage(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏɴ")
                            elif cmd == "sider off":
                            	if msg.to in cctv['point']:
                            		cctv['cyduk'][msg.to]=False
                            		wait["Sider"] = False
                            		kifli.sendMessage(msg.to,"sɪᴅᴇʀ sᴇᴛ ᴛᴏ ᴏғғ")
                            	else:
                            		kifli.sendMessage(msg.to,"sɪᴅᴇʀ ɴᴏᴛ sᴇᴛ")           
                            elif cmd == "lurking on":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    kifli.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏɴ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    kifli.sendMessage(receiver,"sᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
                            elif cmd == "lurking off":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver not in read['readPoint']:
                                    kifli.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ sᴇᴛ ᴏғғ")
                                else:
                                    try:
                                        del read['readPoint'][receiver]
                                        del read['readMember'][receiver]
                                        del read['readTime'][receiver]
                                    except:
                                        pass
                                    kifli.sendMessage(receiver,"ᴅᴇʟᴇᴛᴇ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
        
                            elif cmd == "lurking reset":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if msg.to in read["readPoint"]:
                                    try:
                                        del read["readPoint"][msg.to]
                                        del read["readMember"][msg.to]
                                        del read["readTime"][msg.to]
                                        del read["ROM"][msg.to]
                                    except:
                                        pass
                                    read['readPoint'][receiver] = msg_id
                                    read['readMember'][receiver] = ""
                                    read['readTime'][receiver] = readTime
                                    read['ROM'][receiver] = {}
                                    kifli.sendMessage(msg.to, "ʀᴇsᴇᴛ ʀᴇᴀᴅɪɴɢ ᴘᴏɪɴᴛ : \n" + readTime)
                                else:
                                    kifli.sendMessage(msg.to, "ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴋᴛɪᴠᴇ, ᴄᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ʀᴇsᴇᴛ")
                                    
                            elif cmd == "lurking":
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                                hr = timeNow.strftime("%A")
                                bln = timeNow.strftime("%m")
                                for i in range(len(day)):
                                    if hr == day[i]: hasil = hari[i]
                                for k in range(0, len(bulan)):
                                    if bln == str(k): bln = bulan[k-1]
                                readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                                if receiver in read['readPoint']:
                                    if read["ROM"][receiver].items() == []:
                                        kifli.sendMessage(receiver,"ɴᴏ sɪᴅᴇʀ")
                                    else:
                                        chiya = []
                                        for rom in read["ROM"][receiver].items():
                                            chiya.append(rom[1])
                                        cmem = kifli.getContacts(chiya) 
                                        zx = ""
                                        zxc = ""
                                        zx2 = []
                                        xpesan = '[ ʀ ᴇ ᴀ ᴅ ᴇ ʀ ]\n'
                                    for x in range(len(cmem)):
                                        xname = str(cmem[x].displayName)
                                        pesan = ''
                                        pesan2 = pesan+"@c\n"
                                        xlen = str(len(zxc)+len(xpesan))
                                        xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                        zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                        zx2.append(zx)
                                        zxc += pesan2
                                    text = xpesan+ zxc + "\n" + readTime
                                    try:
                                        kifli.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                    except Exception as error:
                                        print (error)
                                    pass
                                else:
                                    kifli.sendMessage(receiver,"ʟᴜʀᴋɪɴɢ ɴᴏᴛ ᴀᴄᴛɪᴠᴇ")
                            elif cmd.startswith("mimicadd"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        wait["mimic"]["target"][target] = True
                                        kifli.sendMessage(msg.to,"ᴛᴀʀɢᴇᴛ ᴀᴅᴅᴇᴅ")
                                        break
                                    except:
                                        kifli.sendMessage(msg.to,"ғᴀɪʟᴇᴅ ᴀᴅᴅᴇᴅ ᴛᴀʀɢᴇᴛ")
                                        break
                            elif cmd.startswith("mimicdel"):
                                targets = []
                                key = eval(msg.contentMetadata["MENTION"])
                                key["MENTIONEES"][0]["M"]
                                for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                                for target in targets:
                                    try:
                                        del wait["mimic"]["target"][target]
                                        kifli.sendMessage(msg.to,"ᴛᴀɢᴇᴛ ᴅᴇʟᴇᴛᴇᴅ")
                                        break
                                    except:
                                        kifli.sendMessage(msg.to,"ғᴀɪʟ ᴅᴇʟᴇᴛᴇᴅ ᴛᴀʀɢᴇᴛ")
                                        break
                                    
                            elif cmd == "mimiclist":
                                if wait["mimic"]["target"] == {}:
                                    kifli.sendMessage(msg.to,"ɴᴏ ᴛᴀʀɢᴇᴛ")
                                else:
                                    mc = "╔════[ ·✪·ᴍɪᴍɪᴄ ʟɪsᴛ·✪· ]════╗"
                                    for mi_d in wait["mimic"]["target"]:
                                        mc += "\n╠❂➣ "+kifli.getContact(mi_d).displayName
                                    mc += "\n╚═════[  ✯ ᴅk ʙᴏᴛ ✯ ]═════╝"
                                    kifli.sendMessage(msg.to,mc)
                                
                            elif cmd.startswith("mimic"):
                                sep = text.split(" ")
                                mic = text.replace(sep[0] + " ","")
                                if mic == "on":
                                    if wait["mimic"]["status"] == False:
                                        wait["mimic"]["status"] = True
                                        kifli.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴏɴ")
                                elif mic == "off":
                                    if wait["mimic"]["status"] == True:
                                        wait["mimic"]["status"] = False
                                        kifli.sendMessage(msg.to,"ᴍɪᴍɪᴄ ᴏғғ")
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅk ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                            elif cmd.startswith("checkwebsite"):
                                try:
                                    sep = text.split(" ")
                                    query = text.replace(sep[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                    data = r.text
                                    data = json.loads(data)
                                    kifli.sendImageWithURL(to, data["result"])
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkdate"):
                                try:
                                    sep = msg.text.split(" ")
                                    tanggal = msg.text.replace(sep[0] + " ","")
                                    r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                    data=r.text
                                    data=json.loads(data)
                                    ret_ = "[ D A T E ]"
                                    ret_ += "\nDate Of Birth : {}".format(str(data["data"]["lahir"]))
                                    ret_ += "\nAge : {}".format(str(data["data"]["usia"]))
                                    ret_ += "\nBirthday : {}".format(str(data["data"]["ultah"]))
                                    ret_ += "\nZodiak : {}".format(str(data["data"]["zodiak"]))
                                    kifli.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checkpraytime "):
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                r = requests.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(location))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Makassar")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "sᴜʙᴜʜ : " and data[2] != "ᴅᴢᴜʜᴜʀ : " and data[3] != "ᴀsʜᴀʀ : " and data[4] != "ᴍᴀɢʜʀɪʙ : " and data[5] != "ɪsʜᴀ : ":
                                    ret_ = "╔═══[ ᴊᴀᴅᴡᴀʟ sʜᴏʟᴀᴛ ]"
                                    ret_ += "\n╠══[ sᴇᴋɪᴛᴀʀ " + data[0] + " ]"
                                    ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n╠❂➣ " + data[1]
                                    ret_ += "\n╠❂➣ " + data[2]
                                    ret_ += "\n╠❂➣ " + data[3]
                                    ret_ += "\n╠❂➣ " + data[4]
                                    ret_ += "\n╠❂➣ " + data[5]
                                    ret_ += "\n╚════[ ✯ ᴅk ʙᴏᴛ ✯ ]"
                                    kifli.sendMessage(msg.to, str(ret_))
                            elif cmd.startswith("checkweather "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    tz = pytz.timezone("Asia/Makassar")
                                    timeNow = datetime.now(tz=tz)
                                    if "result" not in data:
                                        ret_ = "╔═══[ ᴡᴇᴀᴛʜᴇʀ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0].replace("Temperatur di kota ","")
                                        ret_ += "\n╠❂➣ sᴜʜᴜ : " + data[1].replace("Suhu : ","") + "°ᴄ"
                                        ret_ += "\n╠❂➣ ᴋᴇʟᴇᴍʙᴀʙᴀɴ : " + data[2].replace("Kelembaban : ","") + "%"
                                        ret_ += "\n╠❂➣ ᴛᴇᴋᴀɴᴀɴ ᴜᴅᴀʀᴀ : " + data[3].replace("Tekanan udara : ","") + "ʜᴘᴀ "
                                        ret_ += "\n╠❂➣ ᴋᴇᴄᴇᴘᴀᴛᴀɴ ᴀɴɢɪɴ : " + data[4].replace("Kecepatan angin : ","") + "ᴍ/s"
                                        ret_ += "\n╠════[ ᴛɪᴍᴇ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ᴛᴀɴɢɢᴀʟ : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                        ret_ += "\n╠❂➣ ᴊᴀᴍ : " + datetime.strftime(timeNow,'%H:%M:%S') + " ᴡɪʙ"
                                        ret_ += "\n╚════[ ✯ ᴅk ʙᴏᴛ ✯ ]"
                                        kifli.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("checklocation "):
                                try:
                                    sep = text.split(" ")
                                    location = text.replace(sep[0] + " ","")
                                    r = requests.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(location))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╔═══[ ʟᴏᴄᴀᴛɪᴏɴ sᴛᴀᴛᴜs ]"
                                        ret_ += "\n╠❂➣ ʟᴏᴄᴀᴛɪᴏɴ : " + data[0]
                                        ret_ += "\n╠❂➣  ɢᴏᴏɢʟᴇ ᴍᴀᴘs : " + link
                                        ret_ += "\n╚════[ ✯ ᴅk ʙᴏᴛ ✯ ]"
                                        kifli.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instainfo"):
                                try:
                                    sep = text.split(" ")
                                    search = text.replace(sep[0] + " ","")
                                    r = requests.get("https://www.instagram.com/{}/?__a=1".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data != []:
                                        ret_ = "╔══[ Profile Instagram ]"
                                        ret_ += "\n╠ Nama : {}".format(str(data["graphql"]["user"]["full_name"]))
                                        ret_ += "\n╠ Username : {}".format(str(data["graphql"]["user"]["username"]))
                                        ret_ += "\n╠ Bio : {}".format(str(data["graphql"]["user"]["biography"]))
                                        ret_ += "\n╠ Pengikut : {}".format(str(data["graphql"]["user"]["edge_followed_by"]["count"]))
                                        ret_ += "\n╠ Diikuti : {}".format(str(data["graphql"]["user"]["edge_follow"]["count"]))
                                        if data["graphql"]["user"]["is_verified"] == True:
                                            ret_ += "\n╠ Verifikasi : Sudah"
                                        else:
                                            ret_ += "\n╠ Verifikasi : Belum"
                                        if data["graphql"]["user"]["is_private"] == True:
                                            ret_ += "\n╠ Akun Pribadi : Iya"
                                        else:
                                            ret_ += "\n╠ Akun Pribadi : Tidak"
                                        ret_ += "\n╠ Total Post : {}".format(str(data["graphql"]["user"]["edge_owner_to_timeline_media"]["count"]))
                                        ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                                        path = data["graphql"]["user"]["profile_pic_url_hd"]
                                        kifli.sendImageWithURL(to, str(path))
                                        kifli.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instapost"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")   
                                    cond = text.split("|")
                                    username = cond[0]
                                    no = cond[1] 
                                    r = requests.get("http://rahandiapi.herokuapp.com/instapost/{}/{}?key=betakey".format(str(username), str(no)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["find"] == True:
                                        if data["media"]["mediatype"] == 1:
                                            kifli.sendImageWithURL(msg.to, str(data["media"]["url"]))
                                        if data["media"]["mediatype"] == 2:
                                            kifli.sendVideoWithURL(msg.to, str(data["media"]["url"]))
                                        ret_ = "╔══[ Info Post ]"
                                        ret_ += "\n╠ Jumlah Like : {}".format(str(data["media"]["like_count"]))
                                        ret_ += "\n╠ Jumlah Comment : {}".format(str(data["media"]["comment_count"]))
                                        ret_ += "\n╚══[ Caption ]\n{}".format(str(data["media"]["caption"]))
                                        kifli.sendMessage(to, str(ret_))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("instastory"):
                                try:
                                    sep = text.split(" ")
                                    text = text.replace(sep[0] + " ","")
                                    cond = text.split("|")
                                    search = str(cond[0])
                                    if len(cond) == 2:
                                        r = requests.get("http://rahandiapi.herokuapp.com/instastory/{}?key=betakey".format(search))
                                        data = r.text
                                        data = json.loads(data)
                                        if data["url"] != []:
                                            num = int(cond[1])
                                            if num <= len(data["url"]):
                                                search = data["url"][num - 1]
                                                if search["tipe"] == 1:
                                                    kifli.sendImageWithURL(to, str(search["link"]))
                                                if search["tipe"] == 2:
                                                    kifli.sendVideoWithURL(to, str(search["link"]))
                                except Exception as error:
                                    logError(error)
                                    
                            elif cmd.startswith("say-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("say-" + lang + " ","")
                                if lang not in list_language["list_textToSpeech"]:
                                    return kifli.sendMessage(to, "ʟᴀɴɢᴜᴀɢᴇ ɴᴏᴛ ғᴏᴜɴᴅ")
                                tts = gTTS(text=say, lang=lang)
                                tts.save("hasil.mp3")
                                kifli.sendAudio(to,"hasil.mp3")
                                
                            elif cmd.startswith("searchimage"):
                                try:
                                    separate = msg.text.split(" ")
                                    search = msg.text.replace(separate[0] + " ","")
                                    r = requests.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(search))
                                    data = r.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        items = data["result"]
                                        path = random.choice(items)
                                        a = items.index(path)
                                        b = len(items)
                                        kifli.sendImageWithURL(to, str(path))
                                except Exception as error:
                                    logError(error)
                            elif cmd.startswith("searchmusic "):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = str(cond[0])
                                result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                                data = result.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ᴍᴜsɪᴄ ]"
                                    for music in data["result"]:
                                        num += 1
                                        ret_ += "\n╠ {}. {}".format(str(num), str(music["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ] ".format(str(len(data["result"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ᴍᴜsɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜᴍᴜsɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    kifli.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["result"]):
                                        music = data["result"][num - 1]
                                        result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                        data = result.text
                                        data = json.loads(data)
                                        if data["result"] != []:
                                            ret_ = "╔══════[ ᴍᴜsɪᴄ ]"
                                            ret_ += "\n╠❂➣ ᴛɪᴛʟᴇ : {}".format(str(data["result"]["song"]))
                                            ret_ += "\n╠❂➣ ᴀʟʙᴜᴍ : {}".format(str(data["result"]["album"]))
                                            ret_ += "\n╠❂➣ sɪᴢᴇ : {}".format(str(data["result"]["size"]))
                                            ret_ += "\n╠❂➣ ʟɪɴᴋ :  {}".format(str(data["result"]["mp3"][0]))
                                            ret_ += "\n╚════[ ✯ ᴅk ʙᴏᴛ ✯ ]"
                                            kifli.sendImageWithURL(to, str(data["result"]["img"]))
                                            kifli.sendMessage(to, str(ret_))
                                            kifli.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                            elif cmd.startswith("searchlyric"):
                                sep = msg.text.split(" ")
                                query = msg.text.replace(sep[0] + " ","")
                                cond = query.split("|")
                                search = cond[0]
                                api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                                data = api.text
                                data = json.loads(data)
                                if len(cond) == 1:
                                    num = 0
                                    ret_ = "╔══[ ʀᴇsᴜʟᴛ ʟʏʀɪᴄ ]"
                                    for lyric in data["results"]:
                                        num += 1
                                        ret_ += "\n╠❂➣ {}. {}".format(str(num), str(lyric["single"]))
                                    ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴍᴜsɪᴄ ]".format(str(len(data["results"])))
                                    ret_ += "\n\nᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴅᴇᴛᴀɪʟs ʟʏʀɪᴄ, sɪʟᴀʜᴋᴀɴ ɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ {}sᴇᴀʀᴄʜʟʏʀɪᴄ {}|「ɴᴜᴍʙᴇʀ」".format(str(setKey), str(search))
                                    kifli.sendMessage(to, str(ret_))
                                elif len(cond) == 2:
                                    num = int(cond[1])
                                    if num <= len(data["results"]):
                                        lyric = data["results"][num - 1]
                                        api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                        data = api.text
                                        data = json.loads(data)
                                        lyrics = data["results"]["lyric"]
                                        lyric = lyrics.replace('ti:','Title - ')
                                        lyric = lyric.replace('ar:','Artist - ')
                                        lyric = lyric.replace('al:','Album - ')
                                        removeString = "[1234567890.:]"
                                        for char in removeString:
                                            lyric = lyric.replace(char,'')
                                        kifli.sendMessage(msg.to, str(lyric))
                            elif cmd.startswith("searchyoutube"):
                                sep = text.split(" ")
                                search = text.replace(sep[0] + " ","")
                                params = {"search_query": search}
                                r = requests.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╔══[ ʀᴇsᴜʟᴛ ʏᴏᴜᴛᴜʙᴇ ]"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n╠❂➣{} ]".format(str(data["title"]))
                                    ret_ += "\n╠❂ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╚══[ ᴛᴏᴛᴀʟ {} ᴠɪᴅᴇᴏ ]".format(len(datas))
                                kifli.sendMessage(to, str(ret_))
                            elif cmd.startswith("tr-"):
                                sep = text.split("-")
                                sep = sep[1].split(" ")
                                lang = sep[0]
                                say = text.replace("tr-" + lang + " ","")
                                if lang not in list_language["list_translate"]:
                                    return kifli.sendMessage(to, "Language not found")
                                translator = Translator()
                                hasil = translator.translate(say, dest=lang)
                                A = hasil.text
                                kifli.sendMessage(to, str(A))
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅk ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                        if text.lower() == "mykey":
                            kifli.sendMessage(to, "ᴋᴇʏᴄᴏᴍᴍᴀɴᴅ sᴀᴀᴛ ɪɴɪ [ {} ]".format(str(wait["keyCommand"])))
                        elif text.lower() == "setkey on":
                            wait["setKey"] = True
                            kifli.sendMessage(to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ sᴇᴛᴋᴇʏ")
                        elif text.lower() == "setkey off":
                            wait["setKey"] = False
                            kifli.sendMessage(to, "ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ sᴇᴛᴋᴇʏ")
#------------------------------------============================------------------------------------#
#======================-----------✰ ᴅk ʙᴏᴛ ✰-----------======================#
#------------------------------------============================------------------------------------#
                    elif msg.contentType == 1:
                        if wait["changePictureProfile"] == True:
                            path = kifli.downloadObjectMsg(msg_id)
                            wait["changePictureProfile"] = False
                            kifli.updateProfilePicture(path)
                            kifli.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ᴘʀᴏғɪʟᴇ")
                        if msg.toType == 2:
                            if to in wait["changeGroupPicture"]:
                                path = kifli.downloadObjectMsg(msg_id)
                                wait["changeGroupPicture"].remove(to)
                                kifli.updateGroupPicture(to, path)
                                kifli.sendMessage(to, "sᴜᴄᴄᴇs ᴄʜᴀɴɢᴇ ᴘʜᴏᴛᴏ ɢʀᴏᴜᴘ")
                    elif msg.contentType == 7:
                        if wait["checkSticker"] == True:
                            stk_id = msg.contentMetadata['STKID']
                            stk_ver = msg.contentMetadata['STKVER']
                            pkg_id = msg.contentMetadata['STKPKGID']
                            ret_ = "╔════[ sᴛɪᴄᴋᴇʀ ɪɴғᴏ ] "
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ɪᴅ : {}".format(stk_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋᴀɢᴇs ɪᴅ : {}".format(pkg_id)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴠᴇʀsɪᴏɴ : {}".format(stk_ver)
                            ret_ += "\n╠❂➣ sᴛɪᴄᴋᴇʀ ᴜʀʟ : line://shop/detail/{}".format(pkg_id)
                            ret_ += "\n╚════[ ✯ ᴅk ʙᴏᴛ ✯ ]"
                            kifli.sendMessage(to, str(ret_))
                    elif msg.contentType == 13:
                        if wait["checkContact"] == True:
                            try:
                                contact = kifli.getContact(msg.contentMetadata["mid"])
                                if kifli != None:
                                    cover = kifli.getProfileCoverURL(msg.contentMetadata["mid"])
                                else:
                                    cover = "Tidak dapat masuk di line channel"
                                path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                try:
                                    kifli.sendImageWithURL(to, str(path))
                                except:
                                    pass
                                ret_ = "╔═══[ ᴅᴇᴛᴀɪʟs ᴄᴏɴᴛᴀᴄᴛ ]"
                                ret_ += "\n╠❂➣ ɴᴀᴍᴀ : {}".format(str(contact.displayName))
                                ret_ += "\n╠❂➣ ᴍɪᴅ : {}".format(str(msg.contentMetadata["mid"]))
                                ret_ += "\n╠❂➣ ʙɪᴏ : {}".format(str(contact.statusMessage))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴘʀᴏғɪʟᴇ : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                                ret_ += "\n╠❂➣ ɢᴀᴍʙᴀʀ ᴄᴏᴠᴇʀ : {}".format(str(cover))
                                ret_ += "\n╚════[ ✯ ᴅK ʙᴏᴛ ✯ ]"
                                kifli.sendMessage(to, str(ret_))
                            except:
                                kifli.sendMessage(to, "ᴋᴏɴᴛᴀᴋ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ")
                    elif msg.contentType == 16:
                        if wait["checkPost"] == True:
                            try:
                                ret_ = "╔════[ ᴅᴇᴛᴀɪʟs ᴘᴏsᴛ ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = kifli.getContact(sender)
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠❂➣ ᴀᴜᴛʜᴏʀ : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠❂➣ ᴜʀʟ : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠❂➣ ᴍᴇᴅɪᴀ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠❂➣ ᴏʙᴊᴇᴄᴛ ᴜʀʟ : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠❂➣ sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠❂➣ ɴᴏᴛᴇ : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚════[ ✯ ᴅK ʙᴏᴛ ✯ ]"
                                kifli.sendMessage(to, str(ret_))
                            except:
                                kifli.sendMessage(to, "ɪɴᴠᴀʟɪᴅ ᴘᴏsᴛ")
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
                
        if op.type == 26:
            msg = op.message
            if wait["autoResponPc"] == True:
                if msg.toType == 0:
                    kifli.sendChatChecked(msg._from,msg.id)
                    contact = kifli.getContact(msg._from)
                    cName = contact.displayName
                    balas = ["╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅk ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nᴍᴏʜᴏɴ ᴍᴀᴀғ sᴀʏᴀ sᴇᴅᴀɴɢ sɪʙᴜᴋ, ɪɴɪ ᴀᴅᴀʟᴀʜ ᴘᴇsᴀɴ ᴏᴛᴏᴍᴀᴛɪs, ᴊɪᴋᴀ ᴀᴅᴀ ʏᴀɴɢ ᴘᴇɴᴛɪɴɢ ᴍᴏʜᴏɴ ʜᴜʙᴜɴɢɪ sᴀʏᴀ ɴᴀɴᴛɪ, ᴛᴇʀɪᴍᴀᴋᴀsɪʜ...","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅk ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ ʟᴀɢɪ sɪʙᴜᴋ ʏᴀ ᴋᴀᴋ ᴊᴀɴɢᴀɴ ᴅɪɢᴀɴɢɢᴜ","╔════════════════════╗\n                   「ᴀᴜᴛᴏ ʀᴇᴘʟʏ」\n                             ʙʏ:\n                    ✰ ᴅk ʙᴏᴛ ✰\n╚════════════════════╝\n\nʜᴀʟʟᴏ 「" + cName + "」\nsᴀʏᴀ sᴇᴅᴀɴɢ ᴛɪᴅᴜʀ ᴋᴀᴋ"]
                    dee = "" + random.choice(balas)
                    kifli.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                    kifli.sendMessage(msg._from,dee)
                
        if op.type == 26:
            try:
                print ("[ 26 ] RECIEVE MESSAGE")
                msg = op.message
                text = msg.text
                msg_id = msg.id
                receiver = msg.to
                sender = msg._from
                if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                    if msg.toType == 0:
                        if sender != kifli.profile.mid:
                            to = sender
                        else:
                            to = receiver
                    elif msg.toType == 1:
                        to = receiver
                    elif msg.toType == 2:
                        to = receiver
                    if wait["autoRead"] == True:
                        kifli.sendChatChecked(to, msg_id)
                    if to in read["readPoint"]:
                        if sender not in read["ROM"][to]:
                            read["ROM"][to][sender] = True
                    if sender in wait["mimic"]["target"] and wait["mimic"]["status"] == True and wait["mimic"]["target"][sender] == True:
                        text = msg.text
                        if text is not None:
                            kifli.sendMessage(msg.to,text)
                    if wait["unsendMessage"] == True:
                        try:
                            msg = op.message
                            if msg.toType == 0:
                                kifli.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                            else:
                                kifli.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                                msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                        except Exception as error:
                            logError(error)
                    if msg.contentType == 0:
                        if text is None:
                            return
                        if "/ti/g/" in msg.text.lower():
                            if wait["autoJoinTicket"] == True:
                                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                links = link_re.findall(text)
                                n_links = []
                                for l in links:
                                    if l not in n_links:
                                        n_links.append(l)
                                for ticket_id in n_links:
                                    group = ririn.findGroupByTicket(ticket_id)
                                    kifli.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    kifli.sendMessage(to, "sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴛᴇʀᴇᴅ ᴛʜᴇ ɢʀᴏᴜᴘ %s" % str(group.name))
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if kifliMid in mention["M"]:
                                    if wait["autoRespon"] == True:
                                    	kifli.sendChatChecked(msg._from,msg.id)
                                    	contact = kifli.getContact(msg._from)
                                    	kifli.sendImageWithURL(msg._from, "http://dl.profile.line-cdn.net{}".format(contact.picturePath))
                                    	sendMention(sender, "Loha @!      ,\nInvite aja aim ke Gc Kk\nBuat Bantu2\nsmoga Brmanfaat Ya\nAmin", [sender])
                                    	dee = "" + random.choice(balas)
                                    break
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if wait["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = kifli.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                            else:
                                name_ = contact.displayName
                                ret_ = "sᴇɴᴅ ᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ."
                                ret_ += "\nsᴇɴᴅᴇʀ : @!      "
                                ret_ += "\nsᴇɴᴅ ᴀᴛ : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nᴛʏᴘᴇ : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nᴛᴇxᴛ : {}".format(str(msg_dict[msg_id]["text"]))
                                sendMention(at, str(ret_), [contact.mid])
                            del msg_dict[msg_id]
                        else:
                            kifli.sendMessage(at,"sᴇɴᴛᴍᴇssᴀɢᴇ ᴄᴀɴᴄᴇʟʟᴇᴅ,ʙᴜᴛ ɪ ᴅɪᴅɴ'ᴛ ʜᴀᴠᴇ ʟᴏɢ ᴅᴀᴛᴀ.\nsᴏʀʀʏ > <")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                    
        if op.type == 55:
        	try:
        		group_id = op.param1
        		user_id=op.param2
        		subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
        	except Exception as e:
        		print(e)
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = kifli.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        kifli.sendMessage(op.param1, "Asslamu alaikum " + "☞ " + Name + " ☜" + "\nᴅɪᴇᴍ ᴅɪᴇᴍ Tercyduk Juga ...\nsɪɴɪ ɪᴋᴜᴛ ɴɢᴏᴘɪ\nSambil Gosip  ")
                                    else:
                                        kifli.sendMessage(op.param1, "Loha Kak " + "☞ " + Name + " ☜" + "\nAnda Tercyduk Cctv Cess\nSubhanallah  ")
                                else:
                                    kifli.sendMessage(op.param1, "ihhah Si " + "☞ " + Name + " ☜" + "\nɴɢᴀᴘᴀɪɴ Cuma Nyimak...\nBantu Owner Ramaikan Gc Dhonk")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
                
        if op.type == 55:
            print ("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                else:
                   pass
            except Exception as error:
                logError(error)
                traceback.print_tb(error.__traceback__)
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)

while True:
    try:
        delete_log()
        ops = kifliPoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                kifliBot(op)
                kifliPoll.setRevision(op.revision)
    except Exception as error:
        logError(error)
        
def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
atexit.register(atend)