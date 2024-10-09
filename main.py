import google.generativeai as genai
import os
import random
import pandas as pd
import json 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ["GENAI_API_KEY"])


model = genai.GenerativeModel("gemini-1.5-flash", generation_config={"response_mime_type": "application/json"})

response = model.generate_content("""
                                  
                                  Using this following Schema
                                
                                  Generate 10 synthetic customer reviews for a new smartphone, mentioning its high-quality camera, long battery life, and reasonable price. Ensure each review is unique and realistic like human write this but keep short.
                                  
                                  Review = {
                                        "review": str
                                    }  
                                    return list[Review]
                                  
                                  
""")


data = response.text
print(data)
# # Prepare the data for the DataFrame
newdata = []
for i in range(len(data)):
    newdata.append({
        "rating": random.randint(4, 5),
        "userid": random.randint(19999,400000),
        "review": data[i]["review"],
        "verified purchase": random.randint(0, 1)
    })


# Create a pandas DataFrame
df = pd.DataFrame(newdata)

# Save the DataFrame to a CSV file
df.to_csv("example_synthetic_reviews.csv", index=False)

print("Synthetic reviews saved to synthetic_reviews.csv")
