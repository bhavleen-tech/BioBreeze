import pandas as pd
import numpy as np


algae = [
    "Chlorella",
    "Spirulina",
    "Scenedesmus",
    "Nannochloropsis",
    "Dunaliella",
    "Haematococcus pluvialis",
    "Anabaena",
    "Botryococcus braunii",
    "Euglena",
    "Chlamydomonas",
]


num_samples = 1000


np.random.seed(42) 
carbon_content = np.random.uniform(200, 500, num_samples)  
nitrogen_content = np.random.uniform(10, 50, num_samples)  
other_impurities = np.random.uniform(5, 30, num_samples)  
temperature = np.random.uniform(15, 40, num_samples) 
humidity = np.random.uniform(30, 90, num_samples)  

def assign_best_algae(carbon, nitrogen, impurities, temp, hum):
    if carbon > 400 and temp < 25:
        return "Chlorella"
    elif nitrogen > 30 and hum > 60:
        return "Spirulina"
    elif impurities < 10:
        return "Scenedesmus"
    elif temp > 35 and hum < 50:
        return "Nannochloropsis"
    elif carbon < 300 and temp > 30:
        return "Dunaliella"
    elif hum > 80:
        return "Haematococcus pluvialis"
    elif nitrogen < 20:
        return "Anabaena"
    elif impurities > 25:
        return "Botryococcus braunii"
    elif temp < 20:
        return "Euglena"
    else:
        return "Chlamydomonas"


best_algae = [
    assign_best_algae(c, n, i, t, h)
    for c, n, i, t, h in zip(carbon_content, nitrogen_content, other_impurities, temperature, humidity)
]

dataset = pd.DataFrame({
    "carbon_content": carbon_content,
    "nitrogen_content": nitrogen_content,
    "other_impurities": other_impurities,
    "temperature": temperature,
    "humidity": humidity,
    "best_algae": best_algae,
})


dataset.to_csv("algae_dataset.csv", index=False)

print("Dataset created and saved as 'algae_dataset.csv'.")
