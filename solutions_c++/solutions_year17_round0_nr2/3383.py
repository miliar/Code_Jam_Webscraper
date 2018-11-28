#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string.h>
#define fo(i,a,b) for(i=a;i<=b;i++)
#define fod(i,a,b) for(i=a;i>=b;i--)
using namespace std;
const int maxn=20;
int i,j,k,l,t,n,m,ans,cas;
int a[maxn],mi[maxn];
char s[maxn];
bool bz;
int main(){
//	freopen("fan.in","r",stdin);
//	freopen("fan.out","w",stdout);
	scanf("%d",&cas);
    fo(j,1,cas){
    	if(j==100){
		    ans=ans;
		}
    	scanf("%s",s+1);
    	bz=1;ans=0;n=strlen(s+1);
    	fo(i,1,n)a[i]=s[i]-'0';l=n+1;a[l]=1000;
    	fo(i,1,n)if(a[i]<a[i-1]){l=i-1;break;}
    	k=l;
    	fod(i,l,1){k=i;if(a[i]!=a[i-1])break;}
    	printf("Case #%d: ",j);
    	if(a[k]==1){
		    fo(i,1,n-1)printf("9");
		}
		else{
			if(k<=n)a[k]--;
		/*	fod(i,k-1,1){
			    if(a[i]>a[i+1])a[i]--;
			}*/
		    fo(i,1,k-1){
		    	if(a[i])printf("%d",a[i]);
			}
		    if(k<=n)printf("%d",a[k]);
		    fo(i,k+1,n)printf("9");
		}
		printf("\n");
		//printf("Case #%d: %d\n",ans);
	}
}
