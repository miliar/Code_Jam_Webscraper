#include<cstdio>
#include<deque>

using namespace std;

struct elem
{
	unsigned long long int val;
	unsigned long long int times;
};
		
int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{  
		unsigned long long int n, k;
		scanf("%llu %llu", &n, &k);
		printf("Case #%d: ", tt);
		deque<elem> q;
		elem e;
		e.val = n;
		e.times = 1;
		q.push_back(e);
		while(q.front().times < k)
		{
			elem e = q.front();
			k -= e.times;
			q.pop_front();
			if(e.val & 1)
			{
				elem e2;
				e2.val = e.val >> 1;
				e2.times = e.times << 1;
				if(!q.empty() && q.back().val == e2.val)
					q.back().times += e2.times;
				else
				{
					q.push_back(e2);
				}
			}
			else
			{
				elem e2;
				e2.val = e.val >> 1;
				e2.times = e.times;
				elem e3;
				e3.val = e2.val - 1;
				e3.times = e.times;
				if(!q.empty() && q.back().val == e2.val)
					q.back().times += e2.times;
				else
				{
					q.push_back(e2);
				}
				q.push_back(e3);
			}
		}
		unsigned long long int v = q.front().val;
		unsigned long long int v2 = v >> 1;
		printf("%llu ", v2);
		if(!(v & 1))
		{
			--v2;
		}
		printf("%llu\n", v2);
	}
	return 0;
}

