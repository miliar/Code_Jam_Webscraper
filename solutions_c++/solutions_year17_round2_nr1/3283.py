#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> plli;
typedef pair<double, double> pdd;
typedef pair<string, int> psi;

const int MOD = 1e9 + 7;
const int N = 10001;

typedef long long ll;

int n,m,t;
double pos[N],s[N],k;

bool check(double mid){
	for (int i = 0; i < n; ++i){
		double lo = 0 , hi = 2e9,newM;
		for(int it = 0 ; it < 128 ; it++){
			newM = (lo + hi) * 0.5;
			if(newM * mid >= newM * s[i] + pos[i]){
				hi = newM;
			}else{
				lo = newM;
			}
		}
		if(newM * s[i] + pos[i] <= k)
			return false;
	}
	return true;
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&t);
	for(int tt = 1 ; tt <= t  ; tt++){
		scanf("%lf%d",&k,&n);
		for (int i = 0; i < n; ++i){
			scanf("%lf%lf",&pos[i],&s[i]);
		}
		double lo = 0 , hi = 1e15,mid;
		for(int it = 0 ; it < 128 ; it++){
			mid = (lo + hi) * 0.5;
			if(check(mid)){
				lo = mid;
			}else{
				hi = mid;
			}
		}
		printf("Case #%d: %.6lf\n",tt,mid);
	}
	return 0;
}