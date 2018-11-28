#include<stdio.h>
#include<algorithm>
#include<queue>
#include<functional>

using namespace std;

typedef pair<long long, long long> pp;

priority_queue<pp> Q;

long long n, k;

int main(void)
{
	freopen("C-large.in","r", stdin);
	freopen("C-large.out","w", stdout);
	int T, t=0;
	scanf("%d",&T);
	while(T--)
	{
		t++;
		printf("Case #%d: ",t);

		scanf("%lld %lld",&n,&k);

		while(!Q.empty())
			Q.pop();

		Q.push(make_pair(n,1));

		while(!Q.empty())
		{
			long long a, b;
			a = Q.top().first;
			b = Q.top().second;
			Q.pop();
			while(!Q.empty())
			{
				if(a != Q.top().first)
					break;
				b += Q.top().second;
				Q.pop();
			}

			if(b >= k)
			{
				printf("%lld %lld\n",a/2, (a-1)/2);
				break;
			}
			else
			{
				k-=b;
				if(a&1)
				{
					if(a/2)
						Q.push(make_pair(a/2, 2*b));
				}
				else
				{
					if(a/2)
						Q.push(make_pair(a/2, b));
					if((a-1)/2)
						Q.push(make_pair((a-1)/2, b));
				}
			}
		}
	}
}