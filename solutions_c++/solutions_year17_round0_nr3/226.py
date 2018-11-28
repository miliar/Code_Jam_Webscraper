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
map<lld,lld>f;
map<lld,lld>::iterator ll;
int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		printf("Case #%d: ",cc);
		lld s;
		lld need;
		scanf("%I64d %I64d",&s,&need);
		f.clear();
		f[-s]=1;
		while(need)
		{
			ll=f.begin();
			lld s=-(ll->X);
			lld num=ll->Y;
			f.erase(ll);
			lld l=(s-1)/2;
			lld r=s-1-l;
			need-=num;
			if(need <= 0)
			{
				printf("%I64d %I64d\n",max(l,r),min(l,r));
				break;
			}
			if(l != 0)
				f[-l]+=num;
			if(r != 0)
				f[-r]+=num;
		}
	}
	return 0;
}
/*
5
4 2
5 2
6 2
1000 1000
1000 1

 */
