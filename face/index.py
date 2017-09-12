# -*- coding: utf-8 -*-
#初始化一个AipFace对象
# 引入人脸识别 SDK
from aip import AipFace
from config import *

# 初始化AipFace对象
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 人脸注册
# 接口描述
# 用于从人脸库中新增用户，可以设定多个用户所在组，及组内用户的人脸图片，
# 请求说明
# 举例，要注册一个新用户，用户id为uid1，加入组id为group1, 注册成功后服务端会返回操作的logid：

# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

aipFace.addUser(  
            'uid1', 
            'user info', 
            'group1',
            get_file_content('user.jpg')
            )

# 人脸注册请求参数要求：

# 所有图片经base64编码后的图片数据总和不超过10M。