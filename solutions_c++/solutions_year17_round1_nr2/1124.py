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

int p[100];
int q[100][100];
bool u[100][100];
int n, k;

bool check(int i, int k_min, int k_max) 
{
    if (i == n) {
        return true;
    }
    for (int j = 0; j < k; j++) {
        int cur_k_min = ceil(q[i][j] / (1.1 * p[i]));
        if (0.9 * p[i] * cur_k_min > q[i][j]) {
            continue;
        }
        int cur_k_max = floor(q[i][j] / (0.9 * p[i]));
        if (1.1 * p[i] * cur_k_max < q[i][j]) {
            continue;
        }
        if (cur_k_min > k_max) {
            return false;
        }
        if (cur_k_max < k_min) {
            continue;
        }
        if (!u[i][j]) {
            if (check(i + 1, max(k_min, cur_k_min), min(k_max, cur_k_max))) {
                u[i][j] = true;
                return true;
            }
        }
    }
    return false;
}

void solve()
{
    cin >> n >> k;
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < k; j++) {
            cin >> q[i][j];
            u[i][j] = false;
        }
        sort(q[i], q[i] + k);
    }
    int ans = 0;
    for (int j = 0; j < k; j++) {
        int k_min = ceil(q[0][j] / (1.1 * p[0]));
        if (0.9 * p[0] * k_min > q[0][j]) {
            continue;
        }
        int k_max = floor(q[0][j] / (0.9 * p[0]));
        if (1.1 * p[0] * k_max < q[0][j]) {
            continue;
        }
        ans += check(1, k_min, k_max);
    }
    cout << ans << '\n';
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}