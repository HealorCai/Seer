"""
https://github.com/mees/calvin/blob/main/dataset/README.md
"""

import numpy as np
from pdb import set_trace
calvin_ep_npz = "/fs-computility/efm/caizetao/projects/moat_ws/Seer/calvin/dataset/calvin_debug_dataset/training/episode_0358482.npz" # one step
calvin_ep = np.load(calvin_ep_npz)

# print(f'actions: {calvin_ep["actions"]}')
# print(f'rel_actions: {calvin_ep["rel_actions"]}')
# print(f'robot_obs: {calvin_ep["robot_obs"]}')
# print(f'scene_obs: {calvin_ep["scene_obs"]}')
# print(f'rgb_static: {calvin_ep["rgb_static"]}')
# print(f'rgb_gripper: {calvin_ep["rgb_gripper"]}')
# print(f'rgb_tactile: {calvin_ep["rgb_tactile"]}')
# print(f'depth_static: {calvin_ep["depth_static"]}')
# print(f'depth_gripper: {calvin_ep["depth_gripper"]}')
# print(f'depth_tactile: {calvin_ep["depth_tactile"]}')

print(f'actions: {len(calvin_ep["actions"])}')
print(f'rel_actions: {len(calvin_ep["rel_actions"])}')
print(f'robot_obs: {len(calvin_ep["robot_obs"])}')
print(f'scene_obs: {len(calvin_ep["scene_obs"])}')
print(f'rgb_static: {len(calvin_ep["rgb_static"])}')
print(f'rgb_gripper: {len(calvin_ep["rgb_gripper"])}')
print(f'rgb_tactile: {len(calvin_ep["rgb_tactile"])}')
print(f'depth_static: {len(calvin_ep["depth_static"])}')
print(f'depth_gripper: {len(calvin_ep["depth_gripper"])}')
print(f'depth_tactile: {len(calvin_ep["depth_tactile"])}')

# set_trace()


except_lang_idx = np.load("/fs-computility/efm/caizetao/projects/moat_ws/Seer/calvin/dataset/task_ABC_D/training/except_lang_idx/except_lang_idx.npy")
idx = np.load("/fs-computility/efm/caizetao/projects/moat_ws/Seer/calvin/dataset/calvin_debug_dataset/training/ep_start_end_ids.npy")
print(len(except_lang_idx))
print(idx)