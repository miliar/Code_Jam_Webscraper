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
    int T,D,N;  
    
    inputFile.open("input",ios::in);
    outputFile.open("output",ios::out);       
    logFile.open("log",ios::out);       
    
    inputFile >> T;

    
    for(int dongu=1; dongu<=T; dongu++) {   
        
        inputFile>>D>>N;
        
        int* K = new int[N];
        int* S = new int[N];               
        
        double lastArrive = 0;
        
        for(int i=0;i<N;i++){
            
            inputFile>>K[i]>>S[i];
            
            double t = (double)(D - K[i])/S[i];
            if(t>lastArrive)
                lastArrive = t;
        }
        
        double maxSpeed =  (double)D/lastArrive;
        
        outputFile << "Case #"<<dongu <<": "<<setiosflags(ios::fixed)<<setprecision(7)<<maxSpeed<<endl;                                                 
                
    }

    return 0;
}