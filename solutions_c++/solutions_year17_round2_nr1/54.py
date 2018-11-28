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
int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		double end;
		int n;
		scanf("%lf %d",&end,&n);
		double ans=0;
		for(int i=0;i<n;i++)
		{
			double v,len;
			scanf("%lf %lf",&len,&v);
			len=end-len;
			double t=len/v;
			if(ans == 0)
				ans=end/t;
			else
				ans=min(ans,end/t);
		}
		printf("Case #%d: %.8f\n",cc,ans);
	}
	return 0;
}
