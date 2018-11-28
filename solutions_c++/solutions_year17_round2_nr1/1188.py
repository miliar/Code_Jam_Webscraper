#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define xx first
#define yy second

#ifndef _WIN32
#define gc getchar_unlocked
#else
#define gc getchar
#endif // _WIN32
void ri(int &a) {
    a = 0;
    register int x = gc();
    bool neg = false;
    while (x < '0' || x > '9') {
        if (x == '-') neg = true;
        x = gc();
    }
    while (x >= '0' && x <= '9') {
        a = (a << 3) + (a << 1) + (x-'0');
        x = gc();
    }
    if (neg) a = -a;
}

const int maxn = 100100, INF = (1 << 30)-1;
int t;

int main() {
    freopen("output.out", "w", stdout);
    ri(t);
    for (int casenum = 1, d, n; casenum <= t; casenum++) {
        printf("Case #%d: ", casenum);
        ri(d), ri(n);
        double ans = 1e18;
        for (int i = 0, start, speed; i < n; i++) {
            ri(start), ri(speed);
            ans = min(ans, d/((double)(d-start)/speed));
        }
        printf("%.9f\n", ans);
    }
    return 0;
}
