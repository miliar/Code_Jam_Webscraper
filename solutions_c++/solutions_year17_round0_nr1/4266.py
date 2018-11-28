//
//  main.cpp
//  Oversized Pancake Flipper
//
//  Created by Bill Zeng on 2017-04-08.
//  Copyright © 2017 Bill Zeng. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
#include <queue>
#include <stack>
#include <iostream>
#include <fstream>
using namespace std;
int t;

int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
    fin >> t;
    for(int q = 1; q <= t; q++){
        string s;
        int k, ans = 0;
        fin >> s >> k;
        for(int i = 0; i < s.length() - k + 1; i++){
            if(s[i] == '-'){
                ans++;
                for(int j = i; j < i + k; j++){
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }
        bool flag = true;
        for(int i = (int)s.length()-k; i < s.length(); i++){
            if(s[i] == '-')
                flag = false;
        }
        if(!flag)
            fout << "Case #" << q << ": IMPOSSIBLE\n";
        else
            fout << "Case #" << q << ": " << ans << "\n";
    }
    return 0;
}
