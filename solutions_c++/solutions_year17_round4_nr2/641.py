#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> plli;
typedef pair<double, double> pdd;
typedef pair<string, int> psi;
const ll oo = 1e15;
typedef long long ll;

const int N = 200010;
const int MX = 200000;


int n , m , c,f1[1100],f2[1100],p,t,b;

pii best;

bool check(int mid){
	int extra = 0;
	int pro = 0;
	for (int i = 1 ; i <= n; ++i){
		if(f1[i] <= mid){
			extra += (mid - f1[i]);
			continue;
		}
		if(f1[i] > mid){
			int need = f1[i]-mid;
			if(need > extra)
				return false;
			pro += need;
			extra -= need;
		}
	}
	for (int i = 1 ; i <= c; ++i){
		if(f2[i] > mid)
			return false;
	}
	best = make_pair(mid,pro);
	return true;
}
int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &t);
	for(int it = 1 ; it <= t ; it++){
		scanf("%d%d%d",&n,&c,&m);
		memset(f1,0,sizeof f1);
		memset(f2,0,sizeof f2);
		for(int j = 0 ; j < m ; j++){
			scanf("%d%d",&p,&b);
			f2[b]++;
			f1[p]++;
		}
		int lo = 1 , hi = m;
		while(lo <= hi){
			int mid = (lo + hi)/2;
			if(check(mid)){
				hi = mid -1;
			}else{
				lo = mid + 1;
			}
		}
		printf("Case #%d: %d %d\n",it,best.first,best.second );
	}
	return 0;
}