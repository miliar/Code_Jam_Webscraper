//
//  main.cpp
//  CodeJam.0.Pancake
//
//  Created by David Song on 4/7/17.
//  Copyright © 2017 David Song. All rights reserved.
//

#include <iostream>
using std::string;
using std::cin;
using std::cout;
using std::endl;


string flip(string s, int k) {
    for (int i = 0; i < k; i++) {
        if (s[i] == '+') s[i] = '-';
        else s[i] = '+';
    }
    return s;
}

int count(string s, int k) {
    if (s.length() < k) {
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != '+') return -100;
        }
        return 0;
    }
    else if (s[0] == '+') {
        return count(s.substr(1, s.length() - 1), k);
    }
    else {
        return 1 + count(flip(s, k), k);
    }
    return 0;
}

int main(int argc, const char * argv[]) {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string str; int k;
        cin >> str >> k;
        int c = count(str, k);
        if (c < 0) {
            cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
        }
        else {
            cout << "Case #" << i + 1 << ": " << c << endl;
        }
    }
}
