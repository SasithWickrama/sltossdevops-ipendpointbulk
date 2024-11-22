import traceback
import re
import requests
import xml.etree.ElementTree as ET
from log import getLogger

logger = getLogger('bulkdelete', 'logs/bulkdelete')

imsApi = "http://10.68.128.3:8080/spg";
udrApi = "http://10.68.137.20:3001";

headers = {
    'Content-Type': 'text/html; charset=utf-8'
}

class Delete:
    def del_ats(tpno):
        xmlfile = open('files/DELATS.xml', 'r')
        body = xmlfile.read()

        try:
            response = requests.request("POST", imsApi, headers=headers,
                                        data=body.format(tpno=tpno))
            print(response.request.body)
            #print(response.text)
            logger.info("Start : =========================================================================")
            logger.info(response.request.body)
            
            logger.info("Response : =================================")
            logger.info(response.text)
            logger.info("End : =========================================================================")
            
            ResultCode = re.findall("<m:ResultCode>(.*?)</m:ResultCode>", str(response.content))
            ResultDesc = re.findall("<m:ResultDesc>(.*?)</m:ResultDesc>", str(response.content))
            
            print(ResultCode[0])
            print(ResultDesc[0])
                
            return str(ResultCode[0])+'#'+str(ResultDesc[0])
        except Exception as e:
            print("Exception : %s" % traceback.format_exc())
            return str(e)


    def del_hss(tpno,dt,serial):
        xmlfile = open('files/UDR_DEL_HSS.xml', 'r')
        body = xmlfile.read()

        try:
            response = requests.request("POST", udrApi, headers=headers,
                                        data=body.format(tpno=tpno, DT=dt, SERIAL=serial))

            print(response.text)
            
            logger.info("Start : =========================================================================")
            logger.info(response.request.body)
            
            logger.info("Response : =================================")
            logger.info(response.text)
            logger.info("End : =========================================================================")
            root = ET.fromstring(response.content)
            for resultc in root.iter('ResultCode'):
                ResultCode = resultc.text

            for resultd in root.iter('ResultDescr'):
                ResultDesc = resultd.text

            return ResultCode+'#'+ResultDesc
        except Exception as e:
            return str(e)


    def del_ens(tpno,dt,serial):
        xmlfile = open('files/DELENS.xml', 'r')
        body = xmlfile.read()

        try:
            response = requests.request("POST", udrApi, headers=headers,
                                        data=body.format(tpno=tpno, DT=dt, SERIAL=serial))


            print(response.text)
            
            logger.info("Start : =========================================================================")
            logger.info(response.request.body)
            
            logger.info("Response : =================================")
            logger.info(response.text)
            logger.info("End : =========================================================================")
            
            root = ET.fromstring(response.content)
            for resultc in root.iter('ResultCode'):
                ResultCode = resultc.text

            for resultd in root.iter('ResultDescr'):
                ResultDesc = resultd.text

            return ResultCode+'#'+ResultDesc
        except Exception as e:
            return str(e)
