//
//  main.cpp
//  cont
//
//  Created by v on 08/04/17.
//  Copyright © 2017 Vladimir Berezkin. All rights reserved.
//
#include <algorithm>
#include <bitset>
#include <iostream>
#include <set>
#include <vector>
using namespace std;
//  C
int64_t high_digit(int64_t n) {
    int64_t i = int64_t(1) << 62;
    for (; !(n&i); i>>=1) {
    }
    return i;
}

int main() {
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        int64_t N, K;
        cin >> N >> K;
        //  Slow
//        vector<bool> b(N);
//        for (int i = 0; i < K; ++i) {
//            int begin = 0;
//            int end = (int)N;
//            int len = 0;
//            for (int j = 0; j < N; ++j) {
//                if (!b[j]) {
//                    int k = j + 1;
//                    for (; k < N; ++k) {
//                        if (b[k]) {
//                            if (k - j > len) {
//                                len = k - j;
//                                begin = j;
//                                end = k;
//                            }
//                            j = k;
//                            break;
//                        }
//                    }
//                    if (k == N && k - j > len) {
//                        len = k - j;
//                        begin = j;
//                        end = k;
//                        j = k;
//                    }
//                }
//            }
//            int pos = (begin+end) / 2;
//            b[pos] = true;
//            if (i == K - 1) {
//                int mx = pos - begin;
//                int mn = end - pos - 1;
//                cout << "Case #" << cas << ": " << mx << " " << mn << endl;
//            }
//        }
        
        //  Middle
//        multiset<int, greater<int>> sizes;
//        sizes.insert(int(N));
//        for (int i = 0; i < K; ++i) {
//            auto p = sizes.begin();
//            int n = *p;
//            sizes.erase(p);
//            int mx, mn;
//            if ((n%2) == 0) {
//                mx = n / 2;
//                mn = (n-2) / 2;
//            } else {
//                mx = mn = (n-1) / 2;
//            }
//            if (mx > 0) {
//                sizes.insert(mx);
//            }
//            if (mn > 0) {
//                sizes.insert(mn);
//            }
//            if (i == K-1) {
//                cout << "Case #" << cas << ": " << mx << " " << mn << endl;
//            }
//        }
        
        //  Fast
        int64_t mn = 0;
        int64_t mx = 0;
        int64_t hd = high_digit(K);
        int64_t emptiesRanges = hd;
        int64_t low = hd - int64_t(1);
        int64_t left = K - low;
        int64_t emptiesStalls = N - low;
        
        int64_t minEmptiesWidth = emptiesStalls / emptiesRanges;
        if (minEmptiesWidth > 0) {
            int64_t over = emptiesStalls - minEmptiesWidth * emptiesRanges;
            int64_t w = minEmptiesWidth;
            if (left <= over) {
                ++w;
            }
            if (w%int64_t(2)) {
                mn = mx = (w-int64_t(1))/int64_t(2);
            } else {
                mx = (w)/int64_t(2);
                mn = (w-int64_t(2))/int64_t(2);
            }
        }
        cout << "Case #" << cas << ": " << mx << " " << mn << endl;
    }
    return 0;
}
