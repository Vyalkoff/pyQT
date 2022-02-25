import subprocess
from ipaddress import ip_address


def host_ping(list_address):
    result = {'Доступные узлы': [], 'Недоступные узлы': []}
    for address in list_address:
        try:
            address = ip_address(address)
        except Exception:
            pass
        command = ['ping', '-w', ' 3', str(address)]
        proc = subprocess.Popen(command, stdout=subprocess.PIPE)
        proc.wait()

        if proc.returncode == 0:
            result['Доступные узлы'].append(address)
            print(f'Узел Доступен {address}')
        else:
            result['Недоступные узлы'].append(address)
            print(f'Узел Недоступен {address}')
    return result


if __name__ == '__main__':
    list_add = ['localhost', 'google.com', '192.265.894.256']
    print(host_ping(list_add))
