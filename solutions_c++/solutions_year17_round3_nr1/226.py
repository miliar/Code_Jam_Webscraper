#include<cstdio>
#include<cmath>
#include<algorithm>
#define N 1010

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
#ifndef M_PI
const double M_PI = acos(-1);
#endif

bool cmp(const pll &a, const pll &b){
    return a.first*a.second < b.first*b.second;
}

pll loli[N];

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        int n, K;
        scanf("%d%d", &n, &K);
        for(int i=1; i<=n; i++){
            scanf("%I64d%I64d", &loli[i].first, &loli[i].second);
        }
        sort(loli+1, loli+n+1, cmp);
        ll ans = 0, s=0, t=0;
        for(int i=n-K+2; i<=n; i++){
            s += 2*loli[i].first*loli[i].second;
        }
        t = s + 2*loli[n-K+1].first*loli[n-K+1].second;
        for(int i=1; i<=n-K; i++){
            ans = max(ans, loli[i].first*(loli[i].first+2*loli[i].second)+s);
        }
        for(int i=n-K+1; i<=n; i++){
            ans = max(ans, loli[i].first*loli[i].first+t);
        }
        printf("Case #%d: %.8f\n", kase, M_PI*ans);
    }
    return 0;
}
