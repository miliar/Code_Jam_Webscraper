//
//  main.cpp
//  tidy
//
//  Created by Chris M on 4/8/17.
//  Copyright © 2017 emq. All rights reserved.
//

//
//  main.cpp
//  codesss
//
//  Created by Chris M on 4/7/17.
//  Copyright © 2017 emq. All rights reserved.
//

#include <iostream>
#include <iostream>
#include <sstream>
#include <string>
#include <fstream>
#include <stdint.h>
#include <unistd.h>
#include <math.h>

#include <stdio.h>      /* printf */
#include <assert.h>


#define ha //

// 64bitoperations need 32 bit max numbers


using namespace std;

string testcases ;
long double Distance ;
long double times[2000] ;
long double positions[2000] ;
long double accel[2000] ;
int pos[1000] ;

int main(int argc, const char * argv[]) {
    // insert code here...
    std::ifstream infile("/Users/AQTL/Desktop/codejam/in.txt");
    freopen("/Users/AQTL/Desktop/codejam/out.txt","w",stdout);
    std::getline(infile, testcases) ; // read in string number of test cases
    std::istringstream iss(testcases);
    int N ;
    iss >> N ;
    fprintf(stderr,"\n");
    fprintf(stderr,"there are %d tests in this guy\n",N);
    
    
    for(int n=0;n<N ;n++)
    {
        
        std::getline(infile, testcases) ; // read in the pattern
        std::istringstream issy(testcases);
        
        string FULL ;
        string pattern = "";
        string number_remains ;
        int numbers ;
        issy >> FULL ;
        
   
        
        fprintf(stderr, "Full string %s numbers %d \n",FULL.c_str(),numbers );
        
        for (int x=0;x<FULL.length();x++)
        {
            pos[x] = stoi(FULL.substr(x,1));
        }
       
        // skip this if lenght < 2
        // do this FULL.length() times
        if (FULL.length()> 1)
        {
        for ( int exess = 0 ; exess < FULL.length() ; exess ++)
        {
        for (int x=0;x<FULL.length();x++)
        {
            if ( pos[FULL.length()-1-x] < pos[FULL.length()-2-x] )
            {
                pos[FULL.length()-2-x] = pos[FULL.length()-2-x]  -1 ;
                for (long  rer = FULL.length()-1-x ; rer < FULL.length() ; rer++ )
                {
                    pos [rer] = 9 ;
                }
                
               
                
                
           }
            
        }
        }
        }
        printf("Case #%d: ",n+1);
        bool leading = false ;
        for (int x=0;x<FULL.length();x++)
        {
            if (pos[x] > 0) leading = true ;
            if (leading) printf("%d",pos[x]);
        }
        printf("\n");
        
        
        
        
        
        
    }
    return 0;
    
}
