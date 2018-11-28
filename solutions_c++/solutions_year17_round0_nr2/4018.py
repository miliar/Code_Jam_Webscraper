//
//  2017QB.cpp
//  CodeJam2017
//
//  Created by Ha Young Park on 08/04/2017.
//  Copyright © 2017 Ha Young Park. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int main(int argc, const char * argv[]) {
    ifstream fin;ofstream fout;fin.open("B-large.in");fout.open("B-large.out");

    unsigned T;
    fin >> T;
    for(unsigned i = 0; i < T; i++){
        unsigned long long N;
        fin >> N;
        
        fout << "Case #" << i + 1 << ": ";
        
        if(N < 10)
            fout << N;
        else{
            vector<int> digits;
            unsigned long long temp = N;
            while(temp != 0){
                digits.push_back(temp%10);
                temp /= 10;
            }
            unsigned pos = 0;
            while(pos + 1 < digits.size()){
                if(digits[pos] < digits[pos + 1]){
                    digits[pos + 1] -= 1;

                    for(int j = 0; j <= pos; j++)
                        digits[j] = 9;
                }
                pos++;
            }
            
            for(int k = digits.size() - 1; k >= 0; k--){
                if(digits[k] > 0)
                    fout << digits[k];
            }
        }
        
        
        
        fout << endl;
    }

    fout.close();fin.close();
    return 0;
}

