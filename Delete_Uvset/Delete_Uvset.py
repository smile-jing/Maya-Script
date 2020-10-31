#coding=utf-8
import maya.cmds as cmds
import os,sys

def Delete_UvsetApply():
    renamecheckbox=cmds.checkBox('rm_cbox_UI',q=1,v=1)
    SelectObjects=cmds.ls(sl=1,l=1)
    if SelectObjects:
        for item in SelectObjects:
            firstUvSet=cmds.getAttr(item+'.uvSet[0].uvSetName')
            cmds.polyCopyUV(item,uvs=firstUvSet)
            for uvset in cmds.polyUVSet(q=1,auv=1):
                if uvset!=firstUvSet:
                    cmds.polyUVSet(item,d=1,uvs=uvset)
            if renamecheckbox:
                cmds.polyUVSet(e=1,rn=1,uvs=firstUvSet,nuv="map1")

# Make a new window
#
window = cmds.window( title=u"删除Uv层", iconName='Short Name', widthHeight=(300, 100) )
cmds.columnLayout( adjustableColumn=True )
cmds.text(l=u"选择要清理Uv层的物体")
cmds.text(l=u"支持多选")
cmds.text(l='')
cmds.checkBox('rm_cbox_UI',l='将默认uvset重命名为map1')
cmds.text(l='')
cmds.button(l="Apply",c="Delete_UvsetApply()")
cmds.setParent( '..' )
cmds.showWindow( window )
