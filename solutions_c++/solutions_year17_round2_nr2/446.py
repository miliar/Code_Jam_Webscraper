#include <bits/stdc++.h>
using namespace std;

#pragma GCC diagnostic warning "-Wconversion"

#define pb push_back
#define all(a) begin(a), end(a)
#define has(a, b) (a.find(b) != a.end())
#define fora(i, n) for(int i = 0; i < n; i++)
#define forb(i, n) for(int i = 1; i <= n; i++)
#define forc(a, b) for(const auto &a : b)
#define ford(i, n) for(int i = n; i >= 0; i--)
#define maxval(t) numeric_limits<t>::max()
#define minval(t) numeric_limits<t>::min()

#define dbgs(x) #x << " = " << x
#define dbgs2(x, y) dbgs(x) << ", " << dbgs(y)
#define dbgs3(x, y, z) dbgs2(x, y) << ", " << dbgs(z)
#define dbgs4(w, x, y, z) dbgs3(w, x, y) << ", " << dbgs(z)

typedef long long ll;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	forb(t, T)
	{
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;

		pair<int, char> arr[] = { make_pair(r, 'R'), make_pair(y, 'Y'), make_pair(b, 'B') };
		sort(all(arr), greater<pair<int, char>>());

		if (arr[0].first > arr[1].first + arr[2].first)
		{
			cout << "Case #" << t << ": IMPOSSIBLE" << endl;
			continue;
		}


		queue<char> q, w, e;
		fora(i, arr[0].first)
		{
			q.push(arr[0].second);
		}
		int used1 = 0;
		int used2 = 0;
		fora(i, arr[0].first)
		{
			if (used1 < arr[1].first)
			{
				w.push(arr[1].second);
				++used1;
			}
			else
			{
				w.push(arr[2].second);
				++used2;
			}
		}
		fora(i, arr[2].first - used2)
		{
			e.push(arr[2].second);
		}

		char out[1007];
		out[n] = '\0';

		int i = 0;
		while (!q.empty())
		{
			out[i++] = q.front();
			q.pop();
			out[i++] = w.front();
			w.pop();
			if (!e.empty())
			{
				out[i++] = e.front();
				e.pop();
			}
		}

		cout << "Case #" << t << ": " << out << endl;

	}
}
