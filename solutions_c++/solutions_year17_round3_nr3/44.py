#include <bits/stdc++.h>
using namespace std;

double arr[100];
const double EPS = 1E-12;

bool ok(double v, int N, double rem){
    for(int i = 1; i <= N; i++){
	if(arr[i] - EPS >= v) continue;
	double x = v - arr[i];
	rem -= x;
    }
    if(rem + EPS < 0) return 0;
    else return 1;
}

double solve(){
    int n,k;
    cin >> n >> k;
    assert(n == k);

    double u;
    cin >> u;

    for(int i = 1; i <= n; i++)
	cin >> arr[i];

    double lo = 0, hi = 1;
    for(int i = 0; i < 1000; i++){
	double mid = (lo + hi) * 0.5;

	if(ok(mid,n,u))
	    lo = mid;
	else
	    hi = mid;
    }
    double ret = 1.0;
    for(int i = 1; i <= n; i++){
	if(arr[i] < lo) arr[i] = lo;
	ret *= arr[i];
    }
    return ret;
}


int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i++){
	printf("Case #%d: %.8f\n", i, solve());
    }
    return 0;
}
