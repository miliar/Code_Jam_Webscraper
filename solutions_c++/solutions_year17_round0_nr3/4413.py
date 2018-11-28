#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>

using namespace std;

int T;

long long n,k;

priority_queue<pair<long long,long long> > heap;

void merge()
{
	long long nowl = heap.top().first;
	long long nowc = 0;
	while (heap.size() && heap.top().first==nowl)
	{
		nowc+=heap.top().second;
		heap.pop();
	}
	heap.push(make_pair(nowl,nowc));
}

int main()
{
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		while (heap.size())
			heap.pop();
		scanf("%lld%lld",&n,&k);
		heap.push(make_pair(n,1));

		k--;

		while (k)
		{
			merge();
			pair<long long,long long> top = heap.top();
			heap.pop();

			long long nowl = top.first;
			long long nowc = top.second;
			if (nowl%2==1)
			{
				if (nowc>k)
				{
					heap.push(make_pair(nowl,nowc-k));
					heap.push(make_pair(nowl/2,k*2));
					k=0;
				}
				else
				{
					heap.push(make_pair(nowl/2,nowc*2));
					k-=nowc;
				}
			}
			else
			{
				if (nowc>k)
				{
					heap.push(make_pair(nowl,nowc-k));
					heap.push(make_pair(nowl/2-1,k));
					heap.push(make_pair(nowl/2,k));
					k=0;
				}
				else
				{
					heap.push(make_pair(nowl/2-1,nowc));
					heap.push(make_pair(nowl/2,nowc));
					k-=nowc;
				}
			}
		}
		printf("Case #%d: ",t);

		long long l = heap.top().first;
		if (l%2==0) printf("%lld %lld\n",l/2,l/2-1);
		else printf("%lld %lld\n",l/2,l/2);
	}

	return 0;
}
