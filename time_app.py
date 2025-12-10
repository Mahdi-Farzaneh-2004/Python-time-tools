from datetime import datetime , timedelta
from datetime import date
from datetime import datetime
import datetime
import jdatetime
class Time:
    def date(self):
        print("✅DATE")
        date=datetime.datetime.now()
        date1=date.strftime("Result: %Y-%m-%d")
        print(f"Result: {date1}")
            
    def time(self):
        print("✅TIME")
        time=datetime.datetime.now()
        time1=time.strftime("Result: %H:%M:%S")
        print(f"Result: {time1}")
    
    def time_calculation(self):
        print("✅Time calculation")
        while True:
            try:
                print("Inside time calculation you can enter values like these: \n1.Add \n2.Subtract")
                input_time_calculation=int(input("Enter choise: "))
                if input_time_calculation == 1:
                    print("1.second \n2.minutes \n3.hours \n4.day")
                    input_add=int(input("Enter the base value: "))
                    now_add=datetime.datetime.now()

                    if input_add == 1:
                        input_second_add=int(input("Enter the amount you want to add: "))
                        future_second= now_add+timedelta(seconds=input_second_add)
                        print(future_second.strftime("Result: %H:%M:%S"))
                    
                    elif input_add == 2:
                        input_minutes_add=int(input("Enter the amount you want to add: "))
                        future_minutes = now_add+timedelta(minutes=input_minutes_add)
                        print(future_minutes.strftime("Result: %H:%M:%S"))
                
                    elif input_add == 3:
                        input_hours_add=int(input("Enter the amount you want to add: "))
                        future_hours = now_add+timedelta(hours=input_hours_add)
                        print(future_hours.strftime("Result: %H:%M:%S"))

                    elif input_add == 4:
                        input_day_add=int(input("Enter the amount you want to add: "))
                        future_day = now_add+timedelta(days=input_day_add)
                        print(future_day.strftime("Result: %Y-%m-%d"))

                elif input_time_calculation == 2:
                    print("1.second \n2.minutes \n3.hours \n4.day")
                    input_subtract=int(input("Enter the base value: "))
                    now_subtract=datetime.datetime.now()
              
                    if input_subtract == 1:
                        input_second_add=int(input("Enter the amount you want to add: "))
                        past_second=now_subtract-timedelta(seconds=input_second_add)
                        print(past_second.strftime("Result: %H:%M:%S"))
            
                    elif input_subtract == 2:
                        input_minutes_add=int(input("Enter the amount you want to add: "))
                        past_minutes=now_subtract-timedelta(minutes=input_minutes_add)
                        print(past_minutes.strftime("Result: %H:%M:%S"))
            
                    elif input_subtract == 3:
                        input_hours_add=int(input("Enter the amount you want to add: "))
                        past_hours=now_subtract-timedelta(hours=input_hours_add)
                        print(past_hours.strftime("Result: %H:%M:%S"))
                
                    elif input_subtract == 4:
                        input_day_add=int(input("Enter the amount you want to add: "))
                        past_day=now_subtract-timedelta(days=input_day_add)
                        print(past_day.strftime("Result: %Y-%m-%d"))
            except:
                print("please enter correct value")
            
    def Stopwatch(self):
        print("✅Stopwatch")
        print("when want start type [start]")
        print("when want end type [end]")
        while True:
            input_Stopwatch=str(input("Enter: ")).lower()
            if input_Stopwatch == "start":
                start=datetime.datetime.now()
            if input_Stopwatch == "end":
                end=datetime.datetime.now()
                print(f"Result: {end-start}")
                break
            
    def age_calculation(self):
        print("✅Age calculation")
        input_age_calculation=int(input("Enter your age year: "))
        now=date.today()
        age=now.year-input_age_calculation
        print(f"Result: {age}")
             
    def age_comparison(self):
        print("✅ Age comparison")
        try:
            dob1 = input("Enter first date of birth (YYYY-MM-DD): ").strip()
            dob2 = input("Enter second date of birth (YYYY-MM-DD): ").strip()

            d1 = datetime.datetime.strptime(dob1, "%Y-%m-%d").date()
            d2 = datetime.datetime.strptime(dob2, "%Y-%m-%d").date()

            if d1 < d2:
                print("First person is older.")
            elif d1 > d2:
                print("Second person is older.")
            else:
                print("Both have the same age.")
        except ValueError:
            print("Please enter dates in YYYY-MM-DD format (e.g. 1990-05-23).")
    def mailad_shamsi(self):
        print("✅Converting the solar year to the Gregorian year")
        input_miladi_yaer=int(input("Enter correct year: "))
        input_miladi_month=int(input("Enter correct month: "))
        input_miladi_day=int(input("Enter correct day: "))
        miladi = datetime.datetime(input_miladi_yaer,input_miladi_month,input_miladi_day)
        shamsi = jdatetime.date.fromgregorian(date=miladi)
        print(f"Result: {shamsi}")
        
    def shamsi_milad(self):
        print("✅Converting the Gregorian year to the solar year")
        input_shamsi_yaer=int(input("Enter correct year: "))
        input_shamsi_month=int(input("Enter correct month: "))
        input_shamsi_day=int(input("Enter correct day: "))
        shamsi = jdatetime.date(input_shamsi_yaer,input_shamsi_month,input_shamsi_day)
        miladi = shamsi.togregorian()
        print(f"Result: {miladi}")

    
def main():
    time = Time()
    while True:
        try:
            print("-----Welcome----- \n1.Date and Time now \n2.Time calculation \n3.Stopwatch \n4.Age calculation \n5.Age comparison \n6.Converting the solar year to the Gregorian year \n7.Converting the Gregorian year to the solar year")
            main_input=int(input("Enter your choise: "))
            if main_input == 1:
                print("1.Time \n2.Date")
                input_date_time_now=int(input("Enetr your choise: "))
                if input_date_time_now == 1:
                    time.time()
                elif input_date_time_now == 2:
                    time.date()
            elif main_input == 2:
                time.time_calculation()
            elif main_input == 3:
                time.Stopwatch()
            elif main_input == 4:
                time.age_calculation()
            elif main_input == 5:
                time.age_comparison()
            elif main_input == 6:
                time.mailad_shamsi()
            elif main_input == 7:
                time.shamsi_milad()
        except:
            print("❌Please Enter correct value")
    
if __name__ == "__main__":
    main()
