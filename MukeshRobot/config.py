class Config(object):
    LOGGER = True
    API_ID =016675873641 
    API_HASH = "3fc2b371f4fbb0166758736414d8be92"
    TOKEN = "7010022450:AAEixXqUCOTJSkH3GiX8JSkvJEJRRbXjjL4"  
    OWNER_ID=1266240012
    
    SUPPORT_CHAT = "TheSuperiorDynasty" 
    START_IMG = "https://graph.org/file/e7a7c584fc293ed519433.jpg"
    EVENT_LOGS = (-1002158639980)
    MONGO_DB_URI= "mongodb+srv://Unknown:Unknown@unknown.2qz5dea.mongodb.net/?retryWrites=true&w=majority&appName=Unknown"
   
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "UXBLBVF519U1NRU7"
    )
    TIME_API_KEY = "2GXD3SEFWOAI"

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
