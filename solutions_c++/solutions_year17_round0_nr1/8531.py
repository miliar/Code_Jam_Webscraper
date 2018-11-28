#include <bits/stdc++.h>
#include <unordered_set>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;

typedef long long ll;

int T;
int k;
int l;

bool vis[2000];
int dp[2000];

const int INF = 1000000000;

void printbin(int n) {
	for(int i=0;i<l;i++) {
		if(n&(1<<(l-i-1))) {
			printf("1");
		}else printf("0");
	}
	puts("");
}

int cagar(int n, int u) {
	/*printf("%d ",u);
	printbin(n);*/
	for(int i=u;i<u+k;i++) {
		n^=(1<<i);
	}
	//printbin(n);
	return n;
}

int solve(int n) {
	if(vis[n]) return dp[n];
	else {
		vis[n]=true;
		int r=INF;
		for(int i=0;i<l-k+1;i++) {
			r=min(r,solve(cagar(n,i)));
		}
		dp[n]=1+r;
		return 1+r;
	}
}

int main() {
	scanf("%d",&T);
	int u=1;
	while(T--) {
		memset(dp,0,sizeof(dp));
		memset(vis,0,sizeof(vis));
		string s;
		cin >> s;
		scanf("%d",&k);
		int st=0;
		for(int i=s.size()-1;i>=0;i--) {
			if(s[i]=='-') {
				st|=(1<<(s.size()-1-i));
			}
		}
		l=s.size();
		vis[0]=true;
		dp[0]=0;
		for(int i=1;i<2000;i++) {
			dp[i]=INF;
		}

		if(solve(st)<INF) printf("Case #%d: %d\n",u,solve(st));
		else printf("Case #%d: IMPOSSIBLE\n",u);
		u++;
	}
	return 0;
}