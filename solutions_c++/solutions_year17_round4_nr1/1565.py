#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

int s[10];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;scanf("%d",&test);
	for (int T=1;T<=test;T++)
	{
		int n,m;scanf("%d%d",&n,&m);
		for (int i=0;i<m;i++) s[i]=0;
		int a=0;
		for (int i=0;i<n;i++)
		{
			int x;scanf("%d",&x);
			x%=m;a+=x;
			s[x]++;
		}
		a%=m;
		int ans=(a==0 ? 0 : 1);
		ans+=s[0];
		if (m==2)
			ans+=s[1]/2;
		else
			if (m==3)
			{
				ans+=min(s[1],s[2]);
				ans+=(max(s[1],s[2])-min(s[1],s[2]))/3;
			}
			else
			{
				ans+=min(s[1],s[3]);
				ans+=s[2]/2;
				int x=max(s[1],s[3])-min(s[1],s[3]);
				if (s[2]>=1&&x>=2) {ans++;x-=2;}
				ans+=x/4;
			}
		printf("Case #%d: %d\n",T,ans);
	}
	return 0;
}

