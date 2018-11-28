#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<string>
#include<cstdio>
#include<vector>
#include<cstring>
#include<iostream>
#include<algorithm>
#define rep(i,a,b) for (int i=a; i<=b; i++)
#define per(i,a,b) for (int i=a; i>=b; i--)
#define debug(x) {cout<<(#x)<<" "<<x<<endl;}
using namespace std;
typedef long long LL;

inline int read() {
    int x=0,f=1; char ch=getchar();
    while (!(ch>='0'&&ch<='9')) {if (ch=='-')f=-1;ch=getchar();}
    while (ch>='0'&&ch<='9') {x=x*10+(ch-'0'); ch=getchar();}
    return x*f;
}

const int N = 105;
const int C = 24*60;

int n,m;
int used[C+2];
int dp1[C+2][C+2][3],dp2[C+2][C+2][3];

inline void Init() {
	n=read(),m=read();
	memset(used,0,sizeof(used));
	rep(i,1,n) {
		int l=read(),r=read(); rep(j,l+1,r) used[j]=1;
	}
	rep(i,1,m) {
		int l=read(),r=read(); rep(j,l+1,r) used[j]=2;
	}
	rep(i,0,C) rep(j,0,C) rep(k,1,2) dp1[i][j][k]=dp2[i][j][k]=C;
}

inline void Dp() {
	dp1[0][0][1]=dp2[0][0][2]=0;
	rep(i,1,C) {
		if (used[i]!=2) {
			dp1[i][0][2]=min(dp1[i-1][0][1]+1,dp1[i-1][0][2]); 
			dp2[i][0][2]=min(dp2[i-1][0][1]+1,dp2[i-1][0][2]);
		}
		rep(j,1,C/2) {
			if (used[i]!=1) {
				dp1[i][j][1]=min(dp1[i-1][j-1][1],dp1[i-1][j-1][2]+1);
				dp2[i][j][1]=min(dp2[i-1][j-1][1],dp2[i-1][j-1][2]+1);
			}
			if (used[i]!=2) {
				dp1[i][j][2]=min(dp1[i-1][j][1]+1,dp1[i-1][j][2]);
				dp2[i][j][2]=min(dp2[i-1][j][1]+1,dp2[i-1][j][2]);
			}
		}
	}
	//cout<<used[361]<<endl;
	//cout<<dp2[361][1][1]<<endl;
	//rep(i,1,360) cout<<dp2[i][0][2];
}

int main() {

	#ifndef ONLINE_JUDGE
		freopen("B-large (1).in","r",stdin);
		freopen("data.out","w",stdout);
	#endif

	int T=read();
	rep(cas,1,T) {
		Init();
		Dp();
		int ans=C;
		if (used[C]!=1) ans=min(ans,dp1[C][C/2][1]);
		if (used[C]!=2) ans=min(ans,dp2[C][C/2][2]);
		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}

