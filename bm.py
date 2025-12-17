import cProfile
import pstats
from typing import Callable, Any

def profileFunction(func: Callable[..., Any],
                    name: str,
                    *args,
                    **kwargs
                    ) -> None:
    
    profiler: object = cProfile.Profile()

    profiler.enable()
    func(*args, **kwargs)
    profiler.disable()

    print(f"===== Stats of {name.capitalize()} =====")
    stats = pstats.Stats(profiler)
    stats.sort_stats("tottime")
    stats.print_stats(10)