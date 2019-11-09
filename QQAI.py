from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import \
    TencentCloudSDKException
from tencentcloud.ocr.v20181119 import ocr_client, models
import base64


def jpg_to_base64(file_name: str):
    with open(file_name, 'rb') as f:  # 以二进制读取图片
        data = f.read()
        encode_str = base64.b64encode(data)  # 得到 byte 编码的数据
        b64_str = str(encode_str, 'utf-8')  # 重新编码数据
    return b64_str


try:
    cred = credential.Credential("AKIDvDMK5csukO3Ugedub3jEUWJ4aswk4dij",
                                 "MX5PTIrCIAnCML4XNyJODn7D3e19WdV7")
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ocr.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ocr_client.OcrClient(cred, "ap-shanghai", clientProfile)

    req = models.EnterpriseLicenseOCRRequest()
    b64 = jpg_to_base64()
    params = f'{{"ImageBase64":"{b64}"}}'  # 双{{/}}表示一个{/}
    req.from_json_string(params)

    resp = client.EnterpriseLicenseOCR(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
