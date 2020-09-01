from socket import gethostbyname as ghbn, gethostname as ghn
import redis

ip_addr = ghbn(ghn())
port_num = 6379
client = redis.Redis(host=ip_addr, port=port_num)
client.set('usd_to_aed', '3.67')
client.set('aed_to_usd', '0.27')