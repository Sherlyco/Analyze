import requests
import json
import jsonpath

class Douyin:
    def page_num(self,max_cursor):
        #随机码
        random_field = '00nvcRAUjgJQBMjqpgesfdNJ72&dytk=4a01c95562f1f10264fb14086512f919'
        #网址的主体
        url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid=MS4wLjABAAAAU7Bwg8WznVaafqWLyLUwcVUf9LgrKGYmctJ3n5SwlOA&count=21&max_cursor=' + str(max_cursor) + '&aid=1128&_signature=' + random_field
        #请求头
        headers = {
            'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        }
        response = requests.get(url,headers=headers).text
        #转换成json数据
        resp = json.loads(response)
        #提取到max_cursor
        max_cursor = resp['max_cursor']
        #遍历
        i=0
        for data in resp['aweme_list']:
            # 视频简介
            video_title = data['desc']
            #使用jsonpath语法提取paly_addr
            video_url = data['video']['play_addr']['url_list'][1]

            video = requests.get(video_url, headers=headers).content
            with open('dyv{}.mp4'.format(i), 'wb') as f:
                print('正在下载：', video_title)
                f.write(video)
                f.flush()
            i += 1

        #判断停止构造网址的条件
        if max_cursor==0:
            return 1
        else:
            douyin.page_num(max_cursor)

if __name__ == '__main__':
     douyin = Douyin()
     douyin.page_num(max_cursor=0)