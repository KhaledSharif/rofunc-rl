# Copyright 2023, Junjia LIU, jjliu@mae.cuhk.edu.hk
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rofunc.learning.RofuncRL.trainers.ppo_trainer import PPOTrainer
from rofunc.learning.RofuncRL.trainers.sac_trainer import SACTrainer
from .new_trainer import NewTrainer

trainer_map = {
    "PPO": PPOTrainer,
    "SAC": SACTrainer,
    "New": NewTrainer,
}
