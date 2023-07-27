# import unicodedata
import requests
from bs4 import BeautifulSoup
import json


url = "https://www.sodere.com/movies"


response = requests.get(url)


soup = BeautifulSoup(response.content, "html.parser")


titles = soup.find_all("strong")


title_list = []


for title in titles:
    title_list.append(title.text)


json_data = {"titles": title_list}


json_output = json.dumps(json_data)



# # Define the input string containing Ethiopic script characters
# input_str = "\n \u12a0\u1275\u121d\u1321\u1265\u129d"

# # Use the unicodedata library to normalize the string to the NFKD form, which separates the diacritic marks from the base characters
# normalized_str = unicodedata.normalize("NFKD", input_str)

# # Use the ethiopic library to convert the NFKD string to its Amharic script representation
# amharic_str = ethiopic.transliterate(normalized_str, "ethiopic-am")


# print(amharic_str)

print(json_output)