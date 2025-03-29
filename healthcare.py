import random
import time

class HealthMonitor:
    def __init__(self, user_name):
        self.user_name = user_name
        self.heart_rate = 70  # Default resting heart rate
        self.blood_oxygen = 98  # Default SpO2 level
        self.subscription_fee = 20  # Monthly subscription in USD
        self.users = 1000  # Active users for revenue calculation

    def read_heart_rate(self):
        """Simulates heart rate reading from a medical device."""
        self.heart_rate = random.randint(60, 120)
        return self.heart_rate
    
    def read_blood_oxygen(self):
        """Simulates SpO2 reading from a medical device."""
        self.blood_oxygen = random.randint(90, 100)
        return self.blood_oxygen

    def analyze_data(self):
        """Analyzes heart rate and SpO2 levels and provides recommendations."""
        hr = self.read_heart_rate()
        spo2 = self.read_blood_oxygen()

        if hr > 100:
            alert = "High heart rate detected. Consider resting or hydrating."
        elif hr < 60:
            alert = "Low heart rate detected. If you feel dizzy, seek medical attention."
        else:
            alert = "Heart rate normal. Keep up a healthy lifestyle!"
        
        if spo2 < 95:
            alert += " Low SpO2 detected. Try deep breathing or seek medical help."
        
        return alert

    def generate_revenue(self):
        """Calculates projected revenue from subscriptions."""
        annual_revenue = self.users * self.subscription_fee * 12
        return annual_revenue

    def display_status(self):
        """Displays real-time health monitoring data."""
        while True:
            print(f"\nUser: {self.user_name}")
            print(f"Heart Rate: {self.read_heart_rate()} BPM")
            print(f"Blood Oxygen: {self.read_blood_oxygen()}% SpO2")
            print(f"Health Status: {self.analyze_data()}")
            print(f"Projected Annual Revenue: ${self.generate_revenue():,}")
            
            if self.generate_revenue() >= 200000:
                print("Business Goal Achieved: Generating over $200K per year!")
                break
            
            time.sleep(2)  # Simulate real-time monitoring interval

if __name__ == "__main__":
    user_monitor = HealthMonitor("John Doe")
    user_monitor.display_status()
