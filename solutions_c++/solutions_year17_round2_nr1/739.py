#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef pair<ll,ll> pl;
ll T,D,N;
double t[1002];
pl p[1002];
int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("output_large.out", "w", stdout);
    scanf("%lld", &T);
    for(ll c = 1; c <= T; c++) {
        scanf("%lld%lld", &D, &N);
        for(ll i=0;i<N;i++)
            scanf("%lld%lld", &p[i].first, &p[i].second);
        sort(p,p+N);
        t[N-1] = (double)(D - p[N-1].first) / p[N-1].second;
        for(ll i=N-2;i>=0;i--) {
            t[i] = (double)(D - p[i].first) / p[i].second;
            if(t[i] < t[i+1]) t[i] = t[i+1];
        }
        printf("Case #%lld: %.6f\n", c, D / t[0]);
    }
    return 0;
}
