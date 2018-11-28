#include<set>
#include<map>
#include<queue>
#include<cmath>
#include<string>
#include<cstdio>
#include<vector>
#include<cassert>
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

int n,P;
int a[N];
int num[5];

int main() {

	#ifndef ONLINE_JUDGE
		freopen("A-small-attempt0 (1).in","r",stdin);
		freopen("data.out","w",stdout);
	#endif

	int T=read();
	rep(cas,1,T) {
		n=read(),P=read(); memset(num,0,sizeof(num));
		rep(i,1,n) {a[i]=read(); num[a[i]%P]++;}
		int ans=0;
		if (P==2) {
			ans=num[0]+(num[1]+1)/2;
		} else if (P==3) {
			int tmp=min(num[1],num[2]);
			ans=num[0]+tmp;
			num[1]-=tmp; num[2]-=tmp;
			if (num[1]) {
				ans+=(num[1]+2)/3;
			} else if (num[2]) {
				ans+=(num[2]+2)/3;
			}
		} else if (P==4) {
		}
		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}

