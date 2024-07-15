import json

from katrain.core.base_katrain import KaTrainBase
from katrain.core.engine import KataGoEngine
from katrain.core.game import Game, KaTrainSGF

katrain = KaTrainBase(force_package_config=True, debug_level=2)
engine = KataGoEngine(katrain, katrain.config("engine"))
#                                                             #d16   d17   d18   f18   c17   f17   e17   f16
# sgf = "(;GM[1]FF[4]RU[japanese]PB[zjk]PW[xiaozhi]CA[UTF-8];B[dd];W[dc];B[db];W[fb];B[cc];W[fc];B[ec];W[fd];)"

with open("test-sgf/101weiqi-2024-06-25.sgf") as fin:
    lines = fin.readlines()
    sgf = "".join(lines)

move_tree = KaTrainSGF.parse_sgf(sgf)

# node = moves.nodes_in_tree[-1]

game = Game(katrain, engine, move_tree=move_tree)
game.redo(140)
# print(game.board_size, game.stones, len(game.stones))
stones = game.stones

output = []
for st in stones:
    output.append([st.player, st.coords[0], st.coords[1]])
joutput = json.dumps(output)
with open("./test-sgf/101weiqi-2024-06-25-140.json", "w") as fout:
    fout.writelines([joutput])

# node.analyze(engine, analyze_fast=False)

game.current_node.analyze(engine, analyze_fast=False)
engine.wait_to_finish()


with open("./test-sgf/101weiqi-2024-06-25-140-analysis.json", "w") as fout:
    ownership = json.dumps(game.current_node.analysis["ownership"])
    fout.writelines(ownership)

print("zjk")

