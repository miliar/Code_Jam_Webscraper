//
//  main.cpp
//  cont
//
//  Created by v on 08/04/17.
//  Copyright © 2017 Vladimir Berezkin. All rights reserved.
//
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
//  B
void decrease(string& N, size_t pos) {
    char& v = N[pos];
    if (v > '0') {
        --v;
        return;
    }
    v = '9';
    decrease(N, pos-1);
}
void check(string& N) {
    auto len = N.length();
    int prev = 0;
    int pos = 0;
    for (char c : N) {
        int n = c - '0';
        if (n < prev) {
            for(int i = pos; i < len; ++i) {
                N[i] = '9';
            }
            decrease(N, pos-1);
            check(N);
            break;
        }
        prev = n;
        ++pos;
    }
}
int main() {
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        string N;
        cin >> N;
        check(N);
        int i = 0;
        for (; i < N.length(); ++i) {
            if (N[i] != '0') {
                break;
            }
        }
        N = N.substr(i);
        cout << "Case #" << cas << ": " << N << endl;
    }
    return 0;
}
