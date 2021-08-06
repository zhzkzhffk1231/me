import pyupbit

access = "qvVxpk5eB1ZPzBxlp5XelnqbLqooVAUIHsEmsdyA"          # Open API에서 위에걸로 바꾸기
secret = "SUxnlydlzzAG3o0xqdLEE4JGt8YrZ78nFFs0wkZn"          # Open API에서 밑에걸로 바꾸기
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
