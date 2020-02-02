import glob,xlrd,dominate
from dominate import document
from dominate.tags import *

loc = ("events.xlsx") 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0)

doc = dominate.document(title='Dominate your HTML')

with doc:
    comment("/* ALL EVENTS CARDS [STARTS]*/")
    for i in range(sheet.nrows):
        if(i==0):
            i+=1;
            continue
        #skip first cell of every column
        comment("--------------------------------")
        comment(i," SINGLE EVENT CARD STARTS -----")
        comment("--------------------------------")
        with div():
            attr(cls='col-12 col-md-6 col-lg-3 card-space')
            with div():
                attr(cls='single-price-plan text-center')
                with div():
                    attr(cls='package-plan')
                    h5(sheet.cell_value(i, 2),cls=sheet.cell_value(i, 9))
                    
                    
                    with div():
                        attr(cls='ca-price d-flex justify-content-center')
                        h4(sheet.cell_value(i, 1))
                        
                with div():
                    attr(cls='package-description')
                    p(sheet.cell_value(i, 3))
                    p(sheet.cell_value(i, 4))
                    p(sheet.cell_value(i, 5))
                    p(sheet.cell_value(i, 6))
                    p(sheet.cell_value(i, 7))
                    
                with div():
                    attr(cls='plan-button')
                    a('Register Now',href=sheet.cell_value(i, 8))
                    
        comment("-------------------------------")
        comment(i," SINGLE EVENT CARD ENDS ------")
        comment("-------------------------------")
        comment("*******************************")
        
    comment("/* ALL EVENTS CARDS [ENDS]*/")

print(doc)
