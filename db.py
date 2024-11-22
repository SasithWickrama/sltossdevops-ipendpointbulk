import traceback
import cx_Oracle

class DbConnection:
    def dbconn(self):
        try:
            dsn_tns = cx_Oracle.makedsn('172.25.1.172', '1521', service_name='clty')
            conn = cx_Oracle.connect(user='OSSPRG', password='prgoss456', dsn=dsn_tns)
            return conn
        except Exception as e:
            print("Exception : %s" % traceback.format_exc())
            return traceback.format_exc()
