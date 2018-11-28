//
//  main.cpp
//  Problem-B_Tidy Numbers
//
//  Created by Akram AbdAlAziz on 4/8/17.
//  Copyright © 2017 Akram AbdAlAziz. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    // insert code here...
    string line;
    unsigned long long number, lastTidyNumber;
    unsigned int caseN = 1;
    
    ifstream in("input.in");
    ofstream out("output.out");
    
    getline(in, line);
    cout << "trials = " << line << endl;
    
    int i = stoi(line);
    for (; i > 0 ; i--)
    {
        lastTidyNumber = 0;
        
        getline(in, line);
        number = stoll(line);
        
        cout << line << "    ";
        
        if (line.length() != 1) {
            for (int j = 1; j < line.length(); j++) {
                if (line[j-1] > line[j]) {
                    line[j-1] -= 1;
                    for (int k = j; k < line.length(); k++) {
                        line[k] = '9';
                    }
                    j = 0;
                }
            }
        }

        
        lastTidyNumber = stoll(line);
        
        cout << "Case #" << caseN << ": " << lastTidyNumber << endl;
        out << "Case #"<< caseN <<": " << lastTidyNumber << endl;
        
        caseN++;
    }
    
    in.close();
    out.close();
    
    return 0;
}
