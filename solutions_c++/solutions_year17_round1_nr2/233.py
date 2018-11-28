#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cmath>
#include <iomanip>
#include <string>
#include <cstdio>

using namespace std;

long long r[111];
long long a[111][111];
long long from[111][111];
long long to[111][111];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output_b_2.txt", "w", stdout);
    int Tests;
    cin >> Tests;
    for (int Test = 1; Test <= Tests; Test++) {
        cout << "Case #" << Test << ": ";
        int n, p;
        cin >> n >> p;
        for (int i = 0; i < n; i++) {
            cin >> r[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                cin >> a[i][j];
            }
            sort(a[i], a[i] + p);
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < p; j++) {
                long long lo = 0;
                long long hi = 2000000;
                while (lo + 1 < hi) {
                    long long mi = (lo + hi) / 2;
                    if (a[i][j] * 100 <= r[i] * mi * 110) {
                        hi = mi;
                    }
                    else {
                        lo = mi;
                    }
                }                
                from[i][j] = hi;                
                lo = 0;
                hi = 2000000;
                while (lo + 1 < hi) {
                    long long mi = (lo + hi) / 2;
                    if (a[i][j] * 100 >= r[i] * mi * 90) {
                        lo = mi;
                    }
                    else {
                        hi = mi;
                    }
                }
                to[i][j] = lo;
                //cout << a[i][j] << " " << r[i] * hi * 1.1 << endl;
                //cout << from[i][j] << " " << to[i][j] << ", ";
            }            
            //cout << endl;
        }
        
        for (int j = 0; j < p; j++) {
            long long M = -1;
            for (int i = 0; i < n; i++) {
                if (from[i][0] > M) {
                    M = from[i][0];
                }
            }
            int ok = true;
            for (int i = 0; i < n; i++) {
                if (to[i][0] < M) {
                    ok = false;
                }
            }

            if (ok) {
                for (int ii = 0; ii < n; ii++) {
                    for (int jj = 0; jj < p; jj++) {
                        from[ii][jj] = from[ii][jj + 1];
                        to[ii][jj] = to[ii][jj + 1];
                    }
                }
                ans++;
            }
            else {
                for (int ii = 0; ii < n; ii++) {
                    if (to[ii][0] < M) {
                        for (int jj = 0; jj < p; jj++) {
                            from[ii][jj] = from[ii][jj + 1];
                            to[ii][jj] = to[ii][jj + 1];
                        }
                    }
                }
            }
        }

        cout << ans << endl;
    }
    return 0;
}