import numpy as np
import casadi

from ..misc.enums import Instant
from ..limits.objective_functions import Objective


class SolverInterface:
    def __init__(self, ocp):
        self.ocp = ocp
        self.solver = None

    def configure(self, **options):
        raise RuntimeError("SolverInterface is an abstract class")

    def solve(self):
        raise RuntimeError("SolverInterface is an abstract class")

    def get_iterations(self):
        raise RuntimeError("SolverInterface is an abstract class")

    def get_optimized_value(self, ocp):
        raise RuntimeError("SolverInterface is an abstract class")

    def online_optim(self, ocp):
        raise RuntimeError("SolverInterface is an abstract class")

    def start_get_iterations(self):
        raise RuntimeError("Get Iteration not implemented for solver")

    def finish_get_iterations(self):
        raise RuntimeError("Get Iteration not implemented for solver")

    def get_objective(self):
        self.out["sol_obj"] = Objective.Analyse.get_objective_values(self.ocp, self.out["sol"])

