import datetime
import db
import bulkDelete

conn = db.DbConnection.dbconn(self="")
c = conn.cursor()
sql = "select TPNO,STAT from IPEND_BULK where STAT= '0' "
c.execute(sql)

for row in c:
    TPNO, STAT = row
    #print(len(TPNO), TPNO[0])

    if len(TPNO) == 10 and TPNO[0] == '0':

        TP = TPNO[1:10]

    else:
        TP = TPNO

    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    serial = datetime.datetime.now().strftime("%y%m%d%H%M%S")

    resultats = bulkDelete.Delete.del_ats(TP)
    #print (resultats)

    if resultats[0] == '0':
        c1 = conn.cursor()
        sql = "update IPEND_BULK set ATS = :ats where TPNO = :tpno and  STAT= '0'"
        c1.execute(sql,(resultats,TPNO))
        conn.commit()
        resulthss = bulkDelete.Delete.del_hss(TPNO, dt, serial)

        if resulthss[0] == '0':
            c1 = conn.cursor()
            sql = "update IPEND_BULK set HSS = :hss where TPNO = :tpno and  STAT= '0'"
            c1.execute(sql,(resulthss,TPNO))
            conn.commit()
            resultens = bulkDelete.Delete.del_ens(TPNO, dt, serial)

            if resultens[0] == '0':
                c1 = conn.cursor()
                sql = "update IPEND_BULK set ENS = :ens,STAT= '1' where TPNO = :tpno and  STAT= '0'"
                c1.execute(sql,(resultens,TPNO))
                conn.commit()
            else:
                c1 = conn.cursor()
                sql = "update IPEND_BULK set ENS = :ens,STAT= '1' where TPNO = :tpno and  STAT= '0'"
                c1.execute(sql,(resultens,TPNO))
                conn.commit()

        else:
            c1 = conn.cursor()
            sql = "update IPEND_BULK set HSS = :hss where TPNO = :tpno and  STAT= '0'"
            c1.execute(sql,(resulthss,TPNO))
            conn.commit()
    else:
        print (resultats)
        print (TPNO)
        c1 = conn.cursor()
        sql = "update IPEND_BULK set ATS = :ats where TPNO = :tpno and  STAT= '0'"
        c1.execute(sql,(resultats,TPNO))
        conn.commit()
