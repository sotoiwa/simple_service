# simple_service

マイクロサービスのテスト用のサンプルアプリケーション。

## イメージのビルド

```shell
docker build -t sotoiwa540/simple-service:1.0 .
docker push sotoiwa540/simple-service:1.0
```

## 環境変数

|環境変数|説明|
|---|---|
|SERVICE_NAME|このサービスの名前|
|BACKEND_URLS|カンマ区切りで記述されたバックエンドサービスのURL|

## レスポンス例

```json
{
  "backends": [
    {
      "content": {
        "backends": [],
        "hostname": "ip-10-0-12-127.ap-northeast-1.compute.internal",
        "request": {
          "headers": {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Content-Length": "0",
            "Host": "svc-b.simple-service.local:5000",
            "User-Agent": "python-requests/2.22.0",
            "X-Amzn-Trace-Id": "Root=1-5de0cf8c-9f43a0e81cedfbd035788e60; Parent=598b50565adab1c7; Sampled=1",
            "X-Envoy-Expected-Rq-Timeout-Ms": "15000",
            "X-Forwarded-Proto": "http",
            "X-Request-Id": "5cd98e1d-0856-930d-8b8c-2fabced158bd"
          },
          "method": "GET",
          "url": "http://svc-b.simple-service.local:5000/"
        },
        "serviceName": "ServiceB"
      },
      "statusCode": 200,
      "url": "http://svc-b.simple-service.local:5000"
    }
  ],
  "hostname": "ip-10-0-11-177.ap-northeast-1.compute.internal",
  "request": {
    "headers": {
      "Accept": "*/*",
      "Content-Length": "0",
      "Host": "fargate-elb-1016091394.ap-northeast-1.elb.amazonaws.com",
      "User-Agent": "curl/7.54.0",
      "X-Amzn-Trace-Id": "Root=1-5de0cf8c-9f43a0e81cedfbd035788e60; Parent=7a1b32fb00daa8bc; Sampled=1",
      "X-Envoy-Expected-Rq-Timeout-Ms": "15000",
      "X-Forwarded-For": "27.0.3.145",
      "X-Forwarded-Port": "80",
      "X-Forwarded-Proto": "http",
      "X-Request-Id": "e27a0271-fe6b-9db0-bf27-b61f65dfeafd"
    },
    "method": "GET",
    "url": "http://fargate-elb-1016091394.ap-northeast-1.elb.amazonaws.com/"
  },
  "serviceName": "ServiceA"
}
```
