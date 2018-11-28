//
//  2017QC.cpp
//  CodeJam2017
//
//  Created by Ha Young Park on 08/04/2017.
//  Copyright © 2017 Ha Young Park. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;


int main(int argc, const char * argv[]) {
    ifstream fin;ofstream fout;fin.open("C-small-2-attempt0.in");fout.open("C-small-2-attempt0.out");
    
    unsigned T;
    fin >> T;
    for(unsigned i = 0; i < T; i++){
        unsigned long long N, K;
        fin >> N >> K;
        
        unsigned long long max = N;
        int j;
        for(j = 0; pow(2, j) <= K; j++)
            max /= 2;

        long long offset = N - max * pow(2, j) + 1;
        
        fout << "Case #" << i + 1 << ": ";
        
        if(K - pow(2, j-1) + 1 <= offset)
            fout << max;
        else
            fout << max - 1;
        
        fout << " ";
        if(K < offset)
            fout << max;
        else
            fout << max - 1;
        fout << endl;
        
    }
    
    fout.close();fin.close();
    return 0;
}
