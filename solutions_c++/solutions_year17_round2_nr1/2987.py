#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> ii;
int tcs, n, d;
double ts[1005], dt, ds;
ii a[1005];
bool cmp(ii a, ii b){
	if(a.first == b.first) return a.second < b.second;
	return a.first > b.first;
}
int main(){
	scanf("%i", &tcs);
	for(int tc=1;tc<=tcs;tc++){
		scanf("%i%i", &d, &n);
		for(int i=0;i<n;i++){
			scanf("%i%i", &a[i].first, &a[i].second);
		}
		sort(a, a+n, cmp);
		double mx = 0.0;
		for(int i=0;i<n;i++){
			ts[i] = ((double)d - a[i].first) / a[i].second;
			mx = max(mx, ts[i]);
		}
		double ans = d / mx;
		printf("Case #%i: %lf\n", tc, ans);
	}
}