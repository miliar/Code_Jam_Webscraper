#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <map>

using namespace std;

map<long long, long long> M;

pair<long long, long long> split(long long x)
{
	if (x & 1)
		return make_pair<long long, long long>(x/2, x/2);
	else
		return make_pair<long long, long long>(x/2, (x/2)-1);
}

void add(long long x, long long v)
{
	map<long long, long long>::iterator f = M.find(x);
	if (f != M.end())
		f->second += v;
	else
		M[x] = v;
}

long long solve(long long n, long long k)
{
	//priority_queue<long long> q;
	//q.push(n);
	M.clear();
	M[n] = 1;
	while (!M.empty())
	{
		map<long long, long long>::iterator f;
		f = M.end();
		--f;
		long long x = f->first;
		//q.pop();
		long long cnt = f->second; //M[x];
		M.erase(f);
		//printf("%lld %lld\n", x, cnt);
		if (cnt >= k)
			return x;
		k -= cnt;
		pair<long long, long long> s = split(x);
		add(s.first, cnt);
		add(s.second, cnt);
		//q.push(s.first);
		//q.push(s.second);
	}
	return 0;
}

int main()
{
	int T;
	scanf("%d\n", &T);
	for (int i=0; i<T; ++i)
	{
		long long n, k;
		scanf("%lld %lld\n", &n, &k);
		long long r = solve(n, k);
		//printf("=%lld", r);
		pair<long long, long long> s = split(r);
		printf("Case #%d: %lld %lld\n", i+1, s.first, s.second);
	}
	return 0;
}
