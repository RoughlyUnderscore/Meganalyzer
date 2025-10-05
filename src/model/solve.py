import dataclasses

@dataclasses.dataclass(kw_only=True)
class Solve:
  idx: int
  time: str

  def get_time_float(self):
    min_split = self.time.split(":")
    if len(min_split) == 1:
      return float(self.time)

    return int(min_split[0]) * 60 + float(min_split[1])