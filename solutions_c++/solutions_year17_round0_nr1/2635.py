#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

#define pb push_back
#define rs(x) scanf("%s",x)
#define ri(x) scanf("%d",&x)
#define rii(x,y) ri(x),ri(y)
#define rl(x) scanf("%lld",&x)
#define rll(x,y) rl(x),rl(y)
#define ms(obj,val) memset(obj,val,sizeof(obj))
#define ms2(obj,val,sz) memset(obj,val,sizeof(obj[0])*sz)
#define FOR(i,f,t) for(int i=f;i<(int)t;i++)
#define FORR(i,f,t) for(int i=f;i>(int)t;i--)

typedef long long ll;
typedef vector<int> vi;

const int MAXN=1010;

bool good;
int T,K,N,ans;
char S[MAXN];

int main() {
	ri(T); FOR(t,1,T+1) {
		rs(S),ri(K);
		N=strlen(S);
		ans=0;
		good=true;
		FOR(i,0,N-K+1) if(S[i]=='-') {
			ans++;
			FOR(j,i,i+K) {
				if(S[j]=='-') S[j]='+';
				else S[j]='-';
			}
		}
		FOR(i,N-K+1,N) if(S[i]=='-') good=false;
		if(good) printf("Case #%d: %d\n",t,ans);
		else printf("Case #%d: IMPOSSIBLE\n",t);
	}
}