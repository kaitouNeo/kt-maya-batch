# MAYA批量改漫反射
import maya.cmds as mc;

# 获得选择的物体列表
selected_objects = mc.ls( selection=True );
# 遍历选择的物体
for obj in selected_objects:
    objName = str(obj)
    objType = mc.objectType( obj )
    attrList = mc.listAttr(obj)
    # 漫反射修改
    if "diffuse" in attrList:
        mc.setAttr( ("%s.diffuse" %objName), 1 );
    print( "Edit Attribute succesfully: object: %s, type:%s" %( obj,  objType) )