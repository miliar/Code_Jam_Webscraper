/*
Hanit Banga
*/

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define fast_cin() ios_base::sync_with_stdio(false)

typedef long long ll;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;

const int N = 1e5 + 5;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		int n, p;
		cin >> n >> p;
		int ctr[p] = {0};
		for (int i = 0; i < n; ++i)
		{
			int x;
			cin >> x;
			ctr[x % p]++;
		}

		int ans = ctr[0];
		if (p == 2)
		{
			ans += (ctr[1] + 1) / 2;
		}

		else if (p == 3)
		{
			int temp = min(ctr[1], ctr[2]);
			ans += temp;
			ctr[1] -= temp;
			ctr[2] -= temp;
			ans += (ctr[1] / 3) + (ctr[2] / 3);
			ctr[1] %= 3;
			ctr[2] %= 3;
			if (ctr[1] or ctr[2])
				++ans;
		}

		else if (p == 4)
		{
			ans += (ctr[2] / 2);
			ctr[2] %= 2;
			int temp = min(ctr[1], ctr[3]);
			ans += temp;
			ctr[1] -= temp;
			ctr[3] -= temp;
			if (ctr[2] and ctr[1] > 1)
			{
				++ans;
				--ctr[2];
				ctr[1] -= 2;
			}

			ans += (ctr[1] / 4) + (ctr[3] / 4);
			ctr[1] %= 4;
			ctr[3] %= 4;
			if (ctr[1] or ctr[2] or ctr[3])
				++ans;
		}

		cout << ans << endl;
	}	
}