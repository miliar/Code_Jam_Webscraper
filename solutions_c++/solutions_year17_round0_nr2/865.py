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

int n;
char s[100];
char ans[100];
bool dfs(int p,char pre) {
	if (p>n) return 1;
	if (s[p]>=pre) {
		ans[p]=s[p];
		if (dfs(p+1,s[p])) return 1;
	}
	if (s[p]>'0'&&s[p]-1>=pre) {
		ans[p]=s[p]-1;
		for (int i=p+1;i<=n;i++) ans[i]='9';
		return 1;
	}
	return 0;
}
int main() {
	int T; scanf("%d",&T);
	for (int tt=1;tt<=T;++tt) {
		printf("Case #%d: ",tt);
		scanf("%s",s+1);
		n=strlen(s+1);
		memset(ans,0,sizeof(char)*(n+2));
		dfs(1,'0');
		puts(ans+1+(ans[1]=='0'));
	}
	return 0;
}

