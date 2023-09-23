import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "1BVtsOKUBu2Zb33j8bN2uOJadONFT2AAmBep-XS8cYxDdr9_AlgXDWkWkSpmfL-FEbfjczsO1zeQHLqNBTmVnsO7dmVKn08M0zq_z566gQP8YrRqdPsFwGRdvRABRbYPu7dQr0PEUQsetIhhOuBVoQv8_6HWduxxNg-DUsNgGp_rKJg9NXEagzbbQRJH_rDqaPy7aQakS7Qs2CT62Cn-o_3qZMd0Q_0I4MwS5cZ1UjVDrVqCKEy22SEHmlqTOUFBY1MYHZhCKOrYwuUWUmaZWTuV038voumwWT3vGfYomfYRmPyodw1bQ1RFujLQiqA22bZW73HFnR-Vkt0fAuYaaQSzClWyDMgE")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", ""))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
