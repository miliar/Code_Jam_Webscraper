//
//  main.cpp
//  CodeJam2017
//
//  Created by Ha Young Park on 08/04/2017.
//  Copyright © 2017 Ha Young Park. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main(int argc, const char * argv[]) {
    ifstream fin;ofstream fout;fin.open("A-large.in");fout.open("A-large.out");
    
    unsigned T, K;
    fin >> T;
    for(unsigned i = 0; i < T; i++){
        int F = 0;
        string S;
        fin >> S;
        fin >> K;
       
        unsigned pos = 0;
        while(F >= 0){
            
            while(S[pos] == '+')
                pos++;

            if(pos + K <= S.length()){
                for(unsigned i = 0; i < K; i++)
                {
                    if(S[pos + i] == '-')
                        S[pos + i] = '+';
                    else
                        S[pos + i] = '-';
                }
                F++;
            }
            else if(pos == S.length())
                break;
            else{
                F = -1;
                break;
            }
        }
        
        fout << "Case #" << i + 1 << ": ";
        if(F < 0)
            fout << "IMPOSSIBLE" << endl;
        else
            fout << F << endl;
    }
    
    fout.close();fin.close();
    return 0;
}

