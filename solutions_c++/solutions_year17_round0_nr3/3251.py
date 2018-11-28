#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<queue>
#include<map>
#include<functional>

using namespace std;

int main()
{
	freopen("C-small-1-attempt0.in", "rt", stdin);
	freopen("c-small1.out", "wt", stdout);
	long long i, j, kase, inp, n, k, l, r;
	scanf("%lld", &inp);
	for (kase = 1; kase <= inp; kase++)
	{
		scanf("%lld %lld", &n, &k);
		long long tot = 0;
		priority_queue<long long, vector<long long>, less<long long> > que;
		map <long long, long long> vals;
		vals[n] = 1;
		que.push(n);
		while (true)
		{
			long long cur = que.top();
			que.pop();
			tot += vals[cur];
			long long d = cur / 2;
			l = d;
			if (cur % 2 == 0)
				l--;
			r = d;
			if (tot >= k)
				break;
			if (vals.find(l) == vals.end())
			{
				vals[l] = vals[cur];
				que.push(l);
			}
			else
			{
				vals[l] += vals[cur];
			}
			if (vals.find(r) == vals.end())
			{
				vals[r] = vals[cur];
				que.push(r);
			}
			else
			{
				vals[r] += vals[cur];
			}
		}
		printf("Case #%lld: %lld %lld\n", kase, r, l);
	}
	return 0;
}
