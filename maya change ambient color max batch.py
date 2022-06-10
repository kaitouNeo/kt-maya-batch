# MAYA批量改环境色
import maya.cmds as mc;

# 获得选择的物体列表
selected_objects = mc.ls( selection=True );
# 遍历选择的物体
for obj in selected_objects:
    objName = str(obj)
    objType = mc.objectType( obj )
    attrList = mc.listAttr(obj)
    # 环境色修改
    if "ambientColor" in attrList:
        mc.setAttr( ("%s.ambientColor" %objName), 1, 1, 1 );
    print( "Edit Attribute succesfully: object: %s, type:%s" %( obj,  objType) )