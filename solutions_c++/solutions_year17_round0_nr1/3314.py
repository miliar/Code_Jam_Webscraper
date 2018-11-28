#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
#define maxn 1005
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

int a[maxn];

int T,n,k,cnt;

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	fo(test,1,T) {
		n=0;
		cnt=0;
		//
		char c=getchar();
		while (c!='-' && c!='+') c=getchar();
		while (c=='-' || c=='+') {
			if (c=='-') a[++n]=0;
			else a[++n]=1;
			c=getchar();
		}
		scanf("%d",&k);
		fo(i,1,n-k+1) {
			if (a[i]==0) {
				cnt++;
				fo(j,1,k) a[i+j-1]^=1;
			}
		}
		bool ok=1;
		printf("Case #%d: ",test);
		fo(i,1,n) if (a[i]==0) ok=0;
		if (!ok) puts("IMPOSSIBLE");
		else printf("%d\n",cnt);
	}
	return 0;
}
