//
//  main.cpp
//  Codejam
//
//  Created by Duy DLM on 4/9/17.
//  Copyright © 2017 Duy DLM. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    
    int number;
    fin >> number;
    
    int check = 0;
    
    for (int j = 0; j < number; j++) {
        string s;
        fin >> s;
        int k;
        fin >> k;
        
        int c = 0;

        for (int i = 0; i <= s.length() - k; i++) {
            if (s[i] == '+') {
                continue;
            }
            c++;
            for (int j = 0; j < k; j++) {
                if (s[i+j] == '+') {
                    s[i+j] = '-';
                } else {
                    s[i+j] = '+';
                }
            }
        }
        cout << s;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '-') {
                fout << "Case #" << j+1 << ": " << "IMPOSSIBLE" << endl;
                check = 1;
                break;
            }
        }
        if (check == 0) {
            fout << "Case #" << j+1 << ": " << c << endl;
        }
        check = 0;
        
    }


    return 0;
}
