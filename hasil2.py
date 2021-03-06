U
    ᫬`?*  ?                   @   s?  d dl mZmZ d dlZd dlZd dlZd dlZd dlZd dlZd dl	m
Z
 d dlZd dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlmZ d dlmZmZ e?? Zd dlZd dlZd dlZejd Zd Zd	eks?d
ek?rvede? ed?Zed Ze? d?Z!ee!? ee!k?r.ed? e"?  nHdZ#ed? e$de d?Z%ee# Z&e%?'e&? e%j( eZe?)e?Z*e*?+?  ejd Z,ee,? e,dk?r?dZ-ed? nne,dk?r?dZ-ed? nVe,dk?r?dZ-ed? n>e,dk?r?dZ-ed? n&e,d k?r d!Z-ed"? ned#? e"?  zejd$ Z.W n   d%Z.Y nX e?)e?Z*zejd& Z/dZ/W n   d Z/Y nX ze*?+?  W n   e*?+?  e*?0?  Y nX ee? ed'? d(d)iZ1d(d*iZ2d(d+iZ3d(d,iZ3d dl4Z4e4?5d-de4?6d.?? i a7et7? d/d0? Z8d1d2? Z9d3d4? Z:ej;d5k?re9?  ej;d6k?re:?  d a<e*?n z*ze*j@?Ae*?Be-d:?? W n   Y nX W 5 e*?=ej>e-d7??d8d9? ?Z?X e*?+?  e*?C?  ee?D? d;d<? W 5 Q R X dS )=?    )?TelegramClient?eventsN)?errors)?BeautifulSoup)?JoinChannelRequest)?LeaveChannelRequest)?GetBotCallbackAnswerRequest?StartBotRequest?   z+1z+62Zcreateznama akun : z.txtz	akunakun/zada yg sama ganti nama dlz) 1320901 117011e804dc754e2d5c3dd07a3edc15?ok?w?   ?lZLitecoin_click_botZLTC?cZBCH_clickbotZBCH?bZBitCoinClick_botZBitcoin?dZDogecoin_click_botZDoge?zZZcash_click_botZZcashZgketemuclick?   Z123?   ?connectz
User-Agentz?Mozilla/5.0 (Linux; Android 5.1; A1603 Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36z?Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.0 Chrome/87.0.4280.141 Mobile Safari/537.36zzMozilla/5.0 (Linux; Android 10; SM-A207F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36z?Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36Zfirefoxz/C://Program Files//Mozilla Firefox//firefox.exec                  C   s?   t dd?} t| ?? ?}| ??  |?d?}t|?}t|? t|? t|?D ]6}t|| ? || ?d?}t|? |d t|d < qHtt? d S )Nz	kokis.txt?rz; ?=r
   r   )	?open?str?read?close?split?len?print?range?kokis)ZOOOO0O0O0OOOO0OO0ZOOO0OOO000O0OOOOOZOOO0O0OO00O0OOOOOZOO00000O0O0000O00ZO0O0OOO0O0000O0OOZO00OOO000O00OO0O0? r!   ?dsoooxyry.py?	bacakokis>   s    

 r#   c               	   C   sd   zt ?d? W n   Y nX dd l} td??}| ?|?}W 5 Q R X i a|D ]}|d t|d < qJd S )NzZmv /$HOME/storage/shared/download/doge.click.cookies.json /$HOME/storage/shared/ular/tele/r   zdoge.click.cookies.json?value?name)?os?system?jsonr   ?loadr    )r(   ZOOOO0O00O0OO0OO00ZO000O00OOOOO000O0ZO0OO00O00O0OO00OOr!   r!   r"   ?
bacakokis2L   s      
r*   c                  C   sp   t ?? } d}|d }t?|?}|?? }i a|?d?D ].}|D ]$}dt|?kr<|d t|d <  q4q<q4td? d S )N?YC:\Users\ikhsan prasetia\AppData\Roaming\Mozilla\Firefox\Profiles\wwhq9dho.jagajarakkita\?cookies.sqlite?SELECT * FROM moz_cookies?.r   r   ?kokis3)	r&   ?getcwd?sqlite3r   ?cursorr    ?executer   r   )ZO0O0O00OOOO0OO0O0ZOOOOO00OO000OOOO0ZOOOOOOOO000O00OO0ZO0OOO00OOOOOO0O00ZO0OO0OO0000OO0O0OZO0OOO0O0O0O0000OOZOO0O00O000OO0000Or!   r!   r"   ?
bacakokis3V   s    
r4   ?posix?nt)Z
from_usersc                 ?   s`  d| j k?r?tdkr&t?d?I d H  qda| jjd jd j}t|? z,t	j
|ttddd?}|jdkrpt|d	? W n6   td
? t?d?I d H  | ?d?I d H  Y d S X d}|jdk?r?tdk?r?t|||? |d dkr?| ?? I d H  t?d?I d H  t?? }d}|d }t?|?}|?? }i a|?d?D ]6}	|	D ]*}
dt|
?k?r6|	d t|	d <  ?q.?q6?q.td? t	j
|ttddd?}|d7 }|dkr??q?q?t|? |jdk?r?|dk?r?t|d
? t?d?I d H  | ?d?I d H  d S z?t|jd?}|jdk?r|jdk?rt|? d}|jddd?D ]2}|?
d?}|?
d?}|?
d?}tdt|?? ?q$t?t|?d ?I d H  t	jd||d ?tdtdd!?}W n   Y nX d S d"| j k?r?t| j ? t?d#?I d H  dad S d$| j k?r?t| j ? t?d#?I d H  dad S d%| j k?r*t| j ? t?d#?I d H  dad S d&| j k?r\t?d#?I d H  td'? t?? I d H  d S )(Nz Press the "Visit website" buttonr
   ?
   r   ?   T)?headers?cookies?timeout?allow_redirects??   ZawalnyaZ	istirahat?<   r   r   r+   r,   r-   r.   r   r/   ?   i?  zhtml.parser? Zdivzcontainer-fluid)?class_z	data-codez
