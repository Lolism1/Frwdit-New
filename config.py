#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", "28449014"))
    API_HASH = os.environ.get("API_HASH", "4244ff69cb4941184e47af4ef68e06e2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5729549748:AAG_xtYec6UuHkmzQTb8VKG952GB-7hFx4c") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "🔰Join Now : @MoviezTalkiez")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", "1206047582")
    SESSION = os.environ.get("SESSION", "BQCKRGpLTeee3J6T9q1ErY1dbkqv30OD6wx-6sp4dff_xOb3_1xwS0PRVm3LYAU54nZfdshRVQc64aFZgAhiPU_aC03EnldJc9lDyPLhpBrEvSlitutwmbGdYi89kXroISm7EvskKdxhOo6eqbB3Ij0B_ZJBpkm_DLP47Kcs2ImzX_4AqASjXLKPDGz3cB0WAkXxxGAPE-ISiHGseDyEuNxfcYmPnQh8DKnQb-i4GYdaBv-h4zfuIG9fRjLBuH3NfBjz3P6-6PI1tU803si60EfgoA9ObQCTbNn433_5szh0WN08u59R-yOLtCxI4m7Hg2eQRI8CwjExWuQTN1-THUrxR-LTXgA")
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
