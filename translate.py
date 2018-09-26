# -*- coding: utf-8 -*-
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.tmt.v20180321 import tmt_client, models
def trans(txt):
    try:
        # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
        cred = credential.Credential("AKID3xsdClXLE1dEdqPjRxIRPB8wbjhTRReg", "zm072lIdnldIm4GG4tb9WhgT6YN2gCbt")

        # 实例化要请求产品(以cvm为例)的client对象
        client = tmt_client.TmtClient(cred, "ap-shanghai")

        # 实例化一个请求对象
        req = models.TextTranslateRequest()
        req.SourceText = txt
        req.Source = "en"
        req.Target = "zh"
        req.ProjectId = 0

        # 通过client对象调用想要访问的接口，需要传入请求对象
        resp = client.TextTranslate(req)
        # 输出json格式的字符串回包
        print(type(resp))
        print(resp.to_json_string())
        return resp.to_json_string()
    except TencentCloudSDKException as err:
        print(err)
