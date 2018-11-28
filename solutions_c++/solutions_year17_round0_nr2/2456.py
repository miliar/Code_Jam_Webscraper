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
        ll n;
        cin >> n;

        vector<int> x;
        while (n) {
            x.push_back(n % 10);
            n /= 10;
        }

        reverse(x.begin(), x.end());

        for (int i = int(x.size()) - 2; i >= 0; i--) {
            if (x[i] > x[i + 1]) {
                x[i]--;
                
                for (int j = i + 1; j < x.size(); j++) {
                    x[j] = 9;
                }
                for (int j = i; j >= 0; j--) {
                    if (x[j] == -1) {
                        x[j] = 9;
                        x[j - 1]--;
                    }
                }
            }
        }
        ll result = 0;
        for (int i = 0; i < x.size(); i++) {
            result = result * 10 + x[i];
        }
        cout << "Case #" << test << ": " << result << endl;
    }
    return 0;
}
