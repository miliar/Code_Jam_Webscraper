#include <bits/stdc++.h>

using namespace std;


int main(){
	int t; scanf("%d", &t);
	for (int i=1; i<=t; ++i){
		printf("Case #%d: ", i);
		int d,n; scanf("%d%d", &d, &n);
		double mt = 0.0;
		for (int j=0; j<n; ++j){
			int k,s; scanf("%d%d", &k, &s);
			double res = (double)(d-k)/s;
			if (res > mt) mt = res;
		}
		printf("%.6f\n", d/mt);
	}
}
