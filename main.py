from bs4 import BeautifulSoup
import urllib.request
import re
import pandas as pd
import sys    

html = urllib.request.urlopen('https://www.freelancer.com/job/')
webpage = BeautifulSoup(html, 'html.parser')
dataset = {"Skill":[], "Jobs":[], "Category":[]}
# Iterate through each individual section
for category in webpage.find_all("section", attrs={"class":"PageJob-category"}):
    myCategory = category.find("h3", attrs={"class":"PageJob-category-title"}).get_text()
    # Grab each grid and iterate through each row
    for grid in category.find_all("ul", attrs={"class":"PageJob-browse-list Grid"}):
        for element in grid.find_all("a", attrs={"class":re.compile("PageJob-category-link $")}):
            name, jobs = re.findall(r"([^\(]*)\xa0\((.*)\)", element.get_text().strip())[0]
            dataset["Skill"].append(name)
            dataset["Jobs"].append(jobs)
            dataset["Category"].append(myCategory[:myCategory.rfind("(")].strip())

# Determine the filename that we'll be writing to file.
# Defaults to Output.csv
filename = "Output.csv"
if len(sys.argv) == 2:
    filename = sys.argv[1]
df = pd.DataFrame(dataset)
# NOTE: DataFrame will order columns by alphabet
# We'll change the ordering
df = df[["Skill", "Jobs", "Category"]]
df.to_csv(filename)
print("Dataset created!")