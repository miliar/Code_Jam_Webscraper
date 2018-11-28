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
    ifstream ifs("/Users/gongcheng/B-small-attempt2.in");
    ofstream ofs("/Users/gongcheng/output.txt");
    int caseNum;
    ifs >> caseNum;
    for (int i = 1; i <= caseNum; ++i) {
        string str;
        ifs >> str;
        string str2;
        if (str.length() == 1) {
            str2 = str;
        }
        else {
            bool f = false;
            for (int i = 1; i < str.length(); ++i) {
                if (str[i] > str[i - 1]) {
                    f = true;
                }
            }
            if (!f) {
                f = false;
                for (int i = 1; i < str.length(); ++i) {
                    if (str[i] != str[i - 1])
                        f = true;
                }
                if (!f) {
                    str2 = str;
                }
                else if (str[0] == '1') {
                    for (int i = 0; i < str.length() - 1; ++i) {
                        str2 += "9";
                    }
                }
                else {
                    str2 += str[0] - 1;
                    for (int i = 0; i < str.length() - 1; ++i) {
                        str2 += "9";
                    }
                }
            }
            else if (str[0] == '1') {
                bool flag = false;
                for (int i = 1; i < str.length(); ++i) {
                    if (str[i - 1] == '1' && str[i] == '0') {
                        flag = true;
                        break;
                    }
                }
                if (flag) {
                    for (int i = 0; i < str.length() - 1; ++i) {
                        str2 += "9";
                    }
                }
                else {
                    str2 += str[0];
                    for (int i = 1; i < str.length(); ++i) {
                        if (str[i] >= str2[i - 1]) {
                            str2 += str[i];
                        }
                        else {
                            str2[i - 1] = str2[i - 1] - 1;
                            for (; i < str.length(); ++i) {
                                str2 += "9";
                            }
                        }
                    }
                }
            }
            else {
                str2 += str[0];
                for (int i = 1; i < str.length(); ++i) {
                    if (str[i] >= str2[i - 1]) {
                        str2 += str[i];
                    }
                    else {
                        str2[i - 1] = str2[i - 1] - 1;
                        for (; i < str.length(); ++i) {
                            str2 += "9";
                        }
                    }
                }
            }
        }
        ofs << "Case #" << i << ": ";
        ofs << str2;
        ofs << endl;
    }
    return 0;
}

