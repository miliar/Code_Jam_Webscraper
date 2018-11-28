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
string pos[1000] ;

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
        issy >> FULL >> numbers ;
        
        bool madeit= true ;
        int flips = 0 ;
      
        fprintf(stderr, "Full string %s numbers %d \n",FULL.c_str(),numbers );
      
        for (int x=0;x<FULL.length();x++)
        {
          pos[x] = FULL.substr(x,1);
        }
        for (int x=0;x<FULL.length();x++)
        {
            if ( pos[x] == "-")
            {
                // if the remaining is less than spatula then we are done with impossibl
                if (FULL.length()-x  < numbers)
                {
                    fprintf(stderr,"Fail on tescase %d \n",n );
                    madeit = false ;
                    break ;
                }
                else
                {
                    //swap this guy and next numbers
                    flips++;
                    for ( int y = 0 ; y < numbers ; y++)
                    {
                        if (pos[x+y] == "-")
                        {
                            pos[x+y] = "+" ;
                        }
                        else
                        {
                            pos[x+y] = "-" ;
                        }
                    }
                }
            }
        }
        if (madeit)
        {
            fprintf(stderr,"passed on tescase %d \n",n );
            
            printf("Case #%d: %d\n",n+1,flips);
        }
        else
        {
        printf("Case #%d: IMPOSSIBLE\n",n+1);
        }
       
            
        
        
        
        
    }
    return 0;
    
}


// we don't care about Point 0
// we care about max speed at point 1
// after thaat we accellerate to try and meet or maintain speed for next

// v d*t


// quadratic formula
// x = - b +/- sqrt ( b^2 - 4ac ) / 2a





