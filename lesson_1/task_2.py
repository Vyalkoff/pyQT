from ipaddress import ip_address
from task_1 import host_ping

def host_range_ping():
    while True:
        start = input('Введите адрес: ')
        try:
            last = int(start.split('.')[3])
            break
        except Exception as e:
            print(e)
    while True:
        count_address = input('Задать диапазон: ')
        if (last + int(count_address)) >254:
            print(f'Максимум {254 - last} хостов')
        else:
            break
    list_host = [str(ip_address(start)+i) for i in range(int(count_address))]
    return host_ping(list_host)


if __name__ == '__main__':
    host_range_ping()