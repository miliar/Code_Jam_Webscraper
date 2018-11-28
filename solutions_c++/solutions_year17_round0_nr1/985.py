//
//  main.cpp
//  cont
//
//  Created by v on 19/03/17.
//  Copyright © 2017 Vladimir Berezkin. All rights reserved.
//
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
//  A
int main() {
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        string S;
        int K;
        cin >> S >> K;
        bool b[1000];
        auto len = S.length();
        int i = 0;
        for (char c : S) {
            b[i++] = c == '+' ? 1 : 0;
        }
        int c = 0;
        for (int i = 0; i < len - K + 1; ++i) {
            if (!b[i]) {
                for (int j = 0; j < K; ++j) {
                    b[i+j] = !b[i+j];
                }
                ++c;
            }
        }
        bool ok = true;
        for (auto i = len - K + 1; i < len; ++i) {
            if (!b[i]) {
                ok = false;
                break;
            }
        }
        if (ok) {
            cout << "Case #" << cas << ": " << c << endl;
        } else {
            cout << "Case #" << cas << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}
