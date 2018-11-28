//
//  main.cpp
//  Tencent
//
//  Created by wang haozheng on 2017/4/2.
//  Copyright © 2017年 wang haozheng. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

string minus_one(string a){
    int l = (int)a.size();
    int i = 0;
    bool changed = false;
    int begin = l - 1;
    for (; i < l - 1; ++i){
        if(!changed && a[i] >= a[i + 1]) {
            begin = i;
            changed = true;
        }
        if (a[i] > a[i + 1]) {
            break;
        }
        if(a[i] < a[i + 1]) {
            begin = i;
            changed = false;
        }
    }
    if (i < l - 1) {
        --a[begin];
        for (int j = begin + 1; j < l; ++j) a[j] = '9';
        if (!begin && a[begin] == '0') a = a.substr(1, l - 1);
    }
    return a;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int t;
    ifstream fin("/Users/ezfxwhz/Downloads/B-large.in", ios::in);
    ofstream fout("/Users/ezfxwhz/Documents/Tencent/Tencent/out.out", ios::out);
    fin  >> t;
    for (int j = 0; j < t; ++j) {
        string s;
        fin >> s;
        s = minus_one(s);
        fout << "Case #" << j + 1 << ": " << s;
        if (j < t - 1) fout << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
