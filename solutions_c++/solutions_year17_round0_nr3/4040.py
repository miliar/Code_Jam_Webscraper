#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<queue>
#include<vector>
#include<set>
#include<map>
#include<cmath>

using namespace std;

map<long long, long long>mp;
queue<long long>que;
int t;
long long n, k;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		cin >> n >> k;
		cout << "Case #" << i + 1 << ": ";
		mp.clear();
		while (!que.empty())
		{
			que.pop();
		}
		que.push(n);
		mp[n] = 1;
		while (!que.empty())
		{
			long long now = que.front();
			que.pop();
			if (k>mp[now])
			{
				k -= mp[now];
				if (mp.find(now / 2) == mp.end())
				{
					mp[now / 2] = 0;
					que.push(now / 2);
				}
				mp[now / 2] += mp[now];
				if (mp.find((now-1) / 2) == mp.end())
				{
					mp[(now - 1) / 2] = 0;
					que.push((now - 1) / 2);
				}
				mp[(now - 1) / 2] += mp[now];
			}
			else
			{
				cout << now / 2 << " " << (now - 1) / 2 << "\n";
				break;
			}
		}
	}
	return 0;
}