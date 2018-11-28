#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cmath>
#include <queue>

using namespace std;

struct Cake
{
	int r, h;
	double area;
	void marea()
	{
		area = ((long long)r)*(h*2);
	}
	bool operator < (const Cake &a) const
	{
		return r < a.r;//area < a.area; 
	}
};

Cake C[1000];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t=0; t<T; ++t)
	{
		int N, K;
		scanf("%d%d", &N, &K);
		for (int i=0; i<N; ++i)
		{
			scanf("%d%d", &C[i].r, &C[i].h);
			C[i].marea();
		}
		sort(C, C+N);
		priority_queue<long long> q;
		long long all = 0;
		long long r = 0;
		for (int i=0; i<N; ++i)
		{
			if (q.size() > K-1)
			{
				all += q.top();
				q.pop();
			}
			//printf("=%d %lld", C[i].r, all);
			if (q.size() == K-1)
			{
				long long d = all + C[i].area + ((long long)C[i].r)*((long long)C[i].r);
				//printf(" %lld", d);
				if (r < d)
					r = d;
			}
			//printf("\n");
			all += C[i].area;
			q.push(-C[i].area);
		}
		printf("Case #%d: %lf\n", t+1, double(r)*acos(-1.0));
	}
	return 0;
}