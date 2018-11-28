//
//  main.cpp
//  Problem-A_Oversized Pancake Flipper
//
//  Created by Akram AbdAlAziz on 4/8/17.
//  Copyright © 2017 Akram AbdAlAziz. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    // insert code here...
    string line, flipperSize;
    unsigned long long minNumberOfTimes;
    
    int caseN = 1, kSize;
    bool sFlag;
    
    ifstream in("input.in");
    ofstream out("output.out");
    
    getline(in, line);
    cout << "trials = " << line << endl;
    
    int i = stoi(line);
    for (; i > 0 ; i--)
    {
        string pPattern, cPattern;
        minNumberOfTimes = 0;
        sFlag = true;
        
        getline(in, line, ' ');
        
        getline(in, flipperSize);
        kSize = stoi(flipperSize);
        
        cout << line << ' ' << kSize << "    ";
        
        while (1)
        {
            cPattern = line;
            string::size_type pos = string::npos;
            for (int j = 0; j < line.length(); j++) {
                if (line[j] == '-') {
                    pos = j;
                }
            }
            
            if (pos == string::npos)
                break;
            else
            {
                if (pos < kSize - 1)
                    pos = kSize - 1;
                
                for (int i = 0; i < kSize; i++) {
                    if (line[pos - i] == '+')
                        line[pos - i] = '-';
                    else if (line[pos - i] == '-')
                        line[pos - i] = '+';
                }
                minNumberOfTimes++;
                
                if (pPattern == line) {
                    break;
                }
                if(sFlag)
                    pPattern = cPattern;
                
                sFlag = !(sFlag);
            }
            
        }
        
        if (pPattern == line) {
            cout << "Case #" << caseN << ": IMPOSSIBLE" << endl;
            out << "Case #"<< caseN <<": IMPOSSIBLE" << endl;
        }
        else {
            cout << "Case #" << caseN << ": " << minNumberOfTimes << endl;
            out << "Case #"<< caseN <<": " << minNumberOfTimes << endl;
        }
        
        caseN++;
    }
    
    in.close();
    out.close();
    
    return 0;
}
