#include <iostream>
#include <queue>
#include <math.h>
#include <string.h>
#include <vector>
using namespace std;
typedef long long LL;
const int N = 10005;
const LL INF = 0x3f3f3f3f;
const double Pi = acos(-1);

#define BUG

int n,m,k;
double a,b,x;
struct nd
{
	int l,r;
	int id;
}s[N];

void INIF() {
#ifdef BUG 
	freopen("B-small-attempt0.in","r",stdin); 
	freopen("B-small-attempt0.txt","w",stdout); 
#endif 
}

int t[N];

int cmp(nd a,nd b)
{
	return a.l<b.l;
}

int main()
{

	INIF();
	int kk;
	scanf("%d",&kk);
	for (int cc=1;cc<=kk;cc++)
	{
		scanf("%d%d",&n,&m);
		int pos=0;
		// int p=0;
		for (int i=0;i<n;i++)
		{
			scanf("%d%d",&s[pos].l,&s[pos].r);
			s[pos].id=0;
			pos++;
		}
		for (int i=0;i<m;i++)
		{
			scanf("%d%d",&s[pos].l,&s[pos].r);
			s[pos].id=1;
			pos++;
		}
		sort(s,s+pos,cmp);
		int st[3];
		int ed[3];
		int state=s[0].id;
		int res=1;
		int ans=1;
		int beg;
		vector <int> p;
		for (int i=0;i<pos-1;i++)
		{
			if (s[i].id!=s[i+1].id)
			{
				ans++;
				p.push_back(i);
			}
		}
		for (int i=0;i<pos-1;i++)
		{
			if (s[i].id==s[i+1].id)
			{
				// ans++;
				if (s[i+1].r-s[i].l>720)
					ans+=2;
			}
		}
		if (s[0].id ==s[pos-1].id && s[0].r+1440-s[pos-1].l>720)
			ans++;
		else if (s[0].id ==s[pos-1].id && s[0].r+1440-s[pos-1].l<=720)
			ans--;
		// for (int ss=0;ss<=s[0].l;ss++)
		// {
		// 	beg=ss;
		// 	res=1;
		// 	int f=0;
		// 	for (int i=1;i<pos;i++)
		// 	{
		// 		if (state != s[i].id)
		// 		{
		// 			res++;
		// 			state = s[i].id;
		// 			beg = s[i].id;
		// 		}
		// 		else
		// 		{
		// 			if (s[i].r-st[state]>720)
		// 			{
		// 				res+=2;
		// 				beg=s[i].l;
		// 			}
		// 		}
		// 	}
		// 	ans=min(ans,res);
		// }
		printf("Case #%d: %d\n",cc, ans);
	}
	return 0;
}
/*

5
1 1
540 600
840 900
2 0
900 1260
180 540
1 1
1439 1440
0 1
2 2
0 1
1439 1440
1438 1439
1 2
3 4
0 10
1420 1440
90 100
550 600
900 950
100 150
1050 1400

*/
