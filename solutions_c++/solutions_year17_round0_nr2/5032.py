#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#define ll unsigned long long
#define fo(i,x,y) for(int i=x;i<=y;i++)
#define fd(i,x,y) for(int i=x;i>=y;i--)
using namespace std;
const char* fin="2.in";
const char* fout="2.out";
const ll inf=0x7fffffff;
ll t,n,p[19],ans=0;
int main(){
	freopen(fin,"r",stdin);
	freopen(fout,"w",stdout);
	scanf("%d",&t);
	p[0]=0;
	fo(i,1,18) p[i]=p[i-1]*10+1;
	fo(tt,1,t){
		scanf("%llu",&n);
		ans=0;
		int num=0;
		fd(i,18,1){
			while (ans+p[i]<=n){
				ans+=p[i];
				if (++num==9) break;
			}
			if (num==9) break;
		}
		printf("Case #%d: %llu\n",tt,ans);
	}
	return 0;
}