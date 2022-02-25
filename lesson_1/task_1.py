import subprocess
from ipaddress import ip_address


def host_ping(list_address, pakeg=3):
    result = {
        'Доступные узлы': [],
        'Недоступные узлы': []
    }
    for address in list_address:

        command = ['ping', '-c', '1', '-t', str(pakeg), address, ]

        signal = subprocess.Popen(command, stdout=subprocess.PIPE)
        signal.wait()
        if signal.returncode == 0:
            print(f'{address} - Узел доступен')
            result['Доступные узлы'].append(address)
        else:
            print(f'{address} - Узел Недоступен')
            result['Недоступные узлы'].append(address)
    return result


if __name__ == '__main__':
    address = ['google.com', 'localhost', '123.456.456.46', 'hh.ru']
    host_ping(address)
