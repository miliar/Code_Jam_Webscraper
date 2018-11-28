//
//  main.cpp
//  code jam
//
//  Created by Mahmoud Rashad on 4/8/17.
//  Copyright © 2017 Mahmoud Rashad. All rights reserved.
//

#include <iostream>

using namespace std;

void flip (string &s, int i, int k) {
    int end = i+k;
    while (i < end) {
        if (s[i] == '+') {
            s[i] = '-';
        }
        else
            s[i] = '+';
        i++;
    }
}

int main() {
    
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    int k, j = 1;
    string s;
    while (j <= t) {
        cin >> s >> k;
        int i = 0, res = 0;
        while (i <= s.size()-k) {
            if (s[i] == '-') {
                flip (s, i, k);
                res++;
            }
            i++;
        }
        bool flag = true;
        while (i < s.size()) {
            if (s[i] == '-') {
                flag = false;
            }
            i++;
        }
        if (flag) {
            cout << "Case #" << j << ": " << res << '\n';
        }
        else
            cout << "Case #" << j << ": IMPOSSIBLE\n";
        j++;
    }
    
    return 0;
}
