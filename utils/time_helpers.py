from datetime import datetime
import pytz


def utc_now():
    # Attribution: stackoverflow
    return datetime.now().replace(tzinfo=pytz.utc)
