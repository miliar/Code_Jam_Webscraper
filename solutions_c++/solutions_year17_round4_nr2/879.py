#include <bits/stdc++.h>
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
using namespace std;

const int MAXN = 1000;

void solve() {
    int n, c, m;
    scanf("%d%d%d", &n, &c, &m);
    int cnt1 = 0, cnt2 = 0, y = 0, z = 0;
    multiset<int> p1, p2;
    for(int i = 0; i < m; i++) {
        int p, b;
        scanf("%d%d", &p, &b);
        if(p == 1) {
            if(b == 1)
                cnt1++;
            else
                cnt2++;
        } else {
            if(b == 1)
                p1.insert(p);
            else
                p2.insert(p);
        }

    }
    y = cnt1 + cnt2;
    while(((int)p1.size() - cnt2 > 0) || ((int)p2.size() - cnt1 > 0)) {
        bool ok = false;
        for(auto i1: p1) {
            for(auto i2: p2) {
                if(i1 != i2) {
                    p1.erase(p1.find(i1));
                    p2.erase(p2.find(i2));
                    ok = true;
                    break;
                }
            }
            if(ok)
                break;
        }
        if(!ok) {
            z = max(0, (int)min((int)p1.size() - cnt2, (int)p2.size() - cnt1));
            y += max((int)p1.size() - cnt2, (int)p2.size() - cnt1);
            break;
        } else
            y++;
    }
    printf("%d %d\n", y, z);
}

int main() {
    //ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}