#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cmath>
#include <stack>
#include <functional>
#include <set>
#include <queue>
#include <string>
#include <map>
#include <iomanip>
#include <sstream>

using namespace std;


int main()
{
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cout << "Case #" << t + 1 << ": ";
		long long int N, K;
		cin >> N >> K;
		priority_queue <long long int> q;
		map <long long int, long long int> cnt;
		cnt[N] = 1;
		q.push(N);
		while (true)
		{
			long long int sz = q.top();
			q.pop();
			K -= cnt[sz];
			if (K <= 0)
			{
				cout << sz / 2 << ' ' << (sz - 1) / 2 << endl;
				break;
			}
			if (sz % 2 == 0)
			{
				if (cnt[(sz - 1) / 2 ] == 0)
					q.push((sz - 1) / 2);
				cnt[(sz - 1) / 2] += cnt[sz];
				if (cnt[sz / 2] == 0)
					q.push(sz / 2);
				cnt[sz / 2] += cnt[sz];
			}
			else
			{
				if (cnt[sz / 2] == 0)
					q.push(sz / 2);
				cnt[sz / 2] += cnt[sz] * 2;
			}
			cnt[sz] = 0;
		}
	}
}