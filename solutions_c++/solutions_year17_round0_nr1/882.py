#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>

#define ll long long
#define ull unsigned long long
#define mo 1000000007

using namespace std;
typedef pair<int, int> pii;

//ll moMul(ll a, ll b) {
//    return ((a % mo) * (b % mo)) % mo;
//}

void flip(string& s, int index, int k) {
    for (int i = index; i < index + k; ++i) {
        if (s[i] == '+') {
            s[i] = '-';
        } else {
            s[i] = '+';
        }
    }
}

int solve(string& s, int k) {
    int cnt = 0;
    for (int i = 0; i <= s.length() - k; ++i) {
        if (s[i] == '-') {
            flip(s, i, k);
            ++cnt;
        }
    }
    for (int i = s.length() - k + 1; i < s.length(); ++i) {
        if (s[i] == '-') return -1;
    }
    return cnt;
}

int main() {
    freopen("/Users/Swing/Documents/code/googleCodeJam/A-large.in", "r", stdin);
    freopen("/Users/Swing/Documents/code/googleCodeJam/A-large.out", "w", stdout);

    int t;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        string s;
        int k;
        cin >> s >> k;
        cout << "Case #" << i << ": ";
        int tmp = solve(s, k);
        if (tmp >= 0) {
            cout << tmp << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
//        printf("Case #%d: %.8f\n", i, res);
//        cout << "Case #" << i << ": " << tmp << endl;
//        printf("Case #%d: %.7lf\n", i, res);

    }

    return 0;
}