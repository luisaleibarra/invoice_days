import datetime

# Define the holidays for the year 2024
holidays = [
    datetime.date(2024, 1, 1),   # New Year's Day
    datetime.date(2024, 5, 27),  # Memorial Day
    datetime.date(2024, 6, 19),  # Juneteenth
    datetime.date(2024, 7, 4),   # Independence Day
    datetime.date(2024, 9, 2),   # Labor Day
    datetime.date(2024, 11, 28), # Thanksgiving Day
    datetime.date(2024, 11, 29), # Day after Thanksgiving
    datetime.date(2024, 12, 25)  # Christmas Day
]

# Initialize the start date and end date for the whole year
start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 31)

# Initialize the invoice day number and the combined list
invoice_day_number = 0
combined_days = []

# Function to determine if a date is a holiday or weekend
def is_off_day(date):
    return date.weekday() >= 5 or date in holidays

# Generate days for the whole year
current_date = start_date
while current_date <= end_date:
    if is_off_day(current_date):
        combined_days.append((current_date.strftime('%m/%d/%Y'), 'OFF'))
    else:
        # Check for the start of each quarter to reset invoice_day_number
        if current_date.month in [1, 4, 7, 10] and current_date.day == 1:
            invoice_day_number = 0
        combined_days.append((current_date.strftime('%m/%d/%Y'), str(invoice_day_number)))
        invoice_day_number += 1
    current_date += datetime.timedelta(days=1)

# Print the combined list
for date, status in combined_days:
    print(f"{date}: {status}")
