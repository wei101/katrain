from katrain.core.base_katrain import KaTrainBase
from katrain.core.engine import KataGoEngine
from katrain.core.game import Game, KaTrainSGF

katrain = KaTrainBase(force_package_config=True, debug_level=0)
engine = KataGoEngine(katrain, katrain.config("engine"))
# print(engine.config)

moves = KaTrainSGF.parse_sgf("(;GM[1]FF[4]RU[japanese]PB[zjk]PW[xiaozhi]CA[UTF-8];B[pd];W[po];B[dd];)")

game = Game(katrain, engine)

print(moves.nodes_in_tree)

node = moves.nodes_in_tree[-1]
node.analyze(engine, analyze_fast=False)


