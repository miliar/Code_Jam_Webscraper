#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <queue>

using namespace std;

#define	sqr(a)		((a)*(a))
#define	rep(i,a,b)	for(int i=(a);i<(int)(b);i++)
#define	per(i,a,b)	for(int i=((a)-1);i>=(int)(b);i--)
#define	PER(i,n)	per(i,n,0)
#define	REP(i,n)	rep(i,0,n)
#define	clr(a)		memset((a),0,sizeof (a))
#define	SZ(a)		((int)((a).size()))
#define	ALL(x)		x.begin(),x.end()
#define	mabs(a)		((a)>0?(a):(-(a)))
#define	inf			(0x7fffffff)
#define	eps			1e-6

typedef long long ll;

#define TEST_LOCAL 1

int a[55];
int b[55][55];
int c[55][55][2];
int mp[2505][2505];
int ret[2505][2505];

#define MAXN 2505
#define inf 1000000000

int max_flow(int n,int mat[][MAXN],int source,int sink,int flow[][MAXN]){
	int pre[MAXN],que[MAXN],d[MAXN],p,q,t,i,j;
	if (source==sink) return inf;
	for (i=0;i<n;i++)
		for (j=0;j<n;flow[i][j++]=0);
	for (;;){
		for (i=0;i<n;pre[i++]=0);
		pre[t=source]=source+1,d[t]=inf;
		for (p=q=0;p<=q&&!pre[sink];t=que[p++])
			for (i=0;i<n;i++)
				if (!pre[i]&&(j=mat[t][i]-flow[t][i]))
					pre[que[q++]=i]=t+1,d[i]=d[t]<j?d[t]:j;
				else if (!pre[i]&&(j=flow[i][t]))
					pre[que[q++]=i]=-t-1,d[i]=d[t]<j?d[t]:j;
		if (!pre[sink]) break;
		for (i=sink;i!=source;)
			if (pre[i]>0)
				flow[pre[i]-1][i]+=d[sink],i=pre[i]-1;
			else
				flow[i][-pre[i]-1]-=d[sink],i=-pre[i]-1;
	}
	for (j=i=0;i<n;j+=flow[source][i++]);
	return j;
}


int main()
{
	freopen("data.in","r",stdin);
#if TEST_LOCAL
	freopen("data.out","w",stdout);
#endif

	int T;
	scanf("%d",&T);

	for (int K = 1;K <= T;K++)
	{
		int n,p;
		scanf("%d %d",&n,&p);
		REP(i,n)
		{
			scanf("%d",&a[i]);
		}
		REP(i,n)
		{
			REP(j,p)
			{
				scanf("%d",&b[i][j]);
			}
		}
		REP(i,n)
		{
			REP(j,p)
			{
				c[i][j][0] = (b[i][j] * 10 + a[i] * 11 - 1) / (a[i] * 11);
				c[i][j][1] = b[i][j] * 10 / (a[i] * 9);
			}
		}

		memset(mp,0,sizeof(mp));

		REP(i,n - 1)
		{
			REP(j,p)
			{
				int p1 = i * p + j;
				int x1 = c[i][j][0];
				int y1 = c[i][j][1];
				if (x1 <= y1)
				{
					REP(k,p)
					{
						int p2 = (i + 1) * p + k; 
						int x2 = c[i + 1][k][0];
						int y2 = c[i + 1][k][1];
						if (x2 <= y2)
						{
							if (x1 <= y2 && x2 <= y1)
							{
								mp[p1][p2] = 1;
								mp[p2][p1] = 1;
							}
						}
					}
				}
			}
		}
		int be = n * p;
		int en = n * p + 1;
		REP(j,p)
		{
			if (c[0][j][0] <= c[0][j][1])
			{
				mp[be][j] = 1;
				mp[j][be] = 1;
			}
			if (c[n - 1][j][0] <= c[n - 1][j][1])
			{
				mp[(n - 1) * p + j][en] = 1;
				mp[en][(n - 1) * p + j] = 1;
			}
			
		}

		
		int res = max_flow(en + 1,mp,be,en,ret);


		printf("Case #%d: ",K);
		printf("%d\n",res);
	}


	return 0;
}
