#include <bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define FOR(i,l,r) for(int i=(l);i<(r);++i)
#define REP(i,a) FOR(i,0,a)
#define all(c) begin(c), end(c)
#define uniquenize(v) (v).erase(unique(all(v)), end(v))
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
const int maxn=1e5+1;
template<class T> inline void maxi(T &a,T b) { if (a<b) a=b; }

char s[1010];
int k;
int fto[1000];
int main() {
	fto['-']='+';
	fto['+']='-';

	int T; scanf("%d",&T);
	for (int tt=1;tt<=T;++tt) {
		scanf("%s%d",s+1,&k);
		int n=strlen(s+1);
		int ans=0;
		for (int i=1;i<=n-k+1;++i) {
			if (s[i]=='-') {
				++ans;
				for (int j=i;j<=i+k-1;++j) {
					s[j]=fto[s[j]];
				}
			}
		}
		for (int i=n-k+2;i<=n;++i) {
			if (s[i]=='-') ans=-1;
		}
		printf("Case #%d: ",tt);
		if (ans==-1) puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}

