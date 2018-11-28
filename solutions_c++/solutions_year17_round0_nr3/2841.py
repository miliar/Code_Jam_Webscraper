#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <utility>
#include <map>

typedef long long ll;
typedef std::pair<ll, ll> ii;

int main()
{
	int t;
	std::cin >> t;
	for(int te = 1; te <= t; te++)
	{
		std::priority_queue<ll> hp;
		std::map<ll, ll> freq;
		ll n, k;
		std::cin >> n >> k;
		freq[n] = 1;
		hp.push(n);
		while(freq[hp.top()] < k)
		{
			ll cur = hp.top();
			hp.pop();
			//std::cout << "got " << freq[cur] << " on size " << cur << '\n';
			ll l, r;
			if(cur % 2 == 1)
				l = r = cur / 2;
			else
			{
				r = cur / 2;
				l = cur / 2 - 1;
			}
			if(!freq[l])
				hp.push(l);
			if(r != l && !freq[r])
				hp.push(r);
			freq[l] += freq[cur];
			freq[r] += freq[cur];
			k -= freq[cur];
		}
		ll max, min;
		if(hp.top() % 2 == 1)
		{
			max = min = hp.top() / 2;
		}
		else
		{
			max = hp.top() / 2;
			min = max - 1;
		}
		std::cout << "Case #" << te << ": " << max << " " << min << '\n';
	}
}