

# Author Mitanshi KetulPandya, Kavya Nandishbhai Shah, Chintan Jayprakash Patel
# Version 2023-12-11




import appointment as ap

def weekly_calendar():
    calendar = []
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    for day in days_of_week:
        for hour in range(9, 17):
            appointment = ap.Appointment(day, hour)
            calendar.append(appointment)

    return calendar

def scheduled_appointments(filename, calendar):
        count = 0
        opening_file = open(filename, 'r')
        lines = opening_file.readlines()
        for line in lines:
            values = line.strip().split(',')
            day_of_week = values[3]
            start_time_hour = int(values[4])
            appointment = find_appointment_by_time(calendar, day_of_week, start_time_hour)
            if appointment:
                appointment.schedule(values[0], values[1], int(values[2]))
                count +=1
        print(f'{count} previously scheduled appointments have been loaded')


def checking_booked_slot(calendar, day, start_hour):
    for appointment in calendar:
        if appointment.get_day_of_week() == day and appointment.get_start_time_hour() == start_hour and appointment.get_client_name() != "":
            return True
    return False

def print_menu():
    print("\n")
    print("Jojo's Hair Salon Appointment Manager")
    print("=" * 37)
    print("1) Schedule an appointment")
    print("2) Find appointment by name")
    print("3) Print calendar for a specific day")
    print("4) Cancel an appointment")
    print("9) Exit the system")
    

    return input("Enter your selection: ")

def find_appointment_by_time(calendar, day, start_hour):
    for appointment in calendar:
        if appointment.get_day_of_week() == day and appointment.get_start_time_hour() == start_hour:
            return appointment
    return None

def show_appointments_by_name(calendar, name):
    for appointment in calendar:
        if name.lower() in appointment.get_client_name().lower():
            print(appointment)
    



def show_appointments_by_day(calendar, day):

    print(f"Appointments for {day.capitalize()}\n")
    
    print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name",
        "Phone", "Day", "Start", "End", "Type"))
   
    print("-" * 80)

    for appointment in calendar:
        if appointment.get_day_of_week().lower() == day.lower():
            client_name = appointment.get_client_name() if appointment.get_client_name() else " "
            client_phone = appointment.get_client_phone() if appointment.get_client_phone() else " "
            start_time = f"{appointment.get_start_time_hour():02d}:00"
            end_time = f"{appointment.get_start_time_hour() + 1:02d}:00"  
            appt_type = appointment.get_appt_type_desc() if appointment.get_client_name() else "Available"
            print(f'{client_name:16} {client_phone:>15} {day.capitalize():>8} - {start_time:>8} {end_time:>9} {appt_type:>20}')





def save_scheduled_appointments(calendar, file_name):
    count = 0
 
    if file_name == "appointments1.csv":
        yes_no = input('File already exist. Do you want to overwrite it (Y/N): ').upper()
        if yes_no == 'N':
            file_name = input('Enter file name: ')
            opening_new_file = open(file_name, 'w')
            for appointment_obj in calendar:
              if appointment_obj.get_appt_type() != 0:
                opening_new_file.write(ap.Appointment.format_record(appointment_obj) + '\n')
                count += 1
            print(f'{count} scheduled appointments have been saved')

        else:
             opening_new_file = open(file_name, 'w')
             for appointment_obj in calendar:
               if appointment_obj.get_appt_type() != 0:
                opening_new_file.write(ap.Appointment.format_record(appointment_obj) + '\n')
                count += 1
             print(f'{count} scheduled appointments have been saved')

    else:
        opening_new_file = open(file_name, 'w')
        for appointment_obj in calendar:
            if appointment_obj.get_appt_type() != 0:
                opening_new_file.write(ap.Appointment.format_record(appointment_obj) + '\n')
                count += 1
        print(f'{count} scheduled appointments have been saved')



