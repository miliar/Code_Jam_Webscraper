#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#define N 1111
#define ll long long
#define md 1000000007
#define PI acos(0.0) * 2
using namespace std;

int t;
bool st(pair<ll, ll> u, pair<ll, ll> v){
    return (u.first * u.second) > (v.first * v.second);
    
}
int main(void){
    scanf("%d", &t);
    for(int s = 1; s <= t; s++){
        double ans = 0, ans2 = 0; // curved, flat
        ll mxr = 0;
        int n, k;
        pair<ll, ll> r[N];
        scanf("%d%d", &n, &k);
        for(int i = 0; i < n; i++) scanf("%lld%lld", &r[i].first, &r[i].second);
        sort(r, r + n, st);
        for(int i = 0; i < k - 1; i++) ans += 2.0 * r[i].first * r[i].second, mxr = max(mxr, r[i].first);
        for(int i = k - 1; i < n; i++){
            ll rmxr = max(mxr, r[i].first);
            ans2 = max(ans2, (double)(rmxr * rmxr + 2.0 * r[i].first * r[i].second));
        }
        
        printf("Case #%d: %.9lf\n", s, PI * (ans + ans2));

    }
}

/*
Curved surface area:
pi r^2 h

*/
