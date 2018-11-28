//
//  main.cpp
//  tolilets
//
//  Created by MrMarc on 4/8/17.
//  Copyright © 2017 emq. All rights reserved.
//

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
string  spot [ 100][100] ;
bool tag [101] ;


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
    
    string sample ;
    
    for(int n=0;n<N ;n++)
    {
        
        std::getline(infile, testcases) ; // read in the pattern
        std::istringstream issy(testcases);
        
        int R ;
        int C ;
        issy >> R  >> C  ;
        fprintf(stderr, "case %d  R %d  C%d  \n",n+1,R,C);
        for(int x = 0 ; x < R ; x++)
            
        {
            std::getline(infile, testcases) ; // read in the pattern
            std::istringstream issq (testcases);
            issq >> sample ;
            
            for (int y = 0 ; y < C ; y ++ )
            {
                spot[y][x] = sample.substr(y,1);
                fprintf(stderr, "%s",spot[y][x].c_str());
            }
            fprintf(stderr, "\n");
        }
        for ( int j = 0 ; j < 26 ; j ++ )
        {
            tag[j ] = false ;
            
        }
        
      
        
        
        
        for ( int j = 0 ; j < 26 ; j ++ )
        {
           
            bool startx = false ;
            bool starty = false ;
            bool letterfound = false ;
            bool endx = false ;
            bool endy = false ;
            
            int Istartx = 0;
            int Istarty = 0;
            int Iendx = 0;
            int Iendy = 0;
            string Sletter ;
            int Iletter  = 0;
            
            
            
            
            //find a box and fill it
            //find first ? or untagged Letter
            for(int x = 0 ; x < R ; x++)
            {
                for (int y = 0 ; y < C ; y ++ )
                {
                    char meme =spot[y][x][0] ;
                    int  value = (int)meme - 65 ;
                    if ( spot[y][x] == "?")
                    {
                        value = 100 ;
                        tag[100] = true ;
                    }
                    if ( spot[y][x] == "?" || (!letterfound && !tag[value])   )
                    {
                        if(!startx)
                        {
                            startx = true ;
                            Istartx = x ;
                        }
                        if (!starty)
                        {
                            starty = true;
                            Istarty = y ;
                        }
                        if (!letterfound && !tag[value] )
                        {
                            letterfound = true;
                            Sletter = spot[y][x] ;
                            Iletter = value ;
                        }
                    }
                    if (letterfound && value < 100 && value != Iletter)
                    {
                        if (!endy)
                        {
                            if (y >= Istarty)
                            {
                                
                            endy = true ;
                            Iendy = y;
                            }
                        }
                        if (endy && ! endx )
                        {
                            if (y < Iendy && y >= Istarty && x >= Istartx)
                            {
                                endx = true ;
                                Iendx = x ;
                            }
                        }
                            
                    }
                    
                }
                
                if (starty && !endy  && letterfound)
                {
                    Iendy = C ;
                    endy = true ;
                }
        
                
                
            }
            if (startx && !endx)
            {
                Iendx = R ;
                endx = true ;
            }
            if (startx)
            {
                for(int x = Istartx ; x < Iendx ; x++ )
                {
                    for(int y = Istarty ; y < Iendy ; y ++ )
                    {
                        spot[y][x] = Sletter ;
                    }
                }
                tag[Iletter] = true ;
            }
            
        
        }
        
        
        
        
        
        printf("Case #%d:\n",n+1);
        for(int x = 0 ; x < R ; x++)
            
        {
           for (int y = 0 ; y < C ; y ++ )
            {
                printf( "%s",spot[y][x].c_str());
            }
            printf("\n");
        }
        
        
       
        
        
    }
    return 0;
    
}