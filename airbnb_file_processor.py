from collections import Counter
from math import sqrt
import sys 

'''
This is an interactive program to parse and analyse data's of the Airbnb listing by A00288443.
We can chose one property from Review or Price.
This program will show the MAX, MIN, MEAN, MEDIAN, MODE and STANDARD DEVIATION for that property
We can also see the the Correlation between Price and Ratings.
'''

filename = input("Enter the name of the file which contains Airbnb listing: ")
# create an empty list for review_scores_rating and price_list
airbnb_properties_name = []
review_scores_rating_list = []
price_list = []
#Variable to store airbnb_properties without price or review_score
airbnb_properties_without_price = 0
airbnb_properties_without_review_scores_rating = 0

try:
    # Open the file in read mode
    with open(filename) as airbnb_details_file:
        # Read in each line, one at a time
        count = 0;
        for line in airbnb_details_file:
            try:
                 #Skipping the header
                 if count == 0:
                    count = 1
                    continue
                #Parse the data in CSV file
                 else:
                    # Amenities column is consists of list  or empty list.
                    # Check if CSV entry contains amenities list
                    if ',"["' in line:
                        start_list = line.index(',"["')
                        end_list = line.index('"]"')
                        amenities = line[start_list:end_list+3]
                    # Check if CSV entry contains empty amenities list    
                    else:
                        start_list = line.index('[')
                        end_list = line.index(']')
                        amenities = line[start_list:end_list+1]
                    #Remove aminities from CSV row so that we don't have extra comma(",") when we parse it.    
                    line = line.replace(amenities, " ").strip()
                    #Split the row
                    bnb_properties = line.split(",")
                    #This is to cover the scenario where each value of CSV is separted by comma and
                    #none of the data conatins extra comma.
                    # We are using only name, review_scores_rating and price in this program but we are parsing all data.
                    if len(bnb_properties) == 15:
                        id = int(bnb_properties[0])
                        listing_url = bnb_properties[1]
                        name = bnb_properties[2]
                        host_identity_verified = bnb_properties[3]
                        room_type = bnb_properties[4]
                        accommodates = bnb_properties[5]
                        bedrooms = bnb_properties[6]
                        # If there is no data in price, we are setting it to zero
                        # If there is data, replace first '$' symbol by empty string and then we will remove any space.
                        price = float(bnb_properties[7].replace('$', '').strip()) if bnb_properties[7] else 0
                        minimum_nights = bnb_properties[8]
                        number_of_reviews = bnb_properties[9]
                        last_review = bnb_properties[10]
                        #If data is blank set it to 0 otherwise convert value to integer and set it to review_scores_rating
                        review_scores_rating = int(bnb_properties[11]) if bnb_properties[11] else 0
                        instant_bookable = bnb_properties[12]
                        region_name = bnb_properties[13]
                        region_parent_name = bnb_properties[14]
                    #This is to cover the scenario where name contains one ","
                    elif len(bnb_properties) == 16:
                        id = bnb_properties[0]
                        listing_url = bnb_properties[1]
                        name = bnb_properties[2] + ", " + bnb_properties[3]
                        host_identity_verified = bnb_properties[4]
                        room_type =  bnb_properties[5]
                        accommodates = bnb_properties[6]
                        bedrooms = bnb_properties[7]
                        # If there is no data in price, we are setting it to zero
                        # If there is data, replace first '$' symbol by empty string and then we will remove any space.
                        price = float(bnb_properties[8].replace('$', '').strip()) if bnb_properties[8] else 0
                        minimum_nights = bnb_properties[9]
                        number_of_reviews = bnb_properties[10]
                        last_review = bnb_properties[11]
                        #If data is blank set it to 0 otherwise convert value to integer and set it to review_scores_rating
                        review_scores_rating = int(bnb_properties[12]) if bnb_properties[12] else 0
                        instant_bookable = bnb_properties[13]
                        region_name = bnb_properties[14]
                        region_parent_name = bnb_properties[15]
                    #This is to cover the scenario where name contains two ","
                    elif len(bnb_properties) == 17:
                        id = int(bnb_properties[0])
                        listing_url = bnb_properties[1]
                        name = bnb_properties[2] + ", " + bnb_properties[3]+", " + bnb_properties[4]
                        host_identity_verified = bnb_properties[5]
                        room_type =  bnb_properties[6]
                        accommodates = bnb_properties[7]
                        bedrooms = bnb_properties[8]
                        # If there is no data in price, we are setting it to zero
                        # If there is data, replace first '$' symbol by empty string and then we will remove any space.
                        price = float(bnb_properties[9].replace('$', '').strip()) if bnb_properties[9] else 0
                        minimum_nights = bnb_properties[10]
                        number_of_reviews = bnb_properties[11]
                        last_review = bnb_properties[12]
                        #If data is blank set it to 0 otherwise convert value to integer and set it to review_scores_rating
                        review_scores_rating = int(bnb_properties[13]) if bnb_properties[13] else 0
                        instant_bookable = bnb_properties[14]
                        region_name = bnb_properties[15]
                        region_parent_name = bnb_properties[16]
                    #This is to cover the scenario where name contains three ","
                    elif len(bnb_properties) == 18:
                        id = int(bnb_properties[0])
                        listing_url = bnb_properties[1]
                        name = bnb_properties[2] + ", " + bnb_properties[3]+", " + bnb_properties[4]+", " + bnb_properties[5]
                        host_identity_verified = bnb_properties[6]
                        room_type =  bnb_properties[7]
                        accommodates = bnb_properties[8]
                        bedrooms = bnb_properties[9]
                        # If there is no data in price, we are setting it to zero
                        # If there is data, replace first '$' symbol by empty string and then we will remove any space.
                        price = float(bnb_properties[10].replace('$', '').strip()) if bnb_properties[10] else 0
                        minimum_nights = bnb_properties[11]
                        number_of_reviews = bnb_properties[12]
                        last_review = bnb_properties[13]
                        #If data is blank set it to 0 otherwise convert value to integer and set it to review_scores_rating
                        review_scores_rating = int(bnb_properties[14]) if bnb_properties[14] else 0
                        instant_bookable = bnb_properties[15]
                        region_name = bnb_properties[16]
                        region_parent_name = bnb_properties[17]
                    #This is exception/error scenario where we have more than 18 "," in row
                    else:
                        print("ERROR : Number of ',' is more than 18" + " ...." + str(len(bnb_properties)) )
                        print(line)
                        price = 0
                        review_scores_rating = 0
                    # Adding name to property name list   
                    airbnb_properties_name.append(name)
                    #Add review_scrore in review_scores_rating_list
                    if review_scores_rating :
                        review_scores_rating_list.append(review_scores_rating)
                    else:
                        airbnb_properties_without_review_scores_rating +=1
                    #Add price in the price list
                    if price :
                        price_list.append(price)
                    else:
                        airbnb_properties_without_price += 1
            #Handle exception if there is any value error.
            except ValueError as v_error:
                print("ERROR:Line in incorrect format:", line)
                print(v_error)
