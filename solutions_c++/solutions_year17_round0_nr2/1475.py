//
//  main.cpp
//  gcj_Qualification
//
//  Created by didi on 2017/4/8.
//  Copyright © 2017年 didi. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream in("/Users/didi/Desktop/gcj_Qualification/gcj_Qualification/B-large.in");
ofstream out("/Users/didi/Desktop/gcj_Qualification/gcj_Qualification/B-large.out");

void solve(int test){
    out << "Case #" << test << ": ";
    string str;
    in >> str;
    int i = 0;
    while (i<str.length() - 1){
        if (str[i] <= str [i+1]){
            i += 1;
            continue;
        }else{
            while (i > 0 && str[i-1] == str[i]) i--;
            str[i] -= 1;
            for (int j = i + 1; j < str.length(); j++){
                str[j] = '9';
            }
            break;
        }
    }
    for (int i = 0; i < str.length(); i++){
        if (str[i] == '0') continue;
        string ans = str.substr(i,str.length() - i);
        out << ans << endl;
        break;
    }
}

int main(int argc, const char * argv[]) {
    int test = 0,T;
    in >> T;
    while (test++<T){
        solve(test);
    }
    in.close();
    out.close();
    return 0;
}
