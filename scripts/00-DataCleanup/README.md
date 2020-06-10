# Step 0: Data Clean Up

## Purpose
Although we have the data split up into books, the formatting seems to be almost arbitrary. With endlines in all the wrong places, this is unnecessarily difficult for a machine to read.

## Method
The bible is a very structured text. With the entire text being categorized into `Book >> Verse >> Passage` it naturally carries an index.<br>
Hence we're going to change all our books into `.csv` files with the format `verse no., passage no., text`