#include<bits/stdc++.h>
using namespace std;
#define s(x)        scanf("%d",&x);
#define pb(x)       push_back(x);
#define maxn 100005
#define pf(x,y)  printf("Case #%d: %d\n", x, y);
#define ll long long
int main() {
 
    int t;
    cin >> t;
    for(int j = 1; j <= t; j++) {
        int n, p;
        s(n);
        s(p);
        int g[maxn];
        vector<int> aa(p);
        vector<int> pp;
        int ans = 0;
        for(int i = 0; i < n; i++) {
            cin >> g[i];
            g[i] %= p;
            aa[g[i]]++;
        }
        if (p == 2) {
            for (int i = 0; i < aa[0]; i++) pp.pb(0);
            for (int i = 0; i < aa[1]; i++) pp.pb(1);
        }
        if (p == 3) {
            for (int i = 0; i < aa[0]; i++) pp.pb(0);
            for (int i = 0; i < min(aa[1], aa[2]); i++) {
                pp.pb(1);
                pp.pb(2);
            }
            for (int i = min(aa[1], aa[2]); i < max(aa[1], aa[2]); i++) pp.pb(1);
        }
        if (p == 4) {
            for (int i = 0; i < aa[0]; i++) pp.pb(0);
            for (int i = 0; i < aa[2] / 2 * 2; i++) pp.pb(2);
            for (int i = 0; i < min(aa[1], aa[3]); i++) {
                pp.pb(1);
                pp.pb(3);
            }
            if (aa[2] & 1) pp.pb(2);
            for (int i = min(aa[1], aa[3]); i < max(aa[1], aa[3]); i++) pp.pb(1);
        }      int now = 0;
        for (vector<int>::size_type ix = 0; ix != pp.size(); ++ix) {
            if(now == 0) ans++;
            now = (now + p - ix) % p;
        }
        pf(j, ans);
    }
    return 0;
}
