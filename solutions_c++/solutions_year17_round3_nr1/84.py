#include <iostream>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

typedef pair<long long, long long> pii;

const int MAXN = 1010;
const long double PI = M_PI;


pii a[MAXN];
priority_queue<long long> x;

int main()
{
	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++)
	{
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; i++)
			cin >> a[i].first >> a[i].second;
		sort(a, a + n);
		long double ans = 0;
		long long sum = 0;
		while (!x.empty())
			x.pop();
		for (int i = 0; i < n; i++)
		{
			sum += a[i].first * a[i].second;
			if (x.size() > k - 1)
			{
				sum += x.top();
				x.pop();
			}
			if (x.size() == k - 1)
				ans = max(ans, sum * 2 * PI + PI * a[i].first * a[i].first);
			x.push(-(a[i].first * a[i].second));
		}
		cout.precision(10);	
		cout << "Case #" << tt << ": " << fixed << ans << endl;
	}
}
