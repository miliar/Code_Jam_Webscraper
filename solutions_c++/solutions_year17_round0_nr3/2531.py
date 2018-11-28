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
        ll n, k;
        cin >> n >> k;
        
        map<ll, ll> cnt;
        cnt[n] = 1;
        
        ll mi = -1, ma = -1;
        while (k > 0) {
            auto it = cnt.end();
            --it;
            ll len = it->first, kk = it->second;
            cnt.erase(it);

            ma = len / 2, mi = (len - 1) / 2;

            ll take = min(k, kk);
            kk -= take;
            k -= take;

            if (kk > 0) {
                cnt[len] = kk;
            }
            if (len / 2 > 0) {
                cnt[len / 2] += take;
            }
            if ((len - 1) / 2 > 0) {
                cnt[(len - 1) / 2] += take;
            }
        }
        cout << "Case #" << test << ": " << ma << " " << mi << endl;
    }
    return 0;
}
