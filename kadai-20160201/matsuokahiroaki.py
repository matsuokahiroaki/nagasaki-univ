#!/usr/bin/env python2.7
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.vec3 as Vec3

mc = minecraft.Minecraft.create("localhost")
pos = mc.player.getPos()

print pos

#micra -68,0,165
#zetai -1999,4,-734 (+1931,-4,+899)

pos.x = -1930
pos.y = 4
pos.z = -899

pos.x +=  1931
pos.y +=  - 4
pos.z +=  899

# -2075 4 -724

for i in range(0, 64):
    for j in range(0, 4):
        for k in range(0, 64):
            #mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.BRICK_BLOCK.id)
            #TNT:(46,1),Diamond57
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(35))

pos.x = -1929
pos.y = 4
pos.z = -901

pos.x +=  1931
pos.y +=  - 4
pos.z +=  899

for i in range(0, 62):
    for j in range(0, 4):
        for k in range(0, 62):
            #mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.BRICK_BLOCK.id)
            #TNT:(46,1),Diamond57
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(0))  

pos.x = -1929
pos.y = 4
pos.z = -901

pos.x +=  1931
pos.y +=  - 4
pos.z +=  899

for i in range(0, 61):
    for j in range(0, 1):
        for k in range(0, 61):
            #mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.BRICK_BLOCK.id)
            #TNT:(46,1),Diamond57
            mc.setBlock(pos.x+i, pos.y + j, pos.z+k, block.Block(35))  

