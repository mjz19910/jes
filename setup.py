from setuptools import Extension, setup
from Cython.Build import cythonize


extensions = [
    Extension("jes_init", ["jes_init.pyx"]),
    Extension("jes_sim", ["jes_sim.pyx"]),
    Extension("jes_creature", ["jes_creature.pyx"]),
    Extension("jes_species_info", ["jes_species_info.pyx"]),
    Extension("jes_dataviz", ["jes_dataviz.pyx"]),
    Extension("jes_ui", ["jes_ui.pyx"]),
    Extension("jes_shapes", ["jes_shapes.pyx"]),
    Extension("jes_slider", ["jes_slider.pyx"]),
    Extension("jes_button", ["jes_button.pyx"]),
]

setup(
    ext_modules=cythonize(extensions, language_level = "3"),
)
