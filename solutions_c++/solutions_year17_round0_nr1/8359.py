#include <iostream>
#include <string>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>
#include <cstring>
#include <cmath>
#include <stack>
#define int long long
#define uint unsigned long long
#define CONTAINS(v,n) (find((v).begin(), (v).end(), (n)) != (v).end())
#define SORT(v) sort((v).begin(), (v).end())
#define RSORT(v) sort((v).rbegin(), (v).rend())
#define ARY_SORT(a, size) sort((a), (a)+(size))
#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))
using namespace std;

int memo[1024];
int LEN;
int S;

int flip(int a, int n)
{
	int r = a;
	for (int i = n; i < n + S; i++)
	{
		r ^= (1LL << i);
	}
	return r;
}

//void func(int a, int cnt)
//{
	//if (memo[a] >= 0)
	//{
	//	return;
	//}
	//memo[a] = cnt;

	//for (int i = 0; i <= LEN - S; i++)
	//{
	//	int r = flip(a, i);
	//	func(r, cnt + 1);
	//}
//}

signed main()
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		memset(memo, -1, sizeof(memo));
		string str;
		cin >> str >> S;
		int a = 0;
		LEN = str.length();
		for (int i = 0; i < str.length(); i++)
		{
			if (str.at(i) == '+')
			{
				a += (1LL << i);
			}
		}

		memo[a] = 0;
		int cnt = 0;
		queue<int> q;
		q.push(a);
		while (q.size() > 0)
		{
			cnt++;

			int qcnt = q.size();
			for (int k = 0; k < qcnt; k++)
			{
				int b = q.front();
				q.pop();

				for (int i = 0; i <= LEN - S; i++)
				{
					int r = flip(b, i);
					if (memo[r] < 0)
					{
						memo[r] = cnt;
						q.push(r);
					}
				}
			}
		}

		int all = (1 << LEN) - 1;
		if (memo[all] >= 0)
		{
			cout << "Case #" << (i + 1) << ": " << memo[all] << endl;
		}
		else
		{
			cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << endl;
		}
	}
}
