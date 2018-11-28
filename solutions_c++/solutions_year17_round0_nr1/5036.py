#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#define ll long long
#define fo(i,x,y) for(int i=x;i<=y;i++)
using namespace std;
const char* fin="1.in";
const char* fout="1.out";
const int inf=0x7fffffff;
const int maxn=1006;
int t,n,m,a[maxn],b[maxn],ans;
bool judge(){
	fo(i,1,n) if (b[i]==0) return false;
	return true;
}
int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	scanf("%d",&t);
	fo(tt,1,t){
		char ch=getchar();
		while (ch!='-' && ch!='+') ch=getchar();
		n=0;
		while (ch=='-' || ch=='+') a[++n]=(ch=='+'?1:0),ch=getchar();
		scanf("%d",&m);
		ans=0;
		fo(i,1,n-m+1)
			if (a[i]==0){
				ans++;
				fo(j,i,i+m-1) a[j]^=1;
			}
		fo(i,n-m+2,n)
			if (a[i]==0) ans=inf;
		printf("Case #%d: ",tt);
		if (ans>200000000) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}