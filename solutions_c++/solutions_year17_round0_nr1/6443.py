#include<cstdio>
#include<cstring>
#define F(i,a,b) for(int i=a;i<=b;++i)
using namespace std;
typedef long long ll;
#define ___ freopen("d:\\acm\\input.txt","r",stdin);
const int N=1007;
char a[N];
int cas;

int main(){
	
	int t,l,len;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%s",a+1);
		scanf("%d",&l);
		len=strlen(a+1);
		int ans=0;
		for(int i=1;i+l-1<=len;i++)
		{
			if(a[i]=='-')
			{
				//printf("i=%d\n",i);
				ans++;
				for(int j=0;j<l;j++)
				{
					if(a[i+j]=='-')a[i+j]='+';
					else a[i+j]='-';
				}
			}
			
		}
		for(int i=1;i<=len;i++)if(a[i]=='-'){ans=-1;break;}
		printf("Case #%d: ",++cas);
		if(ans==-1)puts("IMPOSSIBLE");
		else printf("%d\n",ans);
	}
	return 0;
}