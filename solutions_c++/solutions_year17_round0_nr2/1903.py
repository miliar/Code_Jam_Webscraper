#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

#define X first
#define Y second
#define N 1010
#define M 500010

typedef long long ll;
const int INF=1ll<<30;

char s[N];

void Solve(int n,int k)
{
	if (k>n)
	{
		bool flag=true;
		for (int i=1;i<=n;i++) if (s[i]=='-') flag=false;
		if (flag) printf("0\n");
		else printf("IMPOSSIBLE\n");
		return;
	}
	int res=0; bool flag=true;
	for (int i=1;i<=n-k+1;i++)
	{
		if (s[i]=='-')
		{
			res++;
			for (int j=i;j<=i+k-1;j++)
			{
				if (s[j]=='+') s[j]='-';
				else s[j]='+';
			}
		}
	}
	for (int i=n-k+2;i<=n;i++) if (s[i]=='-') flag=false;
	if (flag) printf("%d\n",res);
	else printf("IMPOSSIBLE\n");
}

int main()
{
	//freopen("in.in","r",stdin);
	//freopen("B.out","w",stdout);
	
	int T; ll n; scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		printf("Case #%d: ",cas);
		scanf("%I64d",&n);
		if (n<=9) printf("%I64d\n",n);
		else
		{
			int b[20],m=0,pos; ll x=n;
			while (x) b[++m]=x%10,x/=10;
			for (pos=m;pos>1 && b[pos]<=b[pos-1];pos--);
			if (pos==1) printf("%I64d\n",n);
			else
			{
				int pos2=pos;
				while (pos2<m && b[pos2+1]==b[pos]) pos2++;
				b[pos2]--;
				for (int i=pos2-1;i>=1;i--) b[i]=9;
				if (!b[m]) m--;
				for (int i=m;i>=1;i--) printf("%d",b[i]);
				printf("\n");
			} 
		}
	}
	
	return 0;
}
