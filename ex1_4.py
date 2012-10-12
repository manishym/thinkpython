def km_to_mile(km):
    ''' (number) -> float
    This function returns number of miles in km specified
    km_to_mile(10) -> 6.25
    km_to_mile(1.6) -> 1.0
    '''
    return km/1.6


def average_speed(kms_run, h, m, s):
    ''' (number, number, number, number) -> float
    gives the average speed give kms run and time taken.
    average speed will be in mph
    avarage_speed(10, 0, 30, 45) -> 12.195121951219512
    average_speed(50, 4, 20, 5) -> 7.209227811598847
    '''
    time_as_float = time_to_float(h, m, s)
    return km_to_mile (kms_run) / time_as_float


def time_to_float (h,m,s):
    '''(number, number, number) -> float
    Converts time given in hour, min and seconds into float time in hours
    time_to_float(1, 30, 0) -> 1.50
    time_to_float(2,15,0) -> 2.25
    '''
    return h + m/60 + s/3600
