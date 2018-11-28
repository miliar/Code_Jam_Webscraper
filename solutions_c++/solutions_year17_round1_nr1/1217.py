//
//  main.cpp
//  cont
//
//  Created by v on 15/04/17.
//  Copyright © 2017 Vladimir Berezkin. All rights reserved.
//
#include <algorithm>
#include <bitset>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
int main() {
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        int R, C;
        cin >> R >> C;
        char M[26][26] = {0};
        for (int r = 0; r < R; ++r) {
            for (int c = 0; c < C; ++c) {
                cin >> M[r][c];
            }
        }
        for (int r = 0; r < R; ++r) {
            char fch = 0;
            char ch = 0;
            for (int c = 0; c < C; ++c) {
                if (M[r][c] != '?') {
                    ch = M[r][c];
                    if (!fch) {
                        fch = ch;
                    }
                } else if (ch) {
                    M[r][c] = ch;
                }
            }
            if (fch) {
                for (int c = 0; c < C && M[r][c] == '?'; ++c) {
                    M[r][c] = fch;
                }
            }
        }
        int frf = -1;
        int rf = -1;
        for (int r = 0; r < R; ++r) {
            if (M[r][0] == '?') {
                if (rf >= 0) {
                    copy_n(M[rf], C, M[r]);
                }
            } else {
                rf = r;
                if (frf < 0) {
                    frf = r;
                }
            }
        }
        for (int r = 0; r < R && M[r][0] == '?'; ++r) {
            copy_n(M[frf], C, M[r]);
        }
        cout << "Case #" << cas << ": " << endl;
        for (int r = 0; r < R; ++r) {
            cout << M[r] << endl;
        }
    }
    return 0;
}
