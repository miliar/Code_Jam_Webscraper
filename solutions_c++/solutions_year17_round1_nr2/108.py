#include<bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define x first
#define y second
#define sz(a) ((int)(a).size())
#define rep(i, a, b) for(int (i) = (a); (i) < (b); (i)++)
#define dec(i, a, b) for (int (i) = (a); (i) >= (b); (i)--)
#define clr(a,v) memset(a, v, sizeof(a))
#define all(a) (a).begin(),(a).end()
#define MAXN 303030
#define LOGN 20
#define EPS 1e-8
#define fcin ios_base::sync_with_stdio(false)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

int qt[55][55], l[55][55], r[55][55], need[55], ptr[55];

int getl(int v, int p){
	return (((ll)v*10LL)/((ll)p*11LL)) + !!(((ll)v*10LL)%((ll)p*11LL));
}

int getr(int v, int p){
	return (((ll)v*10LL)/((ll)p*9LL));
}

int main(){
	int t;
	scanf("%d", &t);
	rep(caso,1,t+1){
		int n, m, ans=0;
		clr(ptr,0);
		scanf("%d%d", &n, &m);
		rep(i,0,n) scanf("%d", need+i);
		rep(i,0,n){
			rep(j,0,m) scanf("%d", &qt[i][j]);
			sort(qt[i],qt[i]+m);
			rep(j,0,m) l[i][j] = getl(qt[i][j],need[i]), r[i][j] = getr(qt[i][j],need[i]);
		}
		while(1){
			int fim=0;
			rep(i,0,n) if(ptr[i]==m) fim=1;
			if(fim) break;
			int il = 1, ir = 1e7, id=-1;
			rep(i,0,n){
				il = max(il,l[i][ptr[i]]);
				ir = min(ir,r[i][ptr[i]]);
				if(ir==r[i][ptr[i]]) id=i;
			}
			if(il <= ir){
				ans++;
				rep(i,0,n) ptr[i]++;
			}else ptr[id]++;
		}
		printf("Case #%d: %d\n", caso, ans);
	}
}

