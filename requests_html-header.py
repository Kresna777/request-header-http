# memakai HTMLSession di dalam package requests_html untuk
# menggunakan randon user agent

from requests_html import HTMLSession

url = "https://httpbin.org/headers"

s = HTMLSession()
r = s.get(url)

print(r.text)
