from pathlib import Path
from PIL import Image

font_name=input('Font name (exclude .png extension): ')
font_cp=Image.open('{0}/{1}.png'.format(Path(__file__).parent, font_name))

tile_size=font_cp.width//16
font_powder=Image.new('RGB', (tile_size*10, tile_size*12))

# Coords: x then y (multiplied by tilesize)
charmap=[
[( 1,6),( 2,6),( 3,6),( 4,6),( 5,6),( 6,6),( 7, 6),( 8, 6),( 9, 6),(10,6)],
[(11,6),(12,6),(13,6),(14,6),(15,6),( 0,7),( 1, 7),( 2, 7),( 3, 7),( 4,7)],
[( 5,7),( 6,7),( 7,7),( 8,7),( 9,7),(10,7),( 3, 0),( 4, 0),( 0, 0),( 4,4)],
[( 1,4),( 2,4),( 3,4),( 4,4),( 5,4),( 6,4),( 7, 4),( 8, 4),( 9, 4),(10,4)],
[(11,4),(12,4),(13,4),(14,4),(15,4),( 0,5),( 1, 5),( 2, 5),( 3, 5),( 4,5)],
[( 5,5),( 6,5),( 7,5),( 8,5),( 9,5),(10,5),(11, 1),(10, 1),( 8, 1),( 9,1)],
[( 0,3),( 1,3),( 2,3),( 3,3),( 4,3),( 5,3),( 6, 3),( 7, 3),( 8, 3),( 9,3)],
[( 1,2),( 0,4),( 3,2),( 4,2),( 5,2),(14,5),( 6, 2),(10, 2),( 8, 2),( 9,2)],
[(13,3),(13,2),(12,5),( 7,2),(12,2),(14,2),(15, 2),(11, 2),(15, 5),(12,7)],
[( 2,2),(12,3),(14,3),(15,3),(11,5),(13,5),(11, 7),(13, 7),( 0, 6),(14,7)],
[(12,2),(14,2),(12,3),(14,3),(11,3),(10,3),( 9,14),( 2, 0),(14,15),( 0,0)]]

for j in range(11):
    for i in range(10):
        x, y=charmap[j][i]
        font_powder.paste(font_cp.crop((x*tile_size, y*tile_size, (x+1)*tile_size, (y+1)*tile_size)), (i*tile_size, j*tile_size, (i+1)*tile_size, (j+1)*tile_size))

font_powder.save('{0}/{1}_powder.png'.format(Path(__file__).parent, font_name))