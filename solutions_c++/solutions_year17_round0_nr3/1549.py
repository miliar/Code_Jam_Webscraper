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

LL n,k;
LL ans1,ans2;

void Calc(LL x,LL a,LL b,LL rem) { //a->even b->odd
	if (x&1) {
		if (rem<=b) {
			ans1=ans2=x/2;
			return;
		} else if (rem<=a+b) {
			ans1=x/2; ans2=x/2-1;
			return;
		}
	} else {
		if (rem<=a) {
			ans1=x/2; ans2=x/2-1;
			return;
		} else if (rem<=a+b) {
			ans1=ans2=x/2-1;
			return;
		}
	}
	LL cnt1=0,cnt2=0; //1->even 2->odd
	if (x&1) {
		if ((x/2)&1) cnt2=a+b*2,cnt1=a;
		else cnt1=a+b*2,cnt2=a;
	} else {
		if ((x/2)&1) cnt2=a,cnt1=a+b*2;
		else cnt1=a,cnt2=a+b*2;
	}
	Calc(x/2,cnt1,cnt2,rem-(a+b));
}

int main() {

	#ifndef ONLINE_JUDGE
		freopen("C-large.in","r",stdin);
		freopen("data.out","w",stdout);
	#endif

	int T=read();
	rep(t,1,T) {
		printf("Case #%d: ",t);
		scanf("%lld%lld",&n,&k);
		Calc(n,1-(n&1),n&1,k);
		printf("%lld %lld\n",ans1,ans2);
	}

	return 0;
}

