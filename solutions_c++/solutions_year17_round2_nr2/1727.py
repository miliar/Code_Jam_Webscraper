/* 
 * File:   main.cpp
 * Author: mehmetfatihuslu
 *
 * Created on April 12, 2014, 4:56 PM
 */

#include <cstdlib>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <math.h>
#include <iomanip>
#include <sstream>

using namespace std;

int main(int argc, char** argv) {

    fstream inputFile, outputFile, logFile;
    int T,N;  
    
    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);       
    logFile.open("log",ios::out);       
    
    inputFile >> T;
    
    
    for(int dongu=1; dongu<=T; dongu++) {   
        
        inputFile>>N;
        int *C = new int[6];
        
        inputFile>>C[0]>>C[1]>>C[2]>>C[3]>>C[4]>>C[5];
               
        outputFile << "Case #"<<dongu <<": ";
        
        if(C[0]+C[2]<C[4] || C[0]+C[4]<C[2] || C[2]+C[4]<C[0]){
                
            outputFile <<"IMPOSSIBLE"<<endl;                                                 
        }
        else{
         
            int max = 0;
            int unputable = -1;
            int first = -1;
            
            
            while(true){
                
                if(C[0]>=C[2] && C[0]>=C[4]) max = 0;
                if(C[2]>C[0] && C[2]>=C[4]) max = 2;
                if(C[4]>C[0] && C[4]>C[2]) max = 4;
                
                if(first == -1) first = max;
                
                if(unputable==0){
                    if(C[2]>C[4] || (C[2]==C[4] && first ==2)) max = 2;
                    if(C[4]>C[2] || (C[2]==C[4] && first ==4)) max = 4;
                    else max = 2;
                }
                else if(unputable==2){
                    if(C[0]>C[4] || (C[0]==C[4] && first ==0)) max = 0;
                    if(C[4]>C[0] || (C[0]==C[4] && first ==4)) max = 4; 
                    else max = 0;
                }
                else if(unputable==4){
                    if(C[0]>C[2] || (C[2]==C[0] && first ==0)) max = 0;
                    if(C[2]>C[0] || (C[2]==C[0] && first ==2)) max = 2;
                    else max = 0;
                }
                
                cout<<unputable<<" "<<max<<endl;
                
                if(max == 0){
                    outputFile<<"R";
                    unputable = 0;
                    C[0]--;
                }    
                else if(max == 2){
                    outputFile<<"Y";
                    unputable = 2; 
                    C[2]--;
                }
                else if(max == 4){
                    outputFile<<"B";
                    unputable = 4; 
                    C[4]--;
                }
                if(C[0]==0 && C[2]==0 && C[4]==0) break;
            }//*/
            outputFile <<endl;
        }
                
    }

    return 0;
}