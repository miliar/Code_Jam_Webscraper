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
    
    for (int j = 0; j < number; j++) {
        string s;
        fin >> s;
        
        for (int i = (int)s.length() - 1; i > 0; i--)
        {
            int r = s[i] - '0';
            int l = s[i-1] - '0';
            if(r<l)
            {
                for(int j = i; j<s.length(); j++)
                {
                    s[j] = '9';
                }
                s[i-1]=s[i-1]-1;
            }
        }
        if(s[0] == '0')
        {
            s = s.substr(1);
        }
        cout << s;
        fout << "Case #" << j+1 << ": " << s << endl;
    }


    return 0;
}
