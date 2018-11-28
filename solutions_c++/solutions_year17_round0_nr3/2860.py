#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <set>
#include <utility>
#include <map>
using namespace std;
map<long long, long long> mp;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	long long n, k;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		cin >> n >> k;
		mp.clear();
		mp[n]=1;
		while (true)
		{
			auto tmp = mp.rbegin();
			if (tmp->second >= k) break;
			k -= tmp->second;
			if(tmp->first & 1) mp[tmp->first/2] += tmp->second * 2;
			else mp[tmp->first / 2] += tmp->second, mp[tmp->first / 2 - 1] += tmp->second;
			mp.erase(tmp->first);
		}
		auto tmp = mp.rbegin();
		cout << "Case #" << i << ": " << tmp->first / 2 << " " << (tmp->first - 1) / 2 << endl;
	}
	return 0;
}