#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define ll long long
#define M 1000000007
#define all(a) a.begin(), a.end()

const double eps = 1e-10;
int n, k;
double u, p[60];

int main(){
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("x.out", "w", stdout);
	int T, ca = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &n, &k);
		scanf("%lf", &u);
		
		for(int i = 1; i <= n; ++i){
			scanf("%lf", p + i);
		}

		double l = 0, r = 1;
		for(int i = 1; i <= 200; ++i){
			double d = (l + r) / 2;
			double need = 0;
			for(int j = 1; j <= n; ++j)
				if(p[j] < d) need += d - p[j];
			if(need <= u) l = d;
			else r = d;
		}
		
		double ans = 1;
		for(int i = 1; i <= n; ++i)
			ans *= max(l, p[i]);

		printf("Case #%d: %.10f\n", ++ca, ans);
	}
	return 0;
}
