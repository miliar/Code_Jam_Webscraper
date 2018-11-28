#include <stdio.h>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
#include <numeric>
using namespace std;

char a[30][30];

void solve()
{
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> a[i][j];
        }
    }
    int last_i = 0, last_j = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] != '?') {
                int t = j - 1;
                last_i = i;
                last_j = j;
                while (t >= 0 && a[i][t] == '?') {
                    a[i][t] = a[i][j];
                    --t;
                }
            }
        }
        if (last_j != m - 1) {
            for (int k = last_j + 1; k < m; k++) {
                a[i][k] = a[i][last_j];
            }
        }
        if (i > 0 && a[i - 1][0] == '?') {
            int t = i - 1;
            while (t >= 0 && a[t][0] == '?') {
                for (int k = 0; k < m; k++) {
                    a[t][k] = a[t + 1][k];
                }
                --t;
            }
        }
    }
    if (last_i != n - 1) {
        for (int t = last_i + 1; t < n; t++) {
            for (int k = 0; k < m; k++) {
                a[t][k] = a[t - 1][k];
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << a[i][j];
        }
        cout << '\n';
    }
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ":\n";
        solve();
    }
    return 0;
}