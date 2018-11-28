#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> pii;


#define se second
#define fi first
#define pb push_back
#define mp make_pair

pii horses[1010];

int main() {
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    for(int testcase = 1; testcase <= t; testcase++) {
    	long double ans = 1e18;
    	ll d,n;
    	scanf("%lld%lld", &d, &n);
    	for(int i =0; i < n; i++) {
    		scanf("%lld%lld", &horses[i].fi, &horses[i].se);
    	}
    	sort(horses, horses+n, greater<pii>());
    	ll time = 0;
    	for(int i = 0; i < n; i++) {
    		ans = min(ans, (long double)(d)*horses[i].se/(d-horses[i].fi));
    	}
    	printf("Case #%d: ", testcase);
    	printf("%.10Lf\n", ans);
    }
}