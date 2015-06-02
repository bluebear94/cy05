#TouhouDanmakufu[Package]
#ScriptVersion[3]
#Title["Nice Game!"]
#Text["Actually a Python script. (Yay! I'm free now!)"]

from pathlib import *
from io import *

def process_file(path):
	output_path = path.with_suffix(".bin")
	with path.open(encoding="utf=8") as input, output_path.open(mode="wb") as output:
		output.write(bytes([0, 0]))
		lines = 0
		for line in input:
			if (line.endswith("\n")): line = line[0:-1]
			b = line.encode()
			l = len(b)
			upper = l >> 8
			lower = l & 255
			output.write(bytes([lower, upper]))
			output.write(b)
			lines += 1
		output.seek(0)
		upper = lines >> 8
		lower = lines & 255
		output.write(bytes([lower, upper]))

def iterate(f):
	all_files = Path(".").glob("**/*.txt")
	for file in all_files:
		try:
			f(file)
		except Exception:
			print(file + " could not be processed.")
			raise

# main

iterate(process_file)
print("Packaged!")
