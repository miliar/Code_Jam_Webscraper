#pragma region template
#define _CRT_SECURE_NO_WARNINGS
#include <climits>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <vector>
#include <bitset>
#include <map>
#include <queue>
#include <ctime>
#include <stack>
#include <set>
#include <list>
#include <random>
#include <deque>
#include <functional>
#include <fstream>
#include <complex>
#include <numeric>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <sstream>

using namespace std;

typedef long double ld;
typedef long long ll;

void solve() {
    int n, k;
    ld u;
    cin >> n >> k >> u;
    vector<ld> p(n);
    for (int i = 0; i < n; i++) {
        cin >> p[i];
    }
    sort(p.begin(), p.end());
    p.resize(n + 1);
    p[n] = 1;
    ld sum = p[0];
    for (int i = 1; i <= n; i++) {
        ld x = (u + sum) / i;
        if (p[i - 1] <= x && x <= p[i]) {
            for (int j = 0; j < i; j++) {
                p[j] = x;
            }
            ld result = 1.0;
            for (int j = 0; j < n; j++) {
                result *= p[j];
            }
            cout.precision(30);
            cout << (result < 1e-7 ? 0.0 : result);
            return;
        }
        sum += p[i];
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; ++test) {
        cout << "Case #" << test << ": ";
        solve();
        cout << endl;
    }
    return 0;
}
