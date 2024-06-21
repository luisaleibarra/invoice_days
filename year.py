import datetime

# Define the holidays
holidays = [
    datetime.date(2024, 1, 1),
    datetime.date(2024, 5, 27),
    datetime.date(2024, 6, 19),
    datetime.date(2024, 7, 4),
    datetime.date(2024, 9, 2),
    datetime.date(2024, 11, 28),
    datetime.date(2024, 11, 29),
    datetime.date(2024, 12, 25)
]

# Initialize the start date and end date
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 31)

# Initialize the invoice day number and the combined list
invoice_day_number = 0
combined_days = []

# Iterate through each day of the year
current_date = start_date
while current_date <= end_date:
    if current_date.weekday() >= 5 or current_date in holidays:
        combined_days.append((current_date.strftime('%m/%d/%Y'), 'OFF'))
    else:
        combined_days.append((current_date.strftime('%m/%d/%Y'), str(invoice_day_number)))
        invoice_day_number += 1
    current_date += datetime.timedelta(days=1)

# Print the combined list
for date, status in combined_days:
    print(f"{date}: {status}")
