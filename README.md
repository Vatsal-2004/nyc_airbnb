This is a detailed analysis on the NYC AirBnb Market

Introduction:  
Since 2008, guests and hosts have used Airbnb to expand on traveling possibilities and present a more unique, personalized way of experiencing the world.  
Today, Airbnb became one of a kind service that is used and recognized by the whole world. Data analysis on millions of listings provided through Airbnb is a crucial factor for the company. These millions of listings generate a lot of data - data that can be analyzed and used for security, business decisions, understanding of customers' and providers' (hosts) behavior and performance on the platform, guiding marketing initiatives, implementation of innovative additional services and much more. Theory:  
The very basic information about the dataset using df.info() 
  
By basic inspection, a particular property name will have one particular host name hosted by that same individual but a particular host name can have multiple properties in an area. 
So, host_name is a categorical variable here. Also neighbourhood_group (comprising of Manhattan, Brooklyn, Queens, Bronx, Staten Island), neighbourhood and room_type (private,shared,Entire home/apt) fall into this category. 
~id,latitude,longitude,price,minimum_nights,number_of_reviews,last_review, reviews_per_month, calculated_host_listings_count, availability_365 are numerical variables. 
 
Key Understandings:  
A host on airbnb holds multiple properties in a neighbourhood group(boroughs of NYC) with different host-ids but a host with a particular property/listing in a particular neighbourhood of a neighbourhood group holds a same host-id(also not mandatory as there are exceptions where few hosts have different id’s for each listing/property in a neighbourhood) 
Also the data tells, there might be cases where a particular host has co-hosted someone else’s property/listing in a neighbourhood on Airbnb. 

Flow chart:  
![image](https://github.com/user-attachments/assets/a20a9342-914d-46ee-b58d-12f3b3ee316f)

Conclusions: 
•	Most of the listings in NYC are in Manhattan and Brooklyn. Both of them have more than 20,000 listings, which are over 85% of the overall listings. The neighbourhood with the most listings is Williamsburg in Brooklyn.  
•	Around 52% of listings are entire home/apt, and 45% are private room. Only 2% are shared rooms. Among different neighbourhood groups, Brooklyn has the most private rooms, while Manhattan has the most entire homes/apts. 
•	The availability is lower in Brooklyn and Manhattan compared to other locations. 
•	Some words are quite popular in the name such as 'private', 'beautiful', 'cozy', 'modern', and 'quiet' 
Factors Affecting the price: 
•	Location: The price in Manhattan is much higher than in other locations. 
•	Room type: The entire home/apt is much more expensive than the private room and shared room. The private room is slightly more expensive than the shared room. 
•	Host listings count: It looks like the listings that the calculated_host_listings_count equals to 1 are more expensive. 
•	Minimum nights: No clear trend. 
•	Availability: No clear trend. 
Basis on which we can predict price: 
•	According to the Decision Tree model, the most important features:  
•	Room Type  
•	Location 

