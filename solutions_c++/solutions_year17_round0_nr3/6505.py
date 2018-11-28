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

struct St
{
	int r;
	int l;
	int len;

	St(int l, int r)
	{
		this->l = l;
		this->r = r;
		this->len = (r - l);
	}

	bool operator < (const St &st) const
	{
		if (len == st.len)
		{
			return l > st.l;
		}
		return (len < st.len);
	}
};

signed main()
{
	int T;
	cin >> T;

	for (int t = 0; t < T; t++)
	{
		int N, K;
		cin >> N >> K;
		priority_queue<St> q;
		q.push(St(0, N - 1));
		for (int k = 0; k < K; k++)
		{
			St st = q.top();
			q.pop();

			int s = (st.r - st.l) / 2 + st.l;

			if (k == K - 1)
			{
				int ls = s - st.l;
				int rs = st.r - s;
				int min = MIN(ls, rs);
				int max = MAX(ls, rs);
				cout << "Case #" << (t + 1) << ": " << max << " " << min << endl;
				break;
			}

			if ((s - 1) - st.l >= 0)
			{
				q.push(St(st.l, s - 1));
			}
			if (st.r - (s + 1) >= 0)
			{
				q.push(St(s + 1, st.r));
			}
		}
	}
}
