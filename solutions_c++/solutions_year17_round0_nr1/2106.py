#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

#define pb push_back
#define ri(x) scanf("%d",&x)
#define rii(x,y) ri(x),ri(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)
#define EPS 1e-28
#define PI 2*acos(0.0)
#define y1 fdsadfa
typedef long long ll;
typedef vector<int> vi;

const int MAXN = 2000;
char S[MAXN];
int T, n, K, ac, ans;
vi L, C;
bool pos;
int main(){
	ri(T);
	FOR(t, 1, T+1){
		scanf("%s", S);
		ri(K);
		n = strlen(S);
		L.clear();
		C.resize(n);
		FOR(i, 0, n) C[i] = 0;
		ac = 0, ans = 0, pos = true;
		FOR(i, 0, n){
			if(S[i] == '+') L.pb(1);
			else            L.pb(0);
		}

		
		FOR(i, 0, n-K+1){
			if(i-K>=0 && C[i-K]==1) ac = (ac+1)%2;
			L[i] = (L[i]+ac)%2;
			if(L[i] == 0) ac = (ac+1)%2, C[i] = 1, ans++, L[i]++;
		}
		
		
		FOR(i, n-K+1, n){
			if(i-K>=0 && C[i-K]==1) ac = (ac+1)%2;
			L[i] = (L[i]+ac)%2;
		}

		FOR(i, 0, n) pos = pos && L[i];
		
		printf("Case #%d: ", t);
		if(pos) printf("%d\n", ans);
		else    printf("IMPOSSIBLE\n");
		
	}
}
