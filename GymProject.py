

print('John' ',' 'Raj' ',' 'Anit' ',' 'Sid' ',' 'Pratik' ',' 'Pavn' ','
      'Ash' ',' 'Mangesh' ',' 'Aniket' ',' 'Preeti' ',' 'Lavanya' ',' 'Praju')

print("Which Client Info You Have: ")
clientname = input()
while (True):
    if clientname == "John":
        print('John Buy Golden Membership', 'For 6 months')
        print('Jioning Date : 1.1.2022', 'Vaild: 30.6.2022')

        break

    elif clientname == "Raj":
        print('Raj Buy Golden Membership', 'For 9 months')
        print('Jioning Date : 1.9.2021', 'Vaild: 30.5.2022')

        break
    elif clientname == "Anit":
        print('Anit Buy Golden Membership', 'For 3 months')
        print('Jioning Date : 1.11.2021', 'Vaild: 30.2.2022')

        break

    elif clientname == "Sid":
        print('Sid Buy Golden Membership', 'For 12 months')
        print('Jioning Date : 1.1.2022', 'Vaild: 30.12.2022')

        break
    elif clientname == "Pratik":
        print('Pratik Buy Golden Membership', 'For 8 months')
        print('Jioning Date : 5.12.2021', 'Vaild: 30.7.2022')

        break
    elif clientname == "Pavn":
        print('Pavn Buy Golden Membership', 'For 5 months')
        print('Jioning Date : 7.1.2022', 'Vaild: 30.5.2022')

        break

    elif clientname == "Ash":
        print('Ash Buy Golden Membership', 'For 6 months')
        print('Jioning Date : 1.1.2022', 'Vaild: 30.5.2022')

        break

    elif clientname == "Mangesh":
        print('Mangesh Buy Golden Membership', 'For 6 months')
        print('Jioning Date : 1.1.2022', 'Vaild: 30.5.2022')

        break

    elif clientname == "Aniket":
        print('Aniket Buy Golden Membership', 'For 12 months')
        print('Jioning Date : 1.1.2022', 'Vaild: 31.12.2022')

        break
    elif clientname == "Preeti":
        print('Preeti Buy Golden Membership', 'For 3 months')
        print('Jioning Date : 3.12.2021', 'Vaild: 30.3.2022')

        break
    elif clientname== "Lavanya":
        print('Lavanya Buy Golden Membership', 'For 4 months')
        print('Jioning Date : 4.2.2022', 'Vaild: 30.5.2022')

        break

    elif clientname == "Praju":
        print('Praju Buy Golden Membership', 'For 1 months')
        print('Jioning Date : 10.2.2022', 'Vaild: 30.2.2022')

        break

    else:
        print("Enter Client Name in List")
        break

#User Time Table ROUTIN

day= {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Satruday"}
print(day)
choice = input()

while(True):
    if choice == "Monday":
        print("Today's workout is Biceps")
        print("After workerout diet is oats, 2 fruites, milk")
        break

    elif choice == "Tuesday":
        print("Today's workout is Shoulder")
        print("After workerout diet Mondayet is chapati, egg")
        break

    elif choice == "Wednesday":
        print("Today's workout is Shoulder")
        print("After workerout diet Mondayet is chapati, paneer")
        break


    elif choice == "Thursday":
        print("Today's workout is Back")
        print("After workerout diet is oats, 2 fruites, milk")
        break

    elif choice == "Friday":
        print("Today's workout is Shoulder")
        print("After workerout diet Friday is chapati, paneer")

    elif choice == "Satruday":
        print("Today's workout is legs")
        print("After workerout diet is eggs/meat")
        break
    else:
        print("Enter today's day")
        break
    continue
print(choice)














