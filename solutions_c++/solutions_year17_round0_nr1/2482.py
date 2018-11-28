#pragma region template
#pragma comment(linker, "/stack:200000000")
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
#include <sstream>
#include <fstream>
#include <complex>
#include <numeric>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
using namespace std;
typedef long long ll;
typedef double db;
typedef unsigned long long ull;
typedef long double ld;
struct _{
    _() {
        cout.precision(30);
        ios_base::sync_with_stdio(false);
        cin.tie(0);
    }
} __;
#pragma endregion

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        string s;
        cin >> s;
        int k, n = s.size(), result = 0;
        cin >> k;
        for (int i = 0; i <= n - k; i++) {
            if (s[i] == '-') {
                result++;
                for (int j = i; j < i + k; j++) {
                    if (s[j] == '-') s[j] = '+'; else s[j] = '-';
                }
            }
        }
        bool ok = true;
        for (int i = 0; i < n; i++) {
            if (s[i] == '-') ok = false;
        }

        cout << "Case #" << test << ": ";
        if (!ok) {
            cout << "IMPOSSIBLE" << endl;
        }
        else {
            cout << result << endl;
        }
    }
    return 0;
}
