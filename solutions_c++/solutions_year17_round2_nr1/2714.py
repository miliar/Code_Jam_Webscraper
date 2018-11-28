//
// Created by quuynh on 22/04/17.
//

#include <climits>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <queue>
#include <stack>
#include <unordered_map>
#include <unordered_set>

using namespace std;
#define maxN 1001
#define vc 1000000001
#define For(i, a, b) for(int i=a;i<=b;i++)
long long d, n;
long long k[maxN], s[maxN];

void solve() {
    double l = vc;
    For(i, 1, n) if (l > s[i]) l = s[i];
    double r = vc;
    while (r - l > 0.0000001) {
        double mid = (l + r) / 2;
        bool ok = true;
        For(i, 1, n) if (mid > s[i]) {
                double diff = (double) k[i] / (mid - s[i]);
                if (diff * mid < (double) d) ok = false;
            }
        if (ok) l = mid; else r = mid;
    }
    printf("%.6f", l);
}

void solve1() {
    double maxValue = -vc;
    For(i, 1, n) if (((double) d - k[i]) / s[i] > maxValue) maxValue = ((double) d - k[i]) / s[i];
    double result = (double) d / maxValue;
    printf("%.6f", result);
}

int main() {
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/codejam23042017/A-large (1).in", "r", stdin);
    freopen("/home/quuynh/Desktop/study/programming/Leetcode/codejam23042017/bai1.ans", "w", stdout);
    int nTest;
    cin >> nTest;
    For(test, 1, nTest) {
        cin >> d >> n;
        For(i, 1, n) cin >> k[i] >> s[i];
        cout << "Case #" << test << ": ";
        solve1();
        if (test < nTest) cout << endl;
    }
    return 0;

}