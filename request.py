import requests

url = 'https://example.com'

req = requests.get(url, timeout=2000)

print(f'\nTarget: {url}\n')
print(f'Status code: {req.status_code}\n')
print(' Headers '.center(30, '='))
print('')

for x in req.headers:
    print(f'{x}: {req.headers[x]}')

print('')
print(' Body '.center(30, '='))
print(f'\n{req.text}')


