#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define ll long long
#define M 1000000007
#define all(a) a.begin(), a.end()

int d, n;
int s[1100], k[1100];

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("x.out", "w", stdout);
	int T, t = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &d, &n);
		double ans = 1e18;
		for(int i = 1; i <= n; ++i){
			scanf("%d%d", k + i, s + i);
			ans = min(ans, 1. * d * s[i] / (d - k[i]));
		}
		printf("Case #%d: %.10f\n", ++t, ans);
	}
	
	return 0;
}
