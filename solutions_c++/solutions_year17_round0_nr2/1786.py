//
//  main.cpp
//  CodeJam-qr-02
//
//  Created by 张云尧 on 2017/4/8.
//  Copyright © 2017年 张云尧. All rights reserved.
//

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(int argc, const char * argv[]) {
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    int t;
    in >> t;
    for (int i = 0; i < t; ++i) {
        string str;
        in >> str;
        int size = (int)str.size();
        int j;
        for (j = 0; j < size - 1; ++j)
            if (str[j] > str[j + 1])
                break;
        if (j != size - 1) {
            int tmp = str[j];
            for ( ; j > 0; --j)
                if (str[j - 1] != tmp)
                    break;
            --str[j];
            for (++j ; j < size; ++j)
                str[j] = '9';
        }
        for (j = 0; j < size; ++j)
            if (str[j] != '0')
                break;
        str = str.substr(j, size - j);
        out << "Case #" << i + 1 << ": " << str << endl;
    }
    return 0;
}
