from BeautifulSoup import BeautifulStoneSoup

path = "/Users/suzy/Desktop/slot-filler-validation_db/syscombo/"

def readquerydata():
    fin_qrel = open(path+"KBP2012_english_SF_qrels","r")
    fin_slots = open(path+"KBP2012_english_SF_slot-list","r")
    fin_sfbefore = open(path+"sfbefore","r")
    fin_queries = open(path+"tac_2012_kbp_english_regular_slot_filling_evaluation_queries.xml","r")

    lines = fin_queries.readlines
    soup = BeautifulStoneSoup(fin_queries)
    #print soup.prettify()
    query= soup.findAll('query')
    #print query

    qid = []
    for item in query:
        temp = item['id']
        qid.append(temp)

    name = soup.findAll('name')
    enttype = soup.findAll('enttype')

    qname = []
    #list of query names
    for item in name:
        temp=str(item)
        temp = temp.replace("<name>","")
        temp = temp.replace("</name>","")
        qname.append(temp)
    #print qname

    etype = []
    #list of entity types
    for item in enttype:
        temp=str(item)
        temp = temp.replace("<enttype>","")
        temp = temp.replace("</enttype>","")
        etype.append(temp)
    #print etype

    eID = []
    #list of entity IDs
    for item in qid:
        temp=str(item)
        eID.append(temp)
    #print eID

    fin_qrel.close()
    fin_slots.close()
    fin_sfbefore.close()
    fin_queries.close()

    return [eID,qname,etype]

def readqueryslottemplate():
    fin_slots = open(path+"KBP2012_english_SF_slot-list","r")

    query_slots = {}
    keys = []
    values = []
    for line in fin_slots:
        temp = line.strip()
        #print temp
        temp = temp.split(":")
        keys.append(temp[0])
        value = temp[1]+":"+temp[2]
        values.append(value)
    return [keys,values]


        









