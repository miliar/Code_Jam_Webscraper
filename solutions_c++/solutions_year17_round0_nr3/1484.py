#include <cstdio>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;

map<ll, ll> cnt;
priority_queue<ll> Q;

void domain()
{
	cnt.clear();

	ll N, K;

	cin >> N >> K;

	while (!Q.empty())	Q.pop();

	Q.push(N);
	cnt[N] = 1;

	while (K)
	{
		ll cur = Q.top(); Q.pop();

		ll all = cnt[cur];

		ll l = (cur & 1) ? cur / 2 : (cur / 2 - 1);
		ll r = cur - l - 1;

		if (l > 0)
		{
			if (!cnt.count(l))	Q.push(l);
			cnt[l] = cnt[l] + all;
		}
		if (r > 0)
		{
			if (!cnt.count(r))	Q.push(r);
			cnt[r] = cnt[r] + all;
		}

		if (all >= K)
		{
			cout << max(l,r) << " " << min(l,r) << endl;
			break;
		}
		else
		{
			K -= all;
		}

	}

}

int main()
{
	int T;
	//cin.sync_with_stdio(false);
	scanf("%d\n", &T);

	for (int i = 1; i <= T; ++i)
	{
		printf("Case #%d: ", i);
		domain();
	}

	return 0;
}