# Reinforcement Learning: Lunar Lander with TD3

This project modifies the Lunar Lander environment to **increase challenge and realism**, focusing on **partially obstructed observations**, **variable wind/turbulence**, **gravity adjustments**, and a **more efficiency-oriented reward system**.

## Key Changes
- **Partial Observability:** The agent sees only 6 state variables (position, velocity, partial angle info), omitting certain data to simulate sensor limitations.  
- **Dynamic Conditions:** Wind intensity, turbulence, and gravity can change across episodes, testing the agent’s adaptability.  
- **Reward Reshaping:**  
  - Penalties for excessive fuel consumption (encouraging efficient flight).  
  - Penalties for large angular deviation (promoting stable orientation).  
  - Mild penalty per time step (accelerating decision-making).  
  - Reward for smooth landings within specified boundaries.

## Algorithm: TD3
We applied **TD3** (Twin Delayed Deep Deterministic Policy Gradient), an algorithm tailored for continuous control. Hyperparameters (learning rate, batch size, tau, gamma, buffer size) were optimized with **Optuna**, ensuring robust performance under varied conditions.

## Results & Analysis
- **Partial Observability:** The agent learned to compensate for missing information by focusing on the most critical signals (position and velocity).  
- **Wind & Gravity:** TD3 adapted to unstable conditions, though strong turbulence introduced sporadic crashes.  
- **Reward Efficiency:** Fuel usage decreased, and the agent maintained more stable angles, leading to smoother, quicker landings.

## Conclusion
By introducing partial observations, dynamic environments, and efficiency-driven rewards, we created a more **realistic** and **challenging** scenario. While TD3 handled these constraints effectively, future work could expand toward multi-stage tasks (takeoff and landing) and obstacle avoidance for enhanced autonomy.