data-timerz
data-tokenZtungguzhttps://dogeclick.com/reward)?code?token)?datar9   r;   r:   r<   zYou earned ?   zSkipping task..zPlease stay on the sitez%Sorry, there are no new ads availablezIKLAN HABIS

)Zraw_text?main?asyncio?sleepZreply_markupZrowsZbuttonsZurlr   r   ?get?uar    Zstatus_codeZclickr&   r0   r1   r   r2   r3   r   r   ZcontentZfind_all?intZpost?akunsZ
disconnect)ZO0O000OOOOO0OO00OZOO0OOOO0O000O0OO0ZOO0O0OO00OO0000O0ZO0O0OO0OOO0OOOOOOZO0000OOOO0O000O0OZO0OOOOO0OO0OO0O0OZOO0O0O00OO000OOOOZO0O0000OO0000OOOOZO00OOO0OO0000O0OOZOOO00O0000OO00OOOZOOO0OOOOO0000OOOOZO00O000OO00000OOOZO0O0000OO000OO00OZO0O000OO0O0OO0OOOZO000000O0OOOO0O00ZO0O00OO000O00O000r!   r!   r"   ?handlerk   s?    
  
 



  


rM   z/visit?-ZBerhenti)EZtelethon.syncr   r   ?timerG   ?reZlojin?sysZmultiprocessingZtelethonr   r(   r&   ZrequestsZbs4r   Ztelethon.tl.functions.channelsr   r   Ztelethon.tl.functions.messagesr   r	   ZSessionr   r1   ?argvZakunkeZ
perlustartr   ?inputZnamaZnamafile?listdir?list?exitZisianr   ?oZisi?writer   Zlogin1rL   ?startZcoinZbomZmainanZsitusr   ZuaaaZuamrJ   Z
webbrowser?registerZBackgroundBrowserr    r#   r*   r4   r%   rF   ZonZ
NewMessagerM   ZloopZrun_until_completeZsend_messageZrun_until_disconnected?asctimer!   r!   r!   r"   ?<module>   s?    







  

  

  

  

  
   

 
  
   
    
K