except FileNotFoundError:
    print("ERROR: Unable to open file", filename)
    sys.exit("ERROR: Unable to open file")
except PermissionError:
    print("ERROR: Not sufficient permission to open file : ", filename)
    sys.exit("ERROR: Not sufficient permission to open file")
except IsADirectoryError:
    print("ERROR: Provided file is a directory and not file : ", filename)
    sys.exit("ERROR: Provided file is a directory and not file")
    
# Create a file "Result.txt" or append the existing "Result.txt"
output_file = open('Result.txt', 'a')

#Text to identify new entry in the file
output_file.write("\n")
output_file.write("*"*80 + "\n")
output_file.write("*********************** New Execution of Program *******************************\n")
output_file.write("*"*80 + "\n")
output_file.write("\n")

#Informative information about the data e.g. total number of entry, number of entries which does not have price etc.
print(f"Number of Airbnb property in the provided file : {len(airbnb_properties_name)}")
output_file.write(f"Number of Airbnb property in the provided file : {len(airbnb_properties_name)} \n")
print(f"Number of Airbnb property which is missing price : {airbnb_properties_without_price}")
output_file.write(f"Number of Airbnb property which is missing price : {airbnb_properties_without_price}\n")
print(f"Number of Airbnb property which is missing review_scores_rating : {airbnb_properties_without_review_scores_rating}")
output_file.write(f"Number of Airbnb property which is missing review_scores_rating : {airbnb_properties_without_review_scores_rating}\n")
print("")
output_file.write("\n")
output_file.flush()

