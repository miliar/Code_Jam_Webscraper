#include <iostream>
#include <algorithm>
#include <vector>
#include <deque>
#include <cassert>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <string>
#include <utility>
#include <cmath>
#include <bitset>
#include <climits>
#include <iomanip>
#include <fstream>
#include <unordered_set>
#include <unordered_map>
#include <cstdio>
#include <cstring>

using namespace std;

#define ll long long
#define N (ll)(1e6+5)
#define INF (ll)(1e18+3)
#define EPS (1e-9)
#define PI (3.14159265358979323846)
#define ld double
#define MOD (ll)(1e9+7)

ll solve(ll n) {
    vector<int> digits;
    ll my_n = n;
    while (my_n > 0) {
        digits.push_back(my_n % 10);
        my_n /= 10;
    }
    bool good = true;
    int j;
    for (j = (int) digits.size() - 1; j >= 1; j--) {
        if (digits[j] > digits[j - 1]) {
            good = false;
            break;
        }
    }
    if (good) return n;
    else {
        ll divider = pow(10, j);
        return solve(n / divider * divider - 1);

    }
}

int main() {
    ifstream in("in.txt");
    ofstream out("out.txt");
    int t;
    in >> t;
    
    for (int i = 0; i < t; i++) {
        
        ll n;
        in >> n;
        out << "Case #" << i + 1 << ": " << solve(n) << endl;
    }
    
    in.close();
    out.close();
}
