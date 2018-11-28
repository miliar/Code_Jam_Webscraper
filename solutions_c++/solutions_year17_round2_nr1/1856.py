#include <bits/stdc++.h>
using namespace std;

#define FOR(i,n) for(int i=0;i<n;++i)

void solve() {
    int d,n;
    scanf("%d%d",&d,&n);
    vector<pair<int,int> > h;
    FOR(i,n) {
        int k,s;
        scanf("%d%d",&k,&s);
        h.push_back({k,s});
    }
    
    double ans = 1ll<<60;
    FOR(i,n) {
        long long ds = ((long long)d) * h[i].second;
        double temp = ((double)ds) / (d - h[i].first);
        ans = min(ans, temp);
    }
    printf("%.20lf\n",ans);
    
}


int main(void) {
    int t;
    scanf("%d\n",&t);
    FOR(i,t) {
        printf("Case #%d: ", i+1);
        solve();
    }
    
}
