#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define pi 3.141592654

struct P
{
int r,h;
long long s1, s2, s;
}c[1001];
bool operator<(P a, P b)
{
 if(a.s1 != b.s1)
 return a.s1 < b.s1;
 return a.s2 < b.s2;
}
		
int main()
{
//freopen("1.in","r",stdin);
//freopen("1.out","w",stdout);
	int T;
	scanf("%d",&T);
	int t;
	for(int t = 1; t < T+1; t++)
	{
		printf("Case #%d: ",t);
		int n,k;
		scanf("%d %d",&n, &k);
		
	
		for(int i = 0; i < n; i++)
		{
			P tmp;
			scanf("%d %d", &tmp.r, &tmp.h);
			c[i] = tmp;
			c[i].s = (long long)c[i].r*c[i].r +(long long) c[i].r*2*c[i].h;;
			c[i].s1 = (long long)c[i].r*c[i].r;
			c[i].s2 = (long long)c[i].r*c[i].h*2;
		//	printf("de %d %lld\n",i,c[i].s);
		}
		
		sort(c,c+n);
		priority_queue<long long, std::vector<long long>, std::greater<long long>> hh;
		long long sum = 0;

		for(int i = 0; i < k; i++)
		{
			hh.push(c[i].s2);
			sum +=c[i].s2;
		}
		
		sum += c[k-1].s1;
		long long cs1 = c[k-1].s1;
		for(int i = k; i < n; i++)
		{
		     long long smal = hh.top();
		     long long delt;
		     delt = c[i].s1 - cs1 + c[i].s2;
		     if(delt > smal)
		     {
		     	//printf("de %d %d\n",delt,smal);
		      	hh.pop();
		      	hh.push(c[i].s2);
		      	cs1 = c[i].s1;
		      	sum += delt - smal;
		     }
		}
		
		printf("%.8lf\n",pi*sum);
	}
}

