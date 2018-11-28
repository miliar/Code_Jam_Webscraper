#include<cstdio>
#include<algorithm>
#include<cstring>
#include<bitset>
#include<cmath>
#define fo(i,j,k) for(i=j;i<=k;i++)
#define fd(i,j,k) for(i=j;i>=k;i--)
typedef long long ll;
typedef double db;
using namespace std;
const int maxn=1005;
int a[maxn],ans,i,j,K,len,bz,T,l;char s[maxn];
int main(){
	//freopen("t1.in","r",stdin);
	//freopen("t1.out","w",stdout);
	scanf("%d\n",&T);
	fo(l,1,T){
		char ch;
		for(ch=getchar();ch!='-'&&ch!='+';ch=getchar());
		len=0;
		for(;ch=='-'||ch=='+';ch=getchar()) s[++len]=ch;
		fo(i,1,len) if (s[i]=='+') a[i]=1;else a[i]=0;
		scanf("%d\n",&K);
		ans=0;
		fo(i,1,len-K+1)if (!a[i]){
			fo(j,i,i+K-1)a[j]^=1;
			ans++;
		}
		bz=1;
		fo(i,len-K+1,len) if (!a[i])bz=0;
		printf("Case #%d: ",l);
		if (!bz) printf("IMPOSSIBLE\n");else
		printf("%d\n",ans); 
	}
}
