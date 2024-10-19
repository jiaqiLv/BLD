import pymysql


if __name__ == '__main__':
    connection = pymysql.connect(
        host='192.168.199.4',
        port=53306,
        user='root',
        password='Tongji409!',
        database='bld',
        charset='utf8mb4'
    )