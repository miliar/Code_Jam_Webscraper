//Fruit of Light
//FoL CC
//Apple Strawberry

#include<cstdio>
#include<algorithm>
#include<vector>
#include<iostream>
#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<cstring>

using namespace std;

#define For(i, n) for(int i = 0; i<int(n); ++i)
#define INF 1023456789
#define eps 1e-9

typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<int> vi;


int extra() {
    int n,k,r,h;
    vector<pll> P;
    scanf("%d%d", &n,&k);
    For(i, n) {
        scanf("%d%d", &r, &h);
        P.push_back({ll(h)*r*2, ll(r)*r});
    }
    sort(P.begin(), P.end());
    reverse(P.begin(), P.end());
    ll best = 0;
    ll prvychk = 0;
    For(i, k-1) {
        prvychk += P[i].first;
    }
    For(i, n) {
        ll navyse = (i<k-1) ? P[k-1].first : P[i].first;
        best = max(best, P[i].second + prvychk + navyse);
    }
    printf("%.10lf\n", best * M_PI);
}

int main() {
    int T;
    scanf("%d",&T);
    For(i,T){
        printf("Case #%d: ",i+1);
        extra();
    }
}
