#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef long double ld;

int main(){
	int Test, n;
	double a, b, c;
	ld D, K, V, mn, t;
	scanf("%d\n", &Test);
	for(int test=1; test<=Test; test++){
		scanf("%lf %d\n", &a, &n); D=(ld)a;
		
		mn = -1.0;
		for(int i=0; i<n; i++){
			scanf("%lf %lf", &b, &c); K=(ld)b; V=(ld)c;
			mn = max(mn,(D-K)/V);
		}
		//cout<<mn<<endl;
		t = D/mn;
		printf("Case #%d: %.6lf\n", test, (double)t);
	}
	return 0;
}
