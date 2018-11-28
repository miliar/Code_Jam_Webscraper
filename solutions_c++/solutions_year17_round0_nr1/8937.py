//
//  main.cpp
//  codejam
//
//  Created by Gong Cheng on 4/8/17.
//  Copyright © 2017 Gong Cheng. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream ifs("/Users/gongcheng/A-large.in");
    ofstream ofs("/Users/gongcheng/output.txt");
    int caseNum;
    ifs >> caseNum;
    for (int i = 1; i <= caseNum; ++i) {
        string str;
        int num;
        int count = 0;
        bool flag = true;
        ifs >> str >> num;
        size_t ind;
        size_t len = str.length();
        while ((ind = str.find_first_of("-")) != string::npos) {
            cout << str << endl;
            if (len - ind < num) {
                flag = false;
                break;
            }
            for (size_t j = ind; j < ind + num; ++j) {
                if (str[j] == '+') {
                    str[j] = '-';
                }
                else {
                    str[j] = '+';
                }
            }
            ++count;
            cout << str << endl;
        }
        
        ofs << "Case #" << i << ": ";
        if (!flag) {
            ofs << "IMPOSSIBLE";
        }
        else
            ofs << count;
        ofs << endl;
    }
    return 0;
}

