import gymnasium as gym
from stable_baselines3 import TD3
import os
import sys
import imageio

# Ensure that src is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
sys.path.append(project_root)


def register_environment():
    gym.register(
        id='CustomLunarLander-v3',
        entry_point='src.environments.custom_lunar_lander:CustomLunarLander',
        max_episode_steps=1000,
        reward_threshold=200,
    )


def main():
    # Register the custom environment
    register_environment()

    # Path to your trained TD3 model
    model_path = os.path.join(project_root, "src", "models", "td3", "custom", "td3_CustomLunarLander-v3_trial_3.zip")

    # Load the trained TD3 model
    if not os.path.exists(model_path):
        print(f"Model file not found at {model_path}. Please check the path.")
        sys.exit(1)

    model = TD3.load(model_path)

    # Create the environment with render_mode set to 'rgb_array'
    env = gym.make(
        "CustomLunarLander-v3",
        continuous=True,
        gravity=-10.0,
        enable_wind=True,
        wind_power=10.0,
        turbulence_power=1.0,
        observation_noise=0.02,
        partial_observation=True,
        render_mode="rgb_array"
    )

    num_episodes = 5  # Number of episodes to watch

    for episode in range(num_episodes):
        obs, info = env.reset()
        done = False
        truncated = False
        total_reward = 0.0
        step = 0
        frames = []

        while not done and not truncated:
            # Use the trained model to predict the action
            action, _states = model.predict(obs, deterministic=True)

            # Take the action in the environment
            obs, reward, done, truncated, info = env.step(action)
            total_reward += reward
            step += 1

            # Capture the frame
            frame = env.render()
            frames.append(frame)

        # Save the episode as a GIF
        video_dir = os.path.join(project_root, "data", "videos")
        os.makedirs(video_dir, exist_ok=True)
        video_path = os.path.join(video_dir, f"episode_{episode + 1}.gif")
        imageio.mimsave(video_path, frames, fps=30)
        print(f"Episode {episode + 1}: Total Reward = {total_reward}, Steps = {step}, Video saved to {video_path}")

    env.close()


if __name__ == "__main__":
    main()
