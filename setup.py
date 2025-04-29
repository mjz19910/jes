from setuptools import Extension, setup
from Cython.Build import cythonize


extensions = [
	Extension("jes", ["jes.py"]),
	Extension("jes_sim", ["jes_sim.py"]),
	Extension("jes_creature", ["jes_creature.py"]),
	Extension("jes_species_info", ["jes_species_info.py"]),
	Extension("jes_dataviz", ["jes_dataviz.py"]),
	Extension("jes_ui", ["jes_ui.py"]),
	Extension("jes_shapes", ["jes_shapes.py"]),
	Extension("jes_slider", ["jes_slider.py"]),
	Extension("jes_button", ["jes_button.py"]),
]

setup(
    ext_modules=cythonize(extensions),
)
