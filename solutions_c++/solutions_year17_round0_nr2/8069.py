//
//  main.cpp
//  GoogleCodeJam
//
//  Created by Ivan Bylinkin on 4/7/17.
//  Copyright © 2017 Ivan Bylinkin. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

string read(ifstream &file);
void write(ofstream &file, string data);
void tidy(int caseT, ifstream &in, ofstream &out);

int main(){
    // MARK: Definitions
    ifstream input ("input.txt");
    ofstream output ("output.txt");
    
    // read T
    int T = stoi(read(input));
    
    // read the next T cases
    for (int i=0; i<T; i++){
        tidy(i+1,input,output);
    }
    
    // close files before ending program
    input.close();
    output.close();
    
    // exit
    return 0;
}

void tidy(int caseT, ifstream &in,ofstream &out){
    // read N
    unsigned long N = stol(read(in));
    //cout << N << endl;
    string output = "Case #"+to_string(caseT)+": ";
    
    // start at the largest number and count backwards until you hit a "tidy" number
    for (unsigned long i=N; i>0; i--){
        string nums = to_string(i);
        unsigned long numCount = nums.length();
        
        // if the largest number is only 1 number, then it's the winner
        if (numCount == 1){
            output += nums;
            write(out,output);
            break;
        }
        
        // otherwise, we have to check for "tidiness"
        bool tidyNum = true;
        int place = 0;
        for (unsigned long k=numCount-1; k>0; k--){
            int num = nums[k] - '0';
            int next = nums[k-1] - '0';
            if (num < next){
                // the number is out of place
                unsigned long sub = (num+1)*pow(10,place);
                unsigned long add = (next-num)*pow(10,place);
                
                if (i+add < N){
                    // add one to i to get back to the proper number next loop
                    i = i + add + 1;
                }
                else {
                    // add one to i to get back to the proper number next loop
                    i = i - sub + 1;
                }
                
                tidyNum = false;
                break;
            }
            // move the place up, if the next number is not a 0
            place++;
            if (num == 0 && (nums[k-1] - '0') == 0){
                place--;
            }
        }
        
        if (tidyNum){
            output += nums;
            write(out, output);
            break;
        }
    }
}

string read(ifstream &file){
    string line = "unable to open file";
    if (file.is_open()){
        line = "";
        getline(file,line);
    }
    return line;
}

void write(ofstream &file, string data){
    if (file.is_open()){
        file << data;
        file << "\n";
    }
}
