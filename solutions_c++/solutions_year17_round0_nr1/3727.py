#include <string>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

#define REP(i,n) for(int i=0,_n=(n);i<_n;++i)
#define GI ({int _x; scanf("%d",&_x); _x;})

inline void OPEN(string name) {
	string in = name+".in"; freopen(in.c_str(),"r",stdin);
	string out = name+".out"; freopen(out.c_str(),"w",stdout);
}

// Powered By TimoAI 2.2

char S[1024];
int K;

int main() {
	OPEN("A");
	REP(nc,GI) {
		scanf("%s %d",S,&K);
		int ans = 0;
		int n = strlen(S);
		REP(i,n) {
			if(i + K <= n) {
				// flip
				if(S[i]=='-') {
					ans++;
					REP(a,K) S[i+a] = (S[i+a]=='-' ? '+' : '-');
				}
			}else if(S[i] != '+') {
				ans = -1;
				break;
			}
		}
		printf("Case #%d: ",nc+1);
		if(ans==-1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}
