import numpy as np
from jes_sim import Sim
from jes_ui import UI

def init():
	sim = Sim(
		_c_count=3 * 2, _stabilization_time=int(50 * 4), _trial_time=int(75 * 4),
		_beat_time=20, _beat_fade_time=5, _c_dim=[4,4],
		_beats_per_cycle=3, _node_coor_count=4, # x_position, y_position, x_velocity, y_velocity
		_y_clips=[-10000000,0], _ground_friction_coef=25,
		_gravity_acceleration_coef=0.002, _calming_friction_coef=0.7,
		_typical_friction_coef=0.8, _muscle_coef=0.08,
		_traits_per_box=3, # desired width, desired height, rigidity
		_traits_extra=1, # heartbeat (time)
		_mutation_rate=0.07 * 3, _big_mutation_rate=0.025 * 1,
		_UNITS_PER_METER=0.05
	)

	# Cosmetic UI variables
	ui = UI(
		_W_W=1920, _W_H=1078,
		_MOVIE_SINGLE_DIM=(650,650),
		_GRAPH_COOR=(850,50,900,500), _SAC_COOR=(850,560,900,300), _GENEALOGY_COOR=(20,105,530,802,42),
		_COLUMN_MARGIN=330, _MOSAIC_DIM=[10,24,24,30], #_MOSAIC_DIM=[10,10,17,22],
		_MENU_TEXT_UP=180, _CM_MARGIN1=20, _CM_MARGIN2=1
	)

	sim.ui = ui
	ui.sim = sim
	ui.addButtonsAndSliders()

	sim.initializeUniverse()
	return ui

def ui_loop(ui):
	prev_len = None
	target_len = 0
	sim = ui.sim
	while ui.running:
		ui.sim.checkALAP()
		ui.detectMouseMotion()
		ui.detectEvents()
		ui.detectSliders()
		ui.doMovies()
		ui.drawMenu()
		ui.show()
		if prev_len != len(sim.creatures) and len(sim.creatures) - 1 > target_len:
			ui.ALAPButton.setting = 0
			target_len += 1000

def run_app():
	ui = init()
	ui_loop(ui)

if __name__ == "__main__":
	run_app()
