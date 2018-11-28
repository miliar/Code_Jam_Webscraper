//
//  main.cpp
//  tolilets
//
//  Created by Chris M on 4/8/17.
//  Copyright © 2017 emq. All rights reserved.
//

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
long long  spaces [1000000];
long long  number [1000000];
int active [1000000] ;


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
        
        long  FULL ;
        string pattern = "";
        string number_remains ;
        long  numbers ;
        issy >> FULL >> numbers ;
        
        
        
        fprintf(stderr, "Full string %ld numbers %ld \n",FULL ,numbers );
        for (int x = 0 ; x < 1000000  ;x++)
        {
            spaces[x] = 0 ;
            number[x] = 0 ;
        }
        
        spaces[0] = FULL ;
        number[0] = 1 ;
        active [0] = 1 ;
        //numbers is how many left to place ;
        numbers = numbers - 1 ;
        long long spotsize = 0 ;
        bool done = false ;
        while (!done )
        {
            // find the bigest active number
            long long biggest = 0 ;
            long long big_index = 0 ;
            for (long x=0 ; x < 1000000 ; x++ )
            {
                if ((spaces[x] > biggest) && (number[x] > 0) )
                {
                    biggest = spaces[x] ;
                    big_index = x;
                }
            }
            if ( numbers < number [big_index]) {
      // if the nubmers to place is less that the number of spaces then we are done
                spotsize = biggest ;
                break ;
            }
           // find the numbers for the the spot we are going to use
            long long divider = spaces[big_index] - 1 ;
            long long first = 0 ;
            long long second = 0 ;
            bool first_done = false ;
            bool second_done = false  ;
            if (divider%2 == 0 )
            {
                first = divider / 2 ;
                second = first  ;
                
            }
            else
            {
                first =  (divider - 1 ) / 2  ;
                second = first + 1 ;
            }
            
            if ( first == 0) first_done = true ;
            if (second == 0 ) second_done = true ;
      // otherwise dind the 2 numbers we are diving into
      // increment those spaces by the by number
            for (long x=0 ; x < 1000000 ; x++ )
            {
                if (!first_done) {
                if (spaces[x] == first  )
                {
                    number [x] = number[x] + number [big_index] ;
                    first_done = true ;
                    }
                }
                if (!second_done) {
                    if (spaces[x] == second  )
                    {
                        number [x] = number [x] + number [big_index] ;
                        second_done = true ;
                    }
                }
                if (second_done && first_done )
                {
                    break ;
                }
                
                
            }
            
            if (!second_done || !first_done)
            {
                for (long x=0 ; x < 1000000 ; x++ )
                {
                    if (!first_done)
                    {
                       if (number[x] == 0)
                       {
                           number[x] = number [big_index] ;
                           spaces[x] = first ;
                           first_done = true ;
                           if (first == second)
                           {
                               number[x] = number [x]*2 ;
                               second_done = true ;
                           }
                               
                       }
                    }
                    if (!second_done)
                    {
                        if (number[x] == 0)
                        {
                            number[x] = number [big_index] ;
                            spaces[x] = second  ;
                            second_done = true ;
                        }
                    }
                    if (second_done && first_done )
                    {
                        break ;
                    }
                    if (x == 999999)
                    {
                        fprintf(stderr, "********overfloww  ********************\n\n");
                    }
                
                }
                
                
            }
            
            numbers = numbers - number [big_index] ;
            number [ big_index ] = 0 ;
            
      // decrement the current to 0 and macke incative
       // loop
      //
        }
        long long divider = spotsize - 1 ;
        long long first = 0 ;
        long long second = 0 ;
        
        if (divider%2 == 0 )
        {
            first = divider / 2 ;
            second = first  ;
            
        }
        else
        {
            first =  (divider - 1 ) / 2  ;
            second = first + 1 ;
        }
        
        
        
        
        printf("Case #%d: %lld %lld",n+1,second,first);
        
        printf("\n");
        fprintf(stderr, "the spotsize is  %lld\n\n",spotsize);
        
        
        
        
        
    }
    return 0;
    
}