def main():
    calendar = weekly_calendar()
    
 
    print("Starting the Appointment Manager System")
    print("Weekly calendar created")
    load_choice = input("Would you like to load previously scheduled appointments from a file (Y/N)? ").lower()
    if load_choice == 'y':
         file_name = input("Enter appointment filename: ")
         if file_name == 'appointments1.csv':
           scheduled_appointments(file_name, calendar)
         else:
          file_name = input("File not found. Re-enter appointment filename: ")
    option = print_menu()
             
             
        

    
    
    while option != '9':
        match option:
            case '1':
                print("\n** Schedule an appointment **")
                day = input("What day: ").capitalize()
                start_hour_str = input("Enter start hour (24 hour clock): ")
                if start_hour_str.isdigit() and 0 <= int(start_hour_str) <= 23:
                   start_hour = int(start_hour_str)
                   appointment = find_appointment_by_time(calendar, day, start_hour)
                
                   if checking_booked_slot(calendar, day, start_hour):
                      print("Sorry that time slot is booked already!")
                      option = print_menu()
                   elif appointment:
                      client_name = input("Client Name: ").capitalize()
                      client_phone = input("Client Phone: ")
                      print("Appointment types\n1: Mens Cut $50, 2: Ladies Cut $80, 3: Mens Colouring $50, 4: Ladies Colouring $120")

                      appt_type_str = input("Type of Appointment: ")
                      if appt_type_str in ['1', '2', '3', '4']:
                        appt_type = int(appt_type_str)
                        appointment.schedule(client_name, client_phone, appt_type)
                        print(f"OK, {client_name}'s appointment is scheduled!")
                        option = print_menu()
                      else:
                        print("Sorry that is not a valid appointment type!")
                        option = print_menu()
                   else:
                    print("Sorry that time slot is not in the weekly calendar!")
                    option = print_menu()
            
            case '2':
                print("\n** Find appointment by name **")
                client_name = input("Enter Client Name: ").capitalize()
                found_appointments = False
                print("Appointment for "+ client_name)  
                print("\n\n{:20s}{:15s}{:10s}{:10s}{:10s}{:20s}".format("Client Name","Phone", "Day", "Start", "End", "Type"))
                # print(f"\n{'Client Name'.ljust(20)} {'Phone'.ljust(15)} {'Day'.ljust(10)} {'Start'.ljust(10)} {'End'.ljust(10)} {'Type'}")
                print("-" * 80)
                for appointment in calendar:
                  
                  if client_name in appointment.get_client_name().capitalize():
                  
                    print(appointment)
                    
                    found_appointments = True
                
                if not found_appointments:
                    
                    print("No appointments found.")
                 
                option = print_menu()
            case '3':
                print("\n** Print calendar for a specific day **")
                day = input("Enter day of week: ")
                show_appointments_by_day(calendar, day)
                option = print_menu()
            case '4':
                    print("\n** Cancel an appointment **")
                    day = input("What day: ").capitalize()
                    start_hour = int(input("Enter start hour (24 hour clock): "))
                    appointment = find_appointment_by_time(calendar, day, start_hour)

                    if appointment and appointment.get_client_name():  
                       client_name = appointment.get_client_name()  
                       appointment.cancel()
                       print(f"Appointment: {day} {start_hour:02d}:00 - {start_hour + 1:02d}:00 for {client_name} has been cancelled!")
                       option = print_menu()
                    elif appointment:  
                       print(f"That time slot isn't booked and doesn't need to be cancelled")
                       option = print_menu()
                    else:  
                       print("Sorry, that time slot is not in the weekly calendar!")
                       option = print_menu()
    print('\n** Exit the system **')
    saving_data = input('Would you like to save all scheduled appointments to a file (Y/N)?').upper()
    file_name = input('Enter appointment filename: ')
    if saving_data != 'N':
        save_scheduled_appointments(calendar, file_name)
        print('Good Bye')
    else:
        print('Good Bye!')









if __name__ == "__main__":
    main()
