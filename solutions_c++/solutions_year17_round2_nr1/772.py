#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<LL, double> PII;
typedef set<int>::iterator SIT; 

const int maxn = 1005;

int d, n;
PII h[maxn]; 

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, cases = 0;
	scanf("%d", &T);
	while(T--){
		scanf("%d%d", &d, &n);
		double t = 0;
		for(int i = 0; i < n; ++i){
			int x, y;
			scanf("%d%d", &x, &y);
			t = max(t, 1.0 * (d - x) / y);
		}
		printf("Case #%d: %.10lf\n", ++cases, d / t);
	}
	return 0;
}
