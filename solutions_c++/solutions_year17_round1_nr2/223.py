#include <bits/stdc++.h>

#define FI(i,a,b) for(int i=(a);i<=(b);i++)
#define FD(i,a,b) for(int i=(a);i>=(b);i--)

#define LL long long
#define Ldouble long double
#define PI 3.1415926535897932384626

#define PII pair<int,int>
#define PLL pair<LL,LL>
#define mp make_pair
#define fi first
#define se second

using namespace std;

int t, n, pack, req[55];
PII lob[55][55];

int ptr[55];

bool end(){
	FI(i, 1, n) if(ptr[i] > pack) return true;
	return false;
}

void solve(){
	/*
	FI(j, 1, n){
		printf("Ingre %d:\n", j);
		FI(k, 1, pack) printf("range [%d %d]\n", lob[j][k].fi, lob[j][k].se);
	}
	*/
	int ret = 0;
	FI(i, 1, n) ptr[i] = 1;
	while(!end()){
		int maxi = 0;
		FI(i, 1, n) maxi = max(maxi, lob[i][ptr[i]].fi);
		
		int fail = -1;
		FI(i, 1, n) if(lob[i][ptr[i]].se < maxi){
			fail = i;
			break;
		}
		if(fail == -1){
			ret++;
			FI(i, 1, n) ptr[i]++;
		}
		else ptr[fail]++;
	}
	printf(" %d\n", ret);
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("B2.out", "w", stdout);
	scanf("%d", &t);
	FI(i, 1, t){
		printf("Case #%d:", i);
		scanf("%d %d", &n, &pack);
		FI(j, 1, n) scanf("%d", &req[j]);
		FI(j, 1, n) FI(k, 1, pack){
			int x;
			scanf("%d", &x);
			lob[j][k] = mp(ceil(10.0 * x / (11 * req[j])), 10 * x / (9 * req[j]));
		}
		FI(j, 1, n) sort(lob[j] + 1, lob[j] + pack + 1);
		solve();
	}
	return 0;
}

