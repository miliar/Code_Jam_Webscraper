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

string s[111];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output_a_2.txt", "w", stdout);
    int Tests;
    cin >> Tests;
    for (int Test = 1; Test <= Tests; Test++) {
        cout << "Case #" << Test << ": ";
        int n, m;
        cin >> n >> m;
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }

        int last = -1;
        for (int i = 0; i < n; i++) {
            int nlast = last;
            int prev = -1;
            for (int j = 0; j < m; j++) {
                if (s[i][j] != '?') {
                    nlast = i;
                    if (prev == -1) {
                        for (int jj = 0; jj < j; jj++) {
                            for (int ii = last + 1; ii <= i; ii++) {
                                s[ii][jj] = s[i][j];
                            }
                        }
                    }
                    for (int jj = j; jj < m; jj++) {
                        if (jj > j && s[i][jj] != '?') {
                            break;
                        }
                        for (int ii = last + 1; ii <= i; ii++) {
                            s[ii][jj] = s[i][j];
                        }
                    }
                    prev = j;
                }
            }
            last = nlast;
        }
        cout << endl;
        for (int i = last + 1; i < n; i++) {
            s[i] = s[i - 1];
        } 

        for (int i = 0; i < n; i++) {
            cout << s[i] << endl;
        }
    }
    return 0;
}