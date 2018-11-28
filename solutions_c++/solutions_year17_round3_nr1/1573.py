#include <bits/stdc++.h>

//LIFE IS NOT A PROBLEM TO BE SOLVED

using namespace std;

#define rep(i,a,b) for(int i = int(a); i < int(b) ; i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second

typedef long long int ll;
typedef unsigned long long int ull;
typedef pair < ll, ll > ii;
typedef pair < int, ii > iii;

const int INF = 0x3f3f3f3f;
const long double LINF = 1LL<<58;

int N, K;
ii n[1010];
long double pd[1010][1010];
int best[1010];

bool cmp(ii a, ii b){
	if(a.F!=b.F) return a.F>b.F;
	return a.S>b.S;
}

long double area(int i){
	return n[i].F*n[i].F*M_PI;
}
long double altura(int i){
	return n[i].F*n[i].S*M_PI*2;
}

long double solve(int i, int k){
	
	if(k==0) return 0;
	if(i==N) return -LINF;
	if(pd[i][k]>=0) return pd[i][k];
	
	long double ret=0;
	
	int fim=N+1, ml=i+1;
	if(best[i]) fim=min(fim, best[i]+1);
	
	rep(j, i+1, fim){
		long double aux=solve(j, k-1)+area(i)-area(j)+altura(i);
		if(aux>=ret){
			ret=aux;
			ml=j;
		}
	}
	
	best[i]=ml;
	
	return pd[i][k]=ret;
	
}


int main(){
	
	freopen("Al.in", "r", stdin);
	freopen("teste2.sol", "w", stdout);

	int T; cin >> T;
	
	rep(z, 1, T+1){
		
		scanf("%d %d", &N, &K);
		rep(i, 0, N) scanf("%lld %lld", &n[i].F, &n[i].S);
		n[N]=ii(0, 0);
		
		rep(i, 0, N+4){
			rep(j, 0, K+4) pd[i][j]=-10.0;
			best[i]=0;
		}
		
		sort(n, n+N, cmp);
		
		long double ans=0;
		rep(i, 0, N-K+1){
			rep(j, i+1, N-K+2){
				ans=max(ans, solve(j, K-1)+area(i)-area(j)+altura(i));
			}
				
		}
		
		printf("Case #%d: %.8LF\n", z, ans);
		
	}
	
	return 0;
	
}
