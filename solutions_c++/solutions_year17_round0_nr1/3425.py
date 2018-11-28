#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#define fo(i,a,b) for(i=a;i<=b;i++)
using namespace std;
const int maxn=1e4+7;
int i,j,k,l,t,n,m,ans,cas;
int a[maxn];
char s[maxn];
bool bz;
int main(){
	freopen("fan.in","r",stdin);
	freopen("fan.out","w",stdout);
	scanf("%d",&cas);
    fo(j,1,cas){
    	scanf("%s",s+1);scanf("%d",&k);
    	bz=1;ans=0;
    	n=strlen(s+1);
    	s[0]='-',s[n+1]='-';
    	fo(i,1,n+1){
		    if(s[i]!=s[i-1])a[i]=1;
		    else a[i]=0;
		}
		if(!a[1]&&k<=n)a[1+k]=1-a[1+k],a[1]=1,ans++;
		fo(i,2,n-k+1)if(a[i])a[i]=0,a[i+k]=1-a[i+k],ans++;
		if(!a[1]||!a[n+1])bz=0;
		fo(i,2,n)if(a[i])bz=0;
		if(bz)printf("Case #%d: %d\n",j,ans);
		else printf("Case #%d: IMPOSSIBLE\n",j);
	}
}
