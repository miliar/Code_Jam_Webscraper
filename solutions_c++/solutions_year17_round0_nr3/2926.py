#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define NINF -0x3f3f3f3f

using namespace std;

typedef pair<long long,long long> pii;

bool operator < (const pii &a, const pii &b)
{
	return a.first < b.first;
}

void solve ()
{
	long long n,k;
	scanf("%lld %lld",&n,&k);
	
	map<long long, long long, greater<long long> > q;
	q.insert(pii(n,1));
	
	long long ls, rs;
	while (k > 0)
	{
		auto it = q.begin();
		
		long long len = it->first;
		long long cc = it->second;
		
		long long half = len/2LL;
		
		if (len % 2LL == 0)
		{
			q[half] += cc;
			q[half-1] += cc;
			
			ls = half;
			rs = half-1;
		}
		else
		{
			q[half] += 2LL*cc;
			
			ls = half;
			rs = half;
		}
		
		q.erase(it);
		
		k -= cc;
	}
	
	printf("%lld %lld\n",max(ls,rs),min(ls,rs));
}

int main (int argc, char const* argv[])
{
	int T;
	scanf("%d",&T);
	
	for (int t = 1; t <= T; t += 1)
	{
		printf("Case #%d: ",t);
		
		solve();
	}
	
	return 0;
}

