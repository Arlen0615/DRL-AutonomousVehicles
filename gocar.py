import sys
import gym
import envs.airsim

from baselines import deepq

def callback(lcl, glb):
    # stop training if reward exceeds 199999
    is_solved = lcl['t'] > 100 and sum(lcl['episode_rewards'][-101:-1]) / 100 >= 199999
    return is_solved

def main():
    env = gym.make("AirSimCarEnv-v0")
    model = deepq.models.mlp([64], layer_norm=True)
    
    print("\n======= Training session starts for DQN Car =======")    
    trainedModel = "car.pkl"
    act = deepq.learn(
        env,
        q_func=model,
        lr=1e-3,
        max_timesteps=100000,
        buffer_size=50000,
        exploration_fraction=1.0,   #0.1,
        exploration_final_eps=0.02,
        print_freq=10,
        param_noise=True,
        checkpoint_freq=2,
        learning_starts=5,
        callback=callback,
        load_state=trainedModel
    )
    print("\nSaving model to", trainedModel)
    act.save(trainedModel)


if __name__ == '__main__':
    main()
    
