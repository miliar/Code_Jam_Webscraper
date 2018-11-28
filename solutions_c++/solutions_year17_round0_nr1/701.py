#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<algorithm>
#define LF double
#define LL long long
#define ULL unsigned long long
#define min(a,b) ((a<b)?a:b)
#define max(a,b) ((a>b)?a:b)
#define fo(i,j,k) for(int i=j;i<=k;i++)
#define fd(i,j,k) for(int i=j;i>=k;i--)
#define fr(i,j) for(int i=Begin[j];i;i=Next[i])
using namespace std;
int const ml=1000+9,Inf=1e9;
int t,n,a[ml];
int main(){
	//freopen("chessboard.in","r",stdin);
	//freopen("chessboard.out","w",stdout);
	//freopen("d.in","r",stdin);
	//freopen("d.out","w",stdout);
	scanf("%d",&t);
	fo(cas,1,t){
		char ch=getchar();a[0]=0;
		while((ch!='-')&&(ch!='+'))ch=getchar();
		while((ch=='-')||(ch=='+'))a[++a[0]]=(ch=='+'),ch=getchar();
		scanf("%d",&n);int ans=0;
		fo(i,1,a[0]-n+1)if(!a[i]){
			ans++;
			fo(j,i,i+n-1)a[j]=1-a[j];
		}
		int ok=1;
		fo(i,1,a[0])if(!a[i]){ok=0;break;}
		if(ok)printf("Case #%d: %d\n",cas,ans);
		else printf("Case #%d: IMPOSSIBLE\n",cas);
	}
	return 0;
}