#Claculate Mean, Median, Mode and Standard deviation
while True:
    #In Console, a list of options will be displayed to the user
    print("-"*100)
    print("Please select one of the below options :")
    print("\t\"Price\" or \"P\" to anlayse Airbnb property prices")
    print("\t\"Rating\" or \"R\" to analyse rating provide to Airbnb property.")
    print("\t\"Correlation\" or \"C\" to find correlation between Airbnb property's price and it's rating.")
    print("\t\"Quit\" or \"Q\" to quit the program" )
    print("-"*100)

    user_selection = input("Plese enter you selection : ")
    print(f"You have selected : {user_selection}")
    output_file.write(f"You have selected : {user_selection}\n")
    print()
    output_file.write("\n")
    #If user select the price option, all details of price will be shown.
    if user_selection.lower() == "price" or  user_selection.lower() == "p":
        #Title of the analysis. Decorative string.
        print("#" * 80)
        output_file.write("#"*80 + "\n")
        print("############# Analysis of the prices for Airbnb Properties  ####################")
        output_file.write("########## Analysis of the prices for Airbnb Properties  #######################\n")
        print("#" * 80)
        output_file.write("#"* 80 + "\n")
        print()
        output_file.write("\n")
        
        #Number of values (records), maximum, minimum value of price
        print(f"Number of price entry : {len(price_list)}")
        output_file.write(f"Number of price entry : {len(price_list)} \n")
        print(f"Highest price of Airbnb property : ${max(price_list): .2f}")
        output_file.write(f"Highest price of Airbnb property : ${max(price_list): .2f}\n")
        print(f"Lower price of Airbnb property : ${min(price_list): .2f}")
        output_file.write(f"Lower price of Airbnb property : ${min(price_list): .2f} \n")
        
        #Calculate the Mean of the prices
        number_of_entry_in_price_list = len(price_list)
        sum_of_all_elements_in_price_list = sum(price_list)
        mean_price = sum_of_all_elements_in_price_list / number_of_entry_in_price_list
        print(f"Mean/Average price of Airbnb property : ${mean_price:.2f}")
        output_file.write(f"Mean/Average price of Airbnb property : ${mean_price:.2f}\n")
        
        #Calculate the Median of the prices
        price_list.sort()
        if number_of_entry_in_price_list % 2 == 0:
            median_of_price = (price_list[number_of_entry_in_price_list//2] 
                               + price_list[number_of_entry_in_price_list//2 - 1])/2
        else:
            median_of_price = price_list[number_of_entry_in_price_list//2]
        print(f"Median of the prices of Airbnb property is: ${median_of_price:.2f}")
        output_file.write(f"Median of the prices of Airbnb property is: ${median_of_price:.2f}\n")
        
        #Calculate the Mode of the prices
        price_list_counter = Counter(price_list)
        mode_price = [k for k, v in price_list_counter.items() if v == price_list_counter.most_common(1)[0][1]]
        print(f"Mode of the prices of Airbnb property is : {str(mode_price)}" )
        output_file.write(f"Mode of the prices of Airbnb property is : {str(mode_price)}")
        
        #Standard Deviation of prices
        #Create a list of the deviations squared
        deviations_for_price = [(value - mean_price) ** 2 for value in price_list ]
        #Calculate the standard deviation
        std_deviation_for_price = sqrt(sum(deviations_for_price)/(len(price_list)-1))
        print(f"Standard Deviation for prices of Airbnb property is: {std_deviation_for_price:.2f} ")
        output_file.write(f"Standard Deviation for prices of Airbnb property is: {std_deviation_for_price:.2f} \n")
        # Decorative string
        print()
        output_file.write("\n")
        print("#" * 80)
        output_file.write("#" * 80 + "\n")
        print()    
        output_file.write("\n")
        output_file.flush()
    #If user selects rating, all analysis of rating will be shown to user.
    elif user_selection.lower() == "rating" or  user_selection.lower() == "r":
        #Title of the analysis. Decorative string.
        print("#" * 80)
        output_file.write("#" * 80 + "\n")
        print("########## Analysis of the Ratings for Airbnb Properties  ######################")
        output_file.write("########## Analysis of the Ratings for Airbnb Properties  ######################\n")
        print("#" * 80)
        output_file.write("#" * 80 + "\n")
        print()
        output_file.write("\n")
        #Number of values (records), maximum, minimum value of rating
        print(f"Number of review entry : {len(review_scores_rating_list)}")
        output_file.write(f"Number of review entry : {len(review_scores_rating_list)}\n")
        print(f"Highest Rated of Airbnb property : {max(review_scores_rating_list)}")
        output_file.write(f"Highest Rated of Airbnb property : {max(review_scores_rating_list)}\n")
        print(f"Lowest Rated of Airbnb property : {min(review_scores_rating_list)}")
        output_file.write(f"Lowest Rated of Airbnb property : {min(review_scores_rating_list)}\n")

        #Calculate the Mean of the review_score_rating
        number_of_review_scrore_rating = len(review_scores_rating_list)
        total_sum_of_review_scrore_rating = sum(review_scores_rating_list)
        mean_review_scrore_rating =  total_sum_of_review_scrore_rating / number_of_review_scrore_rating
        print(f"Mean/Average Rating for Airbnb property : {mean_review_scrore_rating:.2f}")
        output_file.write(f"Mean/Average Rating for Airbnb property : {mean_review_scrore_rating:.2f}\n")
        
        #Calculate the Median of the review_score_rating
        review_scores_rating_list.sort() 
        if number_of_review_scrore_rating % 2 == 0:  
            median_of_review_scrore_rating = (review_scores_rating_list[number_of_review_scrore_rating//2]  
                                              + review_scores_rating_list[number_of_review_scrore_rating//2 - 1])/2
        else: 
            median_of_review_scrore_rating = review_scores_rating_list[number_of_review_scrore_rating//2] 
        print(f"Median of the rating for Airbnb property : {median_of_review_scrore_rating:.2f}")
        output_file.write(f"Median of the rating for Airbnb property : {median_of_review_scrore_rating:.2f}\n")
        
        #Calculate the Mode of the rating
        review_scores_rating_list_counter = Counter(review_scores_rating_list)
        mode_review_scores_rating = [k for k, v in review_scores_rating_list_counter.items() 
                      if v == review_scores_rating_list_counter.most_common(1)[0][1]]
        print(f"Mode of the rating for Airbnb property : {mode_review_scores_rating}")
        output_file.write(f"Mode of the rating for Airbnb property : {mode_review_scores_rating}\n")
        #Standard Deviation in rating
        #Create a list of the deviations squared
        deviations_for_review_rating = [(value - mean_review_scrore_rating) ** 2 
                                        for value in review_scores_rating_list ]
        #Calculate the standard deviation
        std_dev_for_review_rating = sqrt(sum(deviations_for_review_rating)/(len(review_scores_rating_list)-1))
        print(f"Standard Deviation for rating for Airbnb property  : {std_dev_for_review_rating:.2f}")
        output_file.write(f"Standard Deviation for rating for Airbnb property  : {std_dev_for_review_rating:.2f}\n")
        print("#" * 80)
        output_file.write("#" * 80 + "\n")
        print()
        output_file.write("\n")
        output_file.flush()
    elif user_selection.lower() == "Correlation" or user_selection.lower() == "c":
        #Title of the analysis. Decorative string.
        print("#" * 80)
        output_file.write("#" * 80 + "\n")
        print("######### Correlation between Price and Ratings for Airbnb Properties  #########")
        output_file.write("######### Correlation between Price and Ratings for Airbnb Properties  #########\n")
        print("#" * 80)
        output_file.write("#" * 80 + "\n")
        print()
        output_file.write("\n")
        #Calculate the means
        price_mean = sum(price_list)/len(price_list)
        review_scores_rating_mean = sum(review_scores_rating_list)/len(review_scores_rating_list)
    
        #Cate a list of the deviations
        price_deviations = [ price - price_mean for price in price_list ]
        review_scores_rating_deviations = [ review_scores_rating - review_scores_rating_mean 
                                           for review_scores_rating in review_scores_rating_list ]
        
        #Create a list of the deviations multipled
        price_rating_deviations = [ price_mean*review_scores_rating_mean 
                                   for (price_mean,review_scores_rating_mean) 
                                   in zip(price_deviations,review_scores_rating_deviations)]
        
        #Create a list of the deviations squared
        price_square_deviations = [ (price - price_mean) ** 2 for price in price_list ]
        review_scores_rating_deviations = [ (review_scores_rating - review_scores_rating_mean) ** 2 
                                           for review_scores_rating in review_scores_rating_list ]
        
        #Calculate the correlation
        correlation = sum(price_rating_deviations)/(sqrt(sum(price_square_deviations))*(sqrt(sum(review_scores_rating_deviations))))
        
        print(f"Number of price entry: {len(price_list)}")
        output_file.write(f"Number of price entry: {len(price_list)}\n")
        print(f"Number of review_score entry: {len(review_scores_rating_list)}")
        output_file.write(f"Number of rating entry: {len(review_scores_rating_list)}\n")
        print(f"Correlation between price and rating: {correlation:.2f}")
        output_file.write(f"Correlation between price and rating: {correlation:.2f}\n")
        #Display the relationship type based on correlation value
        if correlation < 0.3 :
            print("The relationship between price and rating is very weak.")
            output_file.write("The relationship between price and rating is very weak.\n")
        elif 0.3 <= correlation <0.5 :
            print("The relationship between price and rating is Weak.")
            output_file.write("The relationship between price and rating is Weak.\n")
        elif 0.5 <= correlation < 0.7 :
            print("The relationship between price and rating is Moderate.")
            output_file.write("The relationship between price and rating is Moderate.\n")
        else:
            print("The relationship between price and rating is Strong.")
            output_file.write("The relationship between price and rating is Strong.\n")
        # Decorative string
        print("#" * 80)
        output_file.write("#" * 80 + "\n")
        print()
        output_file.write("\n")
        output_file.flush()
    #If user select 'Q' or 'Quit' we need teh break the file loop.        
    elif user_selection.lower() == "quit" or user_selection.lower() == "q":
        break
    #To handle invalid selection
    else:
        print("Invalid Input. Please enter the a valid input or Q/q to quit.")
        output_file.write("Invalid Input. Please enter the a valid input or Q/q to quit.\n")
        continue  
#Exit the program and close the output file
print("Thanks for using this application. \nAll output, which are dispalyed in console, are saved in Result.txt file.")
output_file.write("Thanks for using this application. \nAll output, which are dispalyed in console, are saved in Result.txt file.\n")
output_file.close()
