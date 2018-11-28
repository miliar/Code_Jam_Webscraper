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

void solve()
{
    long long n, k;
    cin >> n >> k;
    long long tc = 1;
    while (n % 2 == 1) {
        if (k <= tc) {
            cout << n / 2 << ' ' << n / 2 - (n % 2 == 0) << '\n';
            return;
        }
        n /= 2;
        tc = (tc + 1) * 2 - 1;
    }
    if (k <= tc) {
        cout << n / 2 << ' ' << n / 2 - (n % 2 == 0) << '\n';
        return;
    }
    long long n1 = n / 2, n2 = n / 2 - 1, c1 = (tc + 1) / 2, c2 = (tc + 1) / 2;
    while (true) {
        if (k <= tc + c1) {
            cout << n1 / 2 << ' ' << n1 / 2 - (n1 % 2 == 0) << '\n';
            return;
        }
        if (k <= tc + c1 + c2) {
            cout << n2 / 2 << ' ' << n2 / 2 - (n2 % 2 == 0) << '\n';
            return;
        }
        tc += c1 + c2;
        if (n1 % 2 == 0) {
            c2 = c1 + c2 * 2;
        } else {
            c1 = c2 + c1 * 2;
        }
        n1 = n1 / 2;
        n2 = n1 - 1;
    }
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