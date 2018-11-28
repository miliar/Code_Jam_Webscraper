//
//  main.cpp
//  CodeJamSandbox
//
//  Created by Maxime Tenth on 4/8/17.
//  Copyright © 2017 Maxime Tenth. All rights reserved.
//

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <fstream>

using namespace std;

int checkOnesCase(string word){
    size_t len = word.length();
    
    for (size_t i = 0; i < len; i++) {
        if(word[i] == '0'){
            return 1;
        }
        if(word[i] != '1'){
            return 0;
        }
    }
    return 0;
}
int cases = 0;
void processLine(vector<string> words, int lineNum) {
    if(lineNum == 0) {
        return;
    }
    cout << "Case #" << lineNum << ": ";
    
    string word = words[0];
    size_t len = word.length();
    
    if(checkOnesCase(word)){
        for (size_t i = 1; i < len; i++) {
            cout << 9;
        }
    }else{
        int prev = word[0];
        size_t nines = 0;
        for (size_t i = 1; i < len; i++) {
            int n = word[i];
            if(prev > n){
                nines = i;
                break;
            }
            prev = n;
        }
        if(nines){
            word[nines-1]--;
            if(nines > 1){
                for (long i = nines-2; i >= 0 && word[i] > word[i+1]; i--) {
                    word[i]--;
                    nines = i+1;
                }
            }
            for (size_t i = nines; i < len; i++) {
                word[i] = '9';
            }
        }
        cout << word;
    }
    cout << endl;
}

int main(int argc, const char * argv[]) {
    string line;
    for(int i = 0 ; getline(std::cin, line) ; i++){
        vector<string> v;
        istringstream iss(line);
        while (iss) {
            string word;
            iss >> word;
            if(word != ""){
                v.push_back(word);
            }
        }
        processLine(v, i);
    }
    return 0;
}

