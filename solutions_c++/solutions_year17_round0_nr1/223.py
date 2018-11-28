#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<sstream>
using namespace std;
typedef long long lld;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define eps 1e-8
#define pi acos(-1.0)
char str[100010];
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		scanf("%s",str);
		int m;
		scanf("%d",&m);
		int T=('-')+('+');
		int n=strlen(str);
		int ans=0;
		for(int i=0;i<n;i++)
			if(str[i] != '+')
			{
				if(i+m > n)
				{
					ans=-1;
					break;
				}
				ans++;
				for(int j=i;j<i+m;j++)
					str[j]=T-str[j];
			}
		printf("Case #%d: ",cc);
		if(ans == -1)
			printf("IMPOSSIBLE\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}
/*
3
---+-++- 3
+++++ 4
-+-+- 4

 */
