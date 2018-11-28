#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> plli;
typedef pair<double, double> pdd;
typedef pair<string, int> psi;

const int MOD = 1e9 + 7;

const ll oo = 1e15;


typedef long long ll;

int t , n , k;

double p[100],u;

bool check(double mid){
	double need = 0;
	for (int i = 0; i < n; ++i){
		need += max(0.0,mid-p[i]);
	}
	return need <= u;
}

int main() {
 	freopen("input.txt","r",stdin);
 	freopen("output.txt","w",stdout);
 	scanf("%d",&t);
 	for(int it = 1 ; it <= t ; it++){
 		scanf("%d%d",&n,&k);
 		scanf("%lf",&u);
 		for (int i = 0; i < n; ++i){
 			scanf("%lf",&p[i]);
 		}
 		double lo = 0.0 , hi = 1,mid;
 		for(int k = 0 ; k < 128 ; k++){
 			mid = (lo + hi) * 0.5;
 			if(check(mid))
 				lo = mid;
 			else
 				hi = mid;
 		}
 		double ans = 1;
 		for (int i = 0; i < n; ++i){
 			ans = ans * max(p[i],mid);
 		}
 		printf("Case #%d: %.9lf\n",it,ans);
 	}
	return 0;
}
