
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'game'))

from game_engine import FlappyBirdEnv


    # bird_above_gap_top = state[3]
    # if bird_above_gap_top < 0:
    #     return 0
    # return 1
def naive_action(state):
    
        bird_vel = state[1]
        dist_from_top = state[3]
        dist_from_bottom = state[4]

        
        center_error = dist_from_top - dist_from_bottom

        if center_error > 0: 
            if bird_vel > 0.2: 
                return 1 
                
        return 0 
def run(n_games=5):
    env = FlappyBirdEnv()
    scores = []

    for i in range(n_games):
        state = env.reset()
        done = False
        while not done:
            action = naive_action(state)
            state, reward, done = env.step(action)
        scores.append(env.score)
        print(f"Partie {i + 1} : score = {env.score}")

    print(f"\nScore moyen sur {n_games} parties : {sum(scores) / len(scores):.1f}")

if __name__ == '__main__':
    run()

