import maya.cmds as cmds
import maya.mel as mel

class MainClassBadGeo:
    	
    def __init__(self):
        self.bG_output = ""      
                
    def badGeoUI(self):

        # C H E C K  W I N D O W
        
        if (cmds.window("bGWin", exists=True)):
        	cmds.deleteUI("bGWin", wnd=True)
        	cmds.windowPref("bGWin", r=True)        	            
            
        # C R E A T E  U I
                
        cmds.window("bGWin", s=False, tlb=True, rtf=True, t="面选择", w = 145)
        cmds.columnLayout(adj=True)
        
     
        # B A D  G E O M E T R Y
        		
        cmds.frameLayout(label=("类型"), bgc=(0.3, 0.3, 0.3), collapsable=False, collapse=False, w=120)
                    
        cmds.columnLayout(adj=True)
        
        cmds.button(label="三角面", h=25, c = self.bGTriangles)
        cmds.button(label="四边面", h=25, c = self.bGQuads)
        cmds.button(label="多边面", h=25, c = self.bGNGons)
        
               
        cmds.setParent("..")
        cmds.setParent("..")
        
        
        # O U T P U T
        
        cmds.frameLayout(label='输出', bgc=(0.3, 0.3, 0.3), collapsable=False, collapse=True)
                
        self.bG_output = cmds.textField(h = 25, bgc=(0.16, 0.16, 0.16), en = True, ed=False)
        
        cmds.setParent("..")
        cmds.setParent("..")

               
        # S H O W  W I N D O W
        
        cmds.showWindow("bGWin")
        
	
	# M E T H O D S
	
	# T R I A N G L E S

    def bGTriangles(self, _=False):
        bGsel = cmds.ls(sl = True) 
        
        # Change to Component mode to retain object highlighting for better visibility               
        cmds.selectMode(q=True, co=True)

        # Select Object/s and Run Script to highlight Triangles
        cmds.polySelectConstraint(m=3 ,t = 0x0008, sz=1)
        cmds.polySelectConstraint(dis=True)
      
        # Update Textfield  
        bGPolys = cmds.polyEvaluate(fc=True)
        
        try:
            cmds.textField(self.bG_output, e=True, bgc=(1,0,0), tx=("%s 个三角面" % int(bGPolys)))        
        except:
            cmds.textField(self.bG_output, e=True, tx=("请选择模型"), bgc=(1,1,0))
                
     
    # Q U A D S
        
    def bGQuads(self, _=False):
        bGsel = cmds.ls(sl = True)
        
        cmds.selectMode(q=True, co=True)
        
        cmds.polySelectConstraint(m=3 ,t = 0x0008, sz=2)
        cmds.polySelectConstraint(dis=True)
        
        bGPolys = cmds.polyEvaluate(fc=True)
        
        try:
            cmds.textField(self.bG_output, e=True, tx=("%s 个四边面" % int(bGPolys)))
        except:
            cmds.textField(self.bG_output, e=True, tx=("请选择模型"))

    
    # N - G O N S
        
    def bGNGons(self, _=False):
        bGsel = cmds.ls(sl = True) 
        
        cmds.selectMode(q=True, co=True)
        
        cmds.polySelectConstraint(m=3 ,t = 0x0008, sz=3)
        cmds.polySelectConstraint(dis=True)
        
        bGPolys = cmds.polyEvaluate(fc=True)
        
        try:
            cmds.textField(self.bG_output, e=True, tx=("%s 个多边面" % int(bGPolys)))
        except:
            cmds.textField(self.bG_output, e=True, tx=("请选择模型"))

    
          
        
        
MCBG = MainClassBadGeo()
MCBG.badGeoUI()
