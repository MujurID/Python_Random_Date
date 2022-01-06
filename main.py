import random
from datetime import timedelta, datetime

start = datetime(2019,1,1,0,0,0).replace(microsecond=0)
end = datetime(2019,12,31,23,59,59).replace(microsecond=0)

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

random_dates = random_date(start, end).isoformat() #https://stackoverflow.com/a/65749164
print(random_dates)
#output: 2019-03-03T16:52:28
