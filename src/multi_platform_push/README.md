### Config.yml

+ **roomid**: 
B站直播间号，即（live.bilibili.com/） 后面跟的纯数字 
+ **pushtype**:  
要使用的推送平台 
##### Attribute:
|Platform              |pushtype          |
| -------------------- | ---------------- |
|Pushdeer(官方在线)    |pushdeer           |
|Pushdeer(自建服务端)  |pushdeer_sh        |
|Bark                 |bark               |
|Server酱             |serversama         |
|Pushplus             |pushplus           |

+ **pushurl**: 
部分推送平台需要填入的链接参数。
##### Attribute:
|Platform              |pushurl          |
| -------------------- | ---------------- |
|Pushdeer(官方在线)    |缺省               |
|Pushdeer(自建服务端)  |自建服务端链接      |
|Bark                 |自建bark服务端链接  |
|Server酱             |缺省               |
|Pushplus             |缺省               |
+ **pushkey**:  
各平台推送所需的参数，每个平台叫法不一样，下表为名词对照。
##### Attribute:
|Platform              |pushkey           |
| -------------------- | ---------------- |
|Pushdeer(官方在线)    |pushkey           |
|Pushdeer(自建服务端)  |pushkey           |
|Bark                 |bark_key           |
|Server酱             |Sendkey            |
|Pushplus             |pushplus的token    |
+ **pushcontent**:    
推送消息的内容  