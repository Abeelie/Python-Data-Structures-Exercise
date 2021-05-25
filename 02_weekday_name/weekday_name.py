def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 
            4: "Thursday", 5: "Friday", 6: "Saturday"}

    if day_of_week < 1 or day_of_week > 7:
        return None
    else:
    	return days[day_of_week]



print(weekday_name(0))
print(weekday_name(9))