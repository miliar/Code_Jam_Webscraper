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
        int N, P;
        cin >> N >> P;
        int R[50];
        int Q[50][50];
        for (int n = 0; n < N; ++n) {
            cin >> R[n];
        }
        int LowCounts[50][50] = {};
        int UpCounts[50][50] = {};
        for (int n = 0; n < N; ++n) {
            for (int p = 0; p < P; ++p) {
                cin >> Q[n][p];
            }
            sort(Q[n], Q[n] + P);
        }
        for (int n = 0; n < N; ++n) {
            for (int p = 0; p < P; ++p) {
                int q = Q[n][p];
                int r = R[n];
                int cmax = 10*q/9/r;
                int cmin = 10*q/11/r;
                int a = cmin*11*r;
                if (a != 10*q) {
                    ++cmin;
                }
                if (cmax >= cmin) {
                    LowCounts[n][p] = cmin;
                    UpCounts[n][p] = cmax;
                }
                
//                int c1 = q / R[n];
//                int c2 = c1 + 1;
//                if (q * 100 <= 110 * c1 * R[n]) {
//                    LowCounts[n][p] = c1;
//                }
//                if (q * 100 >= 90 * c2 * R[n]) {
//                    UpCounts[n][p] = c2;
//                } else {
//                    UpCounts[n][p] = LowCounts[n][p];
//                }
//                if (LowCounts[n][p] == 0) {
//                    LowCounts[n][p] = UpCounts[n][p];
//                }
            }
        }
        int res = 0;
        bool s[50] = {};
        for (int p = 0; p < P; ++p) {
            int low = LowCounts[0][p];
            int up = UpCounts[0][p];
            if (low > 0) {
                if (N > 1) {
                    for (int p2 = 0; p2 < P; ++p2) {
                        if (!s[p2]) {
                            int low2 = LowCounts[1][p2];
                            int up2 = UpCounts[1][p2];
                            if ((low >= low2 && low <= up2) || (up >= low2 && up <= up2) ||
                                (low2 >= low && low2 <= up) || (up2 >= low && up2 <= up)) {
                                ++res;
                                s[p2] = true;
                                break;
                            }
                        }
                    }
                    
//                    for (int n = 1; n < N; ++n) {
//                        
//                    }
                } else {
                    ++res;
                }
            }
        }
        
        
        cout << "Case #" << cas << ": " << res << endl;
    }
    return 0;
}
