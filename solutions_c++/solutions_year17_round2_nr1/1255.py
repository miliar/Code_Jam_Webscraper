#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		int D, n;
		double an = 1e18;
		scanf("%d%d", &D, &n);
		f(i, 0, n){
			int a, b;
			scanf("%d%d", &a, &b);
			double t = (double)(D - a) / b;
			an = min(an, D / t);
		}
		printf("Case #%d: %.7lf\n", tc, an);
	}
}