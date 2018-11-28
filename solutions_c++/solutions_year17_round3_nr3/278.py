#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <cmath>
#include <set>
#include <map>
#include <iostream>

using namespace std;

const int maxn = 1500;

double a[100];
double U;

int n,k;
bool ok(double mid){
	double ret = 0;
	for (int i =0; i < n; ++i){
		if (a[i] < mid)ret += mid - a[i];
	}
	return ret <= U;
}

int main() {
	freopen("C-small-1-attempt0.in.txt", "r", stdin);
	freopen("C.out", "w", stdout);
	int T;
	cin >> T;

	for(int cas = 1; cas <= T; cas ++) {
		cin >> n >> k;
		cin>>U;
		for (int i = 0; i < n; ++i){
			cin>>a[i];
		}
		a[n] = 1;
		sort(a,a+n+1);
		double L = 0, R = 1;
		int lim = 80;
		while (lim--){
			double mid = (L + R)/2;
			if (ok(mid)){
				L = mid;
			}else{
				R = mid;
			}
		}
		double ans = 1;
		L = min(L,1.0);
		for (int i = 0; i < n; ++i){
			if(a[i] < L){
				ans *= L;
			}else {
				ans *= a[i];
			}
		}
		
		printf("Case #%d: %.10f\n",cas,ans);
	}
	return 0;
}

