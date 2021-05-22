import bpy
import bmesh


bpy.ops.mesh.primitive_cube_add()
object = bpy.context.active_object

WIDTH = 2
HEIGHT = 2
LENGHT = 2
bpy.context.object.dimensions = WIDTH * 2, LENGHT * 2, HEIGHT * 2


bpy.ops.mesh.primitive_cube_add()
bpy.context.active_object.name = 'SmallCube'
bpy.context.object.dimensions = WIDTH, LENGHT, HEIGHT

objects = bpy.context.scene.objects

for obj in objects:
    obj.select_set(obj.type == "MESH")

bpy.ops.object.join()


obj = bpy.context.active_object
bpy.ops.object.mode_set(mode = 'EDIT') 
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
obj.data.vertices[0].select = True
obj.data.vertices[1].select = True
obj.data.vertices[8].select = True
obj.data.vertices[9].select = True
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.edge_face_add()
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
obj.data.vertices[2].select = True
obj.data.vertices[3].select = True
obj.data.vertices[10].select = True
obj.data.vertices[11].select = True
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.edge_face_add()
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
obj.data.vertices[4].select = True
obj.data.vertices[5].select = True
obj.data.vertices[12].select = True
obj.data.vertices[13].select = True
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.edge_face_add()
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
obj.data.vertices[6].select = True
obj.data.vertices[7].select = True
obj.data.vertices[14].select = True
obj.data.vertices[15].select = True
bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.mesh.edge_face_add()
bpy.ops.mesh.select_mode(type="VERT")
bpy.ops.mesh.select_all(action = 'DESELECT')
bpy.ops.object.mode_set(mode = 'OBJECT')
