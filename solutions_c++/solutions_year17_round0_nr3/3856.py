#include<cstdio>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<queue>
#include<cmath>
using namespace std;

long long _max,_min;
typedef pair<long long, long long> pll;
priority_queue<pair<long long, long long> > Q;

void update(long long N, long long num)
{
	if (N <= 0)
	{
		cerr << "error" << endl;
		return;
	}
	if (N & 1)
	{
		Q.push(pll(N/2ll, num * 2ll));
		_min = _max = N/2ll;
	}
	else
	{
		Q.push(pll(N/2ll, num));
		Q.push(pll(N/2ll-1ll, num));
		_min = N/2ll - 1ll;
		_max = N/2ll;
	}
}

int main(int argc, char *argv[])
{	
	if (argc == 1)
	{
		freopen("in", "r", stdin);
		freopen("out","w",stdout);
	}
	else
	{
		if (freopen(argv[1], "r",stdin) == NULL)
		{
			cerr << "open file failed" << endl;
			return 0;
		}
		freopen("ans","w",stdout);
	}
	int T_N;
	cin >> T_N;
	for (int T = 1;T <= T_N;++ T)
	{
		long long n, k;
		cin >> n >> k;
		_min = n;
		_max = 0;
		Q.push(pll(n, 1ll));

		while (k > 0)
		{
			pll now = Q.top();
			Q.pop();
			if (now.second >= k)
			{
				now.second -= k;
				update(now.first, k);
				k = 0;
				if (now.second)
					Q.push(now);
			}
			else
			{
				k -= now.second;
				update(now.first, now.second);
			}
		}

		while (!Q.empty())
			Q.pop();

		cout << "Case #" << T << ": ";
		cout << _max << " " << _min << endl;
	}
}
