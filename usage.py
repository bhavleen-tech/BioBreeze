import joblib
import tkinter as tk
from tkinter import messagebox

model = joblib.load("algae_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")
scaler = joblib.load("scaler.pkl")  


def predict_algae():
    try:
    
        carbon = float(entry_carbon.get())
        nitrogen = float(entry_nitrogen.get())
        impurities = float(entry_impurities.get())
        temp = float(entry_temp.get())
        humidity = float(entry_humidity.get())

 
        input_data = scaler.transform([[carbon, nitrogen, impurities, temp, humidity]])

   
        prediction = model.predict(input_data)
        predicted_algae = label_encoder.inverse_transform(prediction)[0]

        
        messagebox.showinfo("Prediction", f"The best algae is: {predicted_algae}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


app = tk.Tk()
app.title("Algae Predictor")

tk.Label(app, text="Carbon Content (ppm):").grid(row=0, column=0, padx=10, pady=5)
entry_carbon = tk.Entry(app)
entry_carbon.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Nitrogen Content (ppm):").grid(row=1, column=0, padx=10, pady=5)
entry_nitrogen = tk.Entry(app)
entry_nitrogen.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Other Impurities (ppm):").grid(row=2, column=0, padx=10, pady=5)
entry_impurities = tk.Entry(app)
entry_impurities.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Temperature (Celsius):").grid(row=3, column=0, padx=10, pady=5)
entry_temp = tk.Entry(app)
entry_temp.grid(row=3, column=1, padx=10, pady=5)

tk.Label(app, text="Humidity (%):").grid(row=4, column=0, padx=10, pady=5)
entry_humidity = tk.Entry(app)
entry_humidity.grid(row=4, column=1, padx=10, pady=5)


tk.Button(app, text="Predict", command=predict_algae).grid(row=5, column=0, columnspan=2, pady=20)


app.mainloop()
