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

const int N = 1005;

int k[N],s[N];

int main() {

	#ifndef ONLINE_JUDGE
		freopen("A-large (1).in","r",stdin);
		freopen("data.out","w",stdout);
	#endif

	int T=read();
	rep(cas,1,T) {
		int d=read(),n=read();
		double ans=0;
		rep(i,1,n) {
			k[i]=read(),s[i]=read();
			ans=max(ans,((double)d-k[i])/(double)s[i]);
		}
		ans=(double)d/ans;
		
		printf("Case #%d: %lf\n",cas,ans);
		
	}

	return 0;
}

