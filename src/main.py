import os

import matplotlib.pyplot as plt
import mplcursors as mpl
import pandas as pd
from matplotlib.ticker import FuncFormatter

from model import Solve

df = pd.read_csv("input.csv").rename(
  columns={"No.": "idx", "Time": "time"}
)

solves = [
  Solve(**row._asdict())
  for row in df[["idx", "time"]].itertuples(index=False)
]


def format_time(time, _):
  minutes = int(time // 60)
  seconds = time % 60
  return f"{minutes}:{seconds:05.2f}"


x_times = [n for n in range(1, len(solves) + 1)]
individual_times = [solve.get_time_float() for solve in solves]


best_times = {}
prev_best_time = individual_times[0]
for idx, time in enumerate(individual_times):
  if idx == 0:
    continue

  if time < prev_best_time:
    prev_best_time = time
    best_times[idx + 1] = time

best_x = list(best_times.keys())
best_y = list(best_times.values())
best_scatter = plt.scatter(best_times.keys(), best_times.values(), color="red")

cur = mpl.cursor(best_scatter, hover=True)
cur.connect("add", lambda sel: sel.annotation.set_text(
  f"Solve {best_x[sel.index]}: {format_time(best_y[sel.index], 0)}"
))


x_mo3 = [n for n in x_times if n > 2]
mo3 = []
for i in range(len(solves) - 2):
  mo3.append(sum([solve.get_time_float() for solve in solves[i:i+3]]) / 3)

x_ao5 = [n for n in x_times if n > 4]
ao5 = []
for i in range(len(solves) - 4):
  ao5.append(sum(sorted([solve.get_time_float() for solve in solves[i:i+5]])[1:4]) / 3)

mean = sum(solve.get_time_float() for solve in solves) / len(solves)

plt.margins(0)
#plt.ylim(0)

plt.xlabel("Index")
plt.ylabel("Time")

plt.gca().yaxis.set_major_formatter(FuncFormatter(format_time))

plt.plot(x_times, individual_times, label="Solves")
plt.plot(x_mo3, mo3, label="mo3")
plt.plot(x_ao5, ao5, label="ao5")

# My personal information, remove this during use
new_cube = 138
if os.getenv("PERSONAL", "False") == "True":
  plt.axvspan(new_cube, len(solves), color='yellow', alpha=0.25)
  plt.axvline(new_cube, color='red', linestyle='--')
  plt.text(new_cube+1, mean, "New Megaminx (YJ Megaminx YuHu V2 M)", rotation=90)
# My personal information, remove this during use

if __name__ == "__main__":
  plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), fancybox=True, shadow=True)
  plt.show()