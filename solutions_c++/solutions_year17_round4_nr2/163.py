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
int cnt[1010];
int at[1010];
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		memset(cnt,0,sizeof(cnt));
		memset(at,0,sizeof(at));
		int n,c,m;
		scanf("%d %d %d",&n,&c,&m);
		for(int i=0;i<m;i++)
		{
			int pos,who;
			scanf("%d %d",&pos,&who);
			at[pos]++;
			cnt[who]++;
		}
		int train=0;
		for(int i=1;i<=c;i++)
			train=max(train,cnt[i]);
		while(1)
		{
			bool flag=true;
			int hand=0;
			for(int i=1;i<=n && flag;i++)
			{
				hand+=train;
				hand-=at[i];
				if(hand < 0)
					flag=false;
			}
			if(flag)
				break;
			train++;
		}
		int move=0;
		for(int i=1;i<=n;i++)
			move+=max(0,at[i]-train);
		printf("Case #%d: %d %d\n",cc,train,move);
	}
	return 0;
}
/*
5
2 2 2
2 1
2 2
2 2 2
1 1
1 2
2 2 2
1 1
2 1
1000 1000 4
3 2
2 1
3 3
3 1
3 3 5
3 1
2 2
3 3
2 2
3 1

 */
