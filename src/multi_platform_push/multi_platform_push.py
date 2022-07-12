import yaml,os

#读配置文件
with open(os.path.join(os.path.dirname(__file__),'config.yml'),encoding='UTF-8') as conf:
    config = yaml.load(conf.read(),Loader = yaml.Loader)
    room_id = config['roomid']
    pushtype = config['pushtype']
    pushurl = config['pushurl']
    key = config['pushkey']
    content = config['pushcontent']

def push_type():
    '''
    获取推送链接。
    '''
    global url
    if pushtype == 'pushdeer':
        url = 'https://api2.pushdeer.com/message/push?' + key + '&text=' + content
    if pushtype == 'pushdeer_sh':
        url = pushurl + '/message/push?' + key + '&text=' + content
    if pushtype == 'bark':
        url = pushurl + key + '/' + key + '/' + content
    if pushtype == 'serversama':
        url = 'https://sctapi.ftqq.com?act=' + key + '.send?title=' + content
    if pushtype == 'pushplus':
        url = 'http://www.pushplus.plus/send?token=' + key + '&content=' + content