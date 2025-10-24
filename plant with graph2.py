import time
import random
import matplotlib.pyplot as plt

class Plant:
    def __init__(self, name, moisture_level=50):
        self.name = name
        self.moisture_level = moisture_level  # 0 to 100

    def dry_out(self):
        # Simulate drying over time
        self.moisture_level -= random.randint(5, 15)
        self.moisture_level = max(self.moisture_level, 0)

    def water(self):
        print(f" Watering {self.name}...")
        self.moisture_level += random.randint(20, 30)
        self.moisture_level = min(self.moisture_level, 100)

    def status(self):
        print(f"{self.name} moisture level: {self.moisture_level}%")
        if self.moisture_level < 30:
            print("Soil is dry. Needs watering!")
        elif self.moisture_level > 80:
            print("Soil is moist. No need to water.")
        else:
            print("Soil is okay.")

def simulate_watering_system(plant, cycles=10, interval=2):
    print(f"Starting watering simulation for {plant.name}...\n")
    
    moisture_history = []
    cycle_labels = []

    for i in range(cycles):
        print(f"--- Cycle {i+1} ---")
        plant.dry_out()
        plant.status()
        if plant.moisture_level < 30:
            plant.water()
        print()

        # Store data for graph
        moisture_history.append(plant.moisture_level)
        cycle_labels.append(f"Cycle {i+1}")

        time.sleep(interval)  # Simulate time passing

    # Plot moisture graph
    plt.plot(cycle_labels, moisture_history, marker='o', color='green')
    plt.title(f"{plant.name} Moisture Level Over Time")
    plt.xlabel("Simulation Cycle")
    plt.ylabel("Moisture Level (%)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    my_plant = Plant("Aloe Vera")
    simulate_watering_system(my_plant)
