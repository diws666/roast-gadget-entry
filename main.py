# This file IS the entry: ENTRY is the whole one-line entry and must stay
# byte-identical. It is written to /output/entry.txt with no trailing newline.
ENTRY = "My earbuds disconnect exactly when the song gets good. Every time."

with open("/output/entry.txt", "w") as f:
    f.write(ENTRY)
