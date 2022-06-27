import time

Website1 = open ("Page1.HTML", "r")
Website2 = open ("Page2.HTML", "r")
Website3 = open ("Page3.HTML", "r")
Website4 = open ("Page4.HTML", "r")
Website5 = open ("Page5.HTML", "r")
Website6 = open ("Page6.HTML", "r")
Website7 = open ("Page7.HTML", "r")
Website8 = open ("Page8.HTML", "r")
Website9 = open ("Page9.HTML", "r")
Website10 = open("Page10.HTML", "r")

PagerankA_in = []
PagerankB_in = []
PagerankC_in = []
PagerankD_in = []
PagerankE_in = []
PagerankF_in = []
PagerankG_in = []
PagerankH_in = []
PagerankI_in = []
PagerankJ_in = [] 

PagerankA = 1
PagerankB = 1 
PagerankC = 1
PagerankD = 1
PagerankE = 1
PagerankF = 1
PagerankG = 1
PagerankH = 1
PagerankI = 1
PagerankJ = 1

Website_search = ["""<a href="Page1.HTML">""",
                  """<a href="Page2.HTML">""",
                  """<a href="Page3.HTML">""",
                  """<a href="Page4.HTML">""",
                  """<a href="Page5.HTML">""",
                  """<a href="Page6.HTML">""",
                  """<a href="Page7.HTML">""",
                  """<a href="Page8.HTML">""",
                  """<a href="Page9.HTML">""",
                  """<a href="Page10.HTML">"""]

Website_links = [PagerankA_in,
                 PagerankB_in,
                 PagerankC_in,
                 PagerankD_in,
                 PagerankE_in,
                 PagerankF_in,
                 PagerankG_in,
                 PagerankH_in,
                 PagerankI_in,
                 PagerankJ_in]

 
Websites = [Website1 , Website2, Website3 , Website4 , Website5 , Website6, Website7, Website8, Website9 , Website10]


Outbound_links = []
Inbound_links = [0,0,0,0,0,0,0,0,0,0]
term_count = [0,0,0,0,0,0,0,0,0,0]
New_Output_Terms = [0,0,0,0,0,0,0,0,0,0]

count = 0
Iteration = 1

user_search_term = input("What is the word you would like to search for? ")

while count < 10: 
    
    currentwebsite = Websites[count].read()

    term_search = currentwebsite.count (user_search_term)
    a = currentwebsite.count ("<a")    
    Outbound_links.append (a)
    term_count[count]= term_search
    count2 = 0 
    
    for item_search in Website_search:

        search_term = item_search
        b = currentwebsite.count(search_term)
        if b > 0:
            Website_links[count2].append(count)
            
        Inbound_links[count2] = Inbound_links[count2] + b
        count2 = count2 + 1
          
    count = count + 1 



currentPageranks = [0,0,0,0,0,0,0,0,0,0]
unstable = True

while unstable == True :

        time.sleep(0.5)
        print ("Iteration number", Iteration)
        
        Pagerankselection = [(PagerankA / Outbound_links[0]),(PagerankB / Outbound_links[1]),(PagerankC / Outbound_links[2]),
                         (PagerankD / Outbound_links[3]),(PagerankE / Outbound_links[4]),(PagerankF / Outbound_links[5]),
                         (PagerankG / Outbound_links[6]),(PagerankH / Outbound_links[7]),(PagerankI / Outbound_links[8]),
                         (PagerankJ / Outbound_links[9])]

   
        currentPagerankA = PagerankA
        currentPageranks[0] = currentPagerankA
        PagerankA = 0
        for item in (PagerankA_in):
            PagerankA = PagerankA + (Pagerankselection[item])
        PagerankA = (1-0.85) + 0.85*(PagerankA)
        PagerankA = round(PagerankA,4)

#####################################################################################################################################################################################################################################################

        currentPagerankB = PagerankB
        currentPageranks[1] = currentPagerankB
        PagerankB = 0
        for item in (PagerankB_in):
            PagerankB = PagerankB + (Pagerankselection[item])
        
        PagerankB = (1-0.85) + 0.85*(PagerankB)
        PagerankB = round(PagerankB,4)


#####################################################################################################################################################################################################################################################    

        currentPagerankC = PagerankC
        currentPageranks[2] = currentPagerankC
        PagerankC = 0
        for item in (PagerankC_in):
            PagerankC = PagerankC + (Pagerankselection[item])
        PagerankC = (1-0.85) + 0.85*(PagerankC)
        PagerankC = round(PagerankC,4)


#####################################################################################################################################################################################################################################################

        currentPagerankD = PagerankD
        currentPageranks[3] = currentPagerankD
        PagerankD = 0
        for item in (PagerankD_in):
            PagerankD = PagerankD + (Pagerankselection[item])
        
        PagerankD = (1-0.85) + 0.85*(PagerankD)
        PagerankD = round(PagerankD,4)


#####################################################################################################################################################################################################################################################

        currentPagerankE = PagerankE
        currentPageranks[4] = currentPagerankE
        PagerankE = 0
        for item in (PagerankE_in):
            PagerankE = PagerankE + (Pagerankselection[item])
        
        PagerankE = (1-0.85) + 0.85*(PagerankE)
        PagerankE = round(PagerankE,4)


