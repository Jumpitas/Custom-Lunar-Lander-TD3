# Reinforcement Learning: Lunar Lander with TD3

This project modifies the Lunar Lander environment to be more demanding and realistic. The changes include **partially obstructed observations**, **variable wind and turbulence**, **gravity adjustments**, and a **reward system** focused on efficiency. The agent only observes **6 state variables** (position, velocity, partial angle info), simulating sensor limitations and partial observability.

---

## Key Changes

- **Partial Observability**:
  The agent sees only 6 state variables (position, velocity, partial angle info), omitting certain data to simulate sensor limitations.

- **Dynamic Conditions**:  
  Wind intensity, turbulence, and gravity can change from one episode to another, testing the agent’s adaptability.

- **Reward Reshaping**:  
  - Checking fuel usage to encourage efficient flight.  
  - Penalizing large deviations in vehicle orientation.  
  - Applying a mild penalty per time step to promote quicker decisions.  
  - Rewarding smooth landings within certain boundaries.

**Key reward/penalty modifications**:
- **Penalties for excessive fuel consumption** (encouraging efficient flight).
- **Penalties for large angular deviation** (promoting stable orientation).
- **Mild penalty per time step** (accelerating decision-making).
- **Reward for smooth landings** within specified boundaries.

---

## Algorithm: TD3

We use **TD3 (Twin Delayed Deep Deterministic Policy Gradient)**, well-suited for continuous control tasks. The method involves:
- Two critic networks to reduce overestimation bias.
- Delayed policy updates for stability.
- Target smoothing regularization to handle abrupt updates.

---

## Results & Analysis

- **Partial Observability**:  
  The agent learned to handle missing data by focusing on key signals (position and velocity).

- **Wind & Gravity**:  
  TD3 coped with the unpredictable environment; though strong turbulence occasionally caused crashes, overall the agent adapted over time.

- **Reward Efficiency**:  
  Fuel usage decreased, and the agent maintained a more stable angle, achieving smoother and faster landings.

---

## Conclusion

By integrating **partial observability**, **dynamic environmental factors**, and **efficiency-driven goals**, the Lunar Lander environment becomes significantly more realistic and challenging. **TD3** demonstrated robust performance under these tougher conditions, although future extensions might include:
- Self-navigated multi-stage tasks (takeoff and landing).
- Obstacle avoidance strategies for full autonomy.
