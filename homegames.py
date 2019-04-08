# variable for all lines that have titles
# exclude all title lines that start with Boston Red Sox
wanted_lines = 'X-GOOGLE-CALENDAR-CONTENT-TITLE:⚾'
unwanted_lines = 'X-GOOGLE-CALENDAR-CONTENT-TITLE:⚾️ Boston Red Sox @'

#empty list to hold line number of each home game title
title_line_numbers = []

# empty list to hold range of line numbers for each home game
event_line_numbers = []

# add .ics opening line numbers
opening_lines = range(8)
for i in opening_lines:
    event_line_numbers.append(i)

# find line number of each home game title and append to list
with open('RedSox_AllGames.ics', 'r') as old_file:
    for i, line in enumerate(old_file, 1):
        if line.startswith(wanted_lines) and not line.startswith(unwanted_lines):
            title_line_numbers.append(i)

# find line numbers related to each game before/after title line and append to list
for i in title_line_numbers:
    n = range(i-5, i+26)
    for j in n:
        event_line_numbers.append(j)

# create new file for home games
with open("RedSox_HomeGames.ics", "w") as new_file:

    #read lines in original file and write all lines whose number is in list
    with open('RedSox_AllGames.ics', 'r') as old_file:
        for i, line in enumerate(old_file, 1):
            if i in event_line_numbers:
                new_file.write(line)
    
    # write .ics closing line
    new_file.write('END:VCALENDAR')