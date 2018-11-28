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

LL n;
int tot,a[105],ans[105];

int main() {

	#ifndef ONLINE_JUDGE
		freopen("B-large.in","r",stdin);
		freopen("data.out","w",stdout);
	#endif

	int T=read();
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%lld",&n);
		memset(a,0,sizeof(a));
		tot=0; while (n) {a[++tot]=n%10; n/=10;}
		int pos=tot-1; ans[tot]=a[tot]; 
		while (pos) {
			if (a[pos]<a[pos+1]) break;
			ans[pos]=a[pos];
			pos--;
		}
		if (pos) {
			int tmp=pos+1;
			while (tmp<=tot&&a[tmp]==a[tmp+1]) tmp++;
			ans[tmp]--;
			rep(i,1,tmp-1) ans[i]=9;
		}
		if (ans[tot]) printf("%d",ans[tot]);
		per(i,tot-1,1) printf("%d",ans[i]);
		puts("");
	}

	return 0;
}

