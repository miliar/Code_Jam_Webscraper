// CJE3.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <functional>
#include <climits>
#include <unordered_map>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0); cin.tie(0);
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	long T, lp;
	long long ans;
	cin >> T;
	for (lp = 1;lp <= T;lp++)
	{
		long long N, K, ans1, ans2;
		cin >> N >> K;
		unordered_map<long long, long long> mp;
		set<long long> st;
		st.insert(N);
		mp[N] = 1;
		while (K > 0)
		{
			long long num = *st.rbegin();
			long long n1 = num / 2, n2 = (num - 1) / 2;
			if (K - mp[num] >= 0)
			{
				K -= mp[num];
				if (mp.find(n1) != mp.end())
				{
					mp[n1] += mp[num];
				}
				else
				{
					mp[n1] = mp[num];
				}
				if (mp.find(n2) != mp.end())
				{
					mp[n2] += mp[num];
				}
				else
				{
					mp[n2] = mp[num];
				}
				st.erase(num);
				st.insert(n1);
				st.insert(n2);
				mp.erase(num);
			}
			else
			{
				mp[num] -= K;
				K = 0;
				if (mp.find(n1) != mp.end())
				{
					mp[n1] += mp[num];
				}
				else
				{
					mp[n1] = mp[num];
				}
				if (mp.find(n2) != mp.end())
				{
					mp[n2] += mp[num];
				}
				else
				{
					mp[n2] = mp[num];
				}
				st.insert(n1);
				st.insert(n2);
			}
			ans1 = n1, ans2 = n2;
		}
		cout << "Case #" << lp << ": " << max(ans1, ans2) << " " << min(ans1, ans2) << "\n";
	}
	return 0;
}

