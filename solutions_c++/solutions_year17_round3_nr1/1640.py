#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cmath>
#include <cstdlib>
#define fi first
#define se second
using namespace std;
typedef long long llint;
typedef pair<int, int> pii;

const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
const int N = 1e3+10;

struct cake {
    int r, h;
    double sq;
    bool operator<(const cake & ano) const {
        return r > ano.r;
    }
} a[N];

bool cmp(cake a, cake b) {
    return a.sq > b.sq;
}

int main() {
    if (/* DISABLES CODE */ (true)) {
        freopen("/Users/Clair/Desktop/A-small-attempt2.in", "r", stdin);
        freopen("/Users/Clair/Desktop/a-out-s2.txt", "w+", stdout);
    }
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        int n, k;
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> a[i].r >> a[i].h;
            a[i].sq = 2 * PI * a[i].r * a[i].h;
        }
        double r_ans = 0;
        sort(a, a + n); // sort by r.
        for (int st = 0; st < n; st++) {
            priority_queue<double> q;
            double ans = a[st].sq + a[st].r * a[st].r * PI;
            for (int i = st+1; i < n; i++)
                q.push(a[i].sq);
            for (int i = 0; i < k-1 && !q.empty(); i++) {
                ans += q.top();
                q.pop();
            }
            r_ans = max(ans, r_ans);
        }
        printf("Case #%d: %.9lf\n", tt, r_ans);
    }
}