#####################################################################################################################################################################################################################################################

        
        currentPagerankF = PagerankF
        currentPageranks[5] = currentPagerankF
        PagerankF = 0
        for item in (PagerankF_in):
            PagerankF = PagerankF + (Pagerankselection[item])
        
        PagerankF = (1-0.85) + 0.85*(PagerankF)
        PagerankF = round(PagerankF,4)


#####################################################################################################################################################################################################################################################        

        currentPagerankG = PagerankG
        currentPageranks[6] = currentPagerankG
        PagerankG = 0
        for item in (PagerankG_in):
            PagerankG = PagerankG + (Pagerankselection[item])
        
        PagerankG = (1-0.85) + (0.85*PagerankG)
        PagerankG = round(PagerankG,4)


#####################################################################################################################################################################################################################################################        

        currentPagerankH = PagerankH
        currentPageranks[7] = currentPagerankH
        PagerankH = 0
        for item in (PagerankH_in):
            PagerankH = PagerankH + (Pagerankselection[item])
        PagerankH = (1-0.85) + (0.85*PagerankH)
        PagerankH = round(PagerankH,4)


#####################################################################################################################################################################################################################################################        

        currentPagerankI = PagerankI
        currentPageranks[8] = currentPagerankI
        PagerankI = 0
        for item in (PagerankI_in):
            PagerankI = PagerankI + (Pagerankselection[item])
        
        PagerankI = (1-0.85) + (0.85*PagerankI)
        PagerankI = round(PagerankI,4)


#####################################################################################################################################################################################################################################################        

        currentPagerankJ = PagerankJ
        currentPageranks[9] = currentPagerankJ
        PagerankJ = 0
        for item in (PagerankJ_in):
            PagerankJ = PagerankJ + (Pagerankselection[item])
        
        PagerankJ = (1-0.85) + (0.85*PagerankJ)
        PagerankJ = round(PagerankJ,4)


#####################################################################################################################################################################################################################################################        


        Pageranks = (PagerankA , PagerankB , PagerankC , PagerankD, PagerankE, PagerankF , PagerankG , PagerankH , PagerankI , PagerankJ)
        Iteration = Iteration + 1
        
        for item in Pageranks:
            print (round(item,4))

        if  currentPagerankA == PagerankA and currentPagerankB == PagerankB and currentPagerankC == PagerankC and\
            currentPagerankD == PagerankD and currentPagerankE == PagerankE and currentPagerankF == PagerankF and\
            currentPagerankG == PagerankG and currentPagerankH == PagerankH and currentPagerankI == PagerankI and\
            currentPagerankJ == PagerankJ:
                
                
                unstable = False
                print ("The total number of iterations was", Iteration - 1)


Page1_1st_rank  = term_count[0] + PagerankA
Page2_1st_rank  = term_count[1] + PagerankB
Page3_1st_rank  = term_count[2] + PagerankC
Page4_1st_rank  = term_count[3] + PagerankD
Page5_1st_rank  = term_count[4] + PagerankE
Page6_1st_rank  = term_count[5] + PagerankF
Page7_1st_rank  = term_count[6] + PagerankG
Page8_1st_rank  = term_count[7] + PagerankH
Page9_1st_rank  = term_count[8] + PagerankI
Page10_1st_rank = term_count[9] + PagerankJ

Output_Terms = ["Page1.HTML" , "Page2.HTML" , "Page3.HTML" , "Page4.HTML" , "Page5.HTML" , "Page6.HTML" , "Page7.HTML" , "Page8.HTML", "Page9.HTML" , "Page10.HTML"]

First_sort_positions = [Page1_1st_rank , Page2_1st_rank , Page3_1st_rank , Page4_1st_rank , Page5_1st_rank,
                        Page6_1st_rank , Page7_1st_rank , Page8_1st_rank , Page9_1st_rank , Page10_1st_rank]

First_sort_positions = sorted(First_sort_positions , reverse= True )

Page1_index = First_sort_positions.index(Page1_1st_rank)
Page2_index = First_sort_positions.index(Page2_1st_rank)
Page3_index = First_sort_positions.index(Page3_1st_rank)
Page4_index = First_sort_positions.index(Page4_1st_rank)
Page5_index = First_sort_positions.index(Page5_1st_rank)
Page6_index = First_sort_positions.index(Page6_1st_rank)
Page7_index = First_sort_positions.index(Page7_1st_rank)
Page8_index = First_sort_positions.index(Page8_1st_rank)
Page9_index = First_sort_positions.index(Page9_1st_rank)
Page10_index = First_sort_positions.index(Page10_1st_rank)

Indexes = [Page1_index , Page2_index , Page3_index , Page4_index , Page5_index ,
           Page6_index , Page7_index , Page8_index , Page9_index , Page10_index]

count3 = 0

while count3 < 10:
    New_Output_Terms[Indexes[count3]] = Output_Terms[count3]
    count3 = count3 + 1

#print (New_Output_Terms)

for item in New_Output_Terms:
    print (item)
