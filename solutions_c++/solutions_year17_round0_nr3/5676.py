#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<ll, ll> P;
typedef pair<P, P> PP;
#define mp make_pair
ll n, k, x, y, z, res, t, pos, l;
PP p, g, h;
priority_queue<PP>q;
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	cin >> t;
	for (int u = 1; u <= t;u++)
	{
		while (!q.empty())q.pop();

		cin >> n >> k;
		pos = 0;
		l = n;
		p.first = mp((l - 1) / 2, (l - 1) / 2 + (l - 1) % 2);
		p.second = mp(-1, -n);
		q.push(p);
		while (!q.empty())
		{
			p = q.top();
			q.pop();
			pos++;
			//cout << -p.second.first << " " << -p.second.second << endl;
			if (pos == k)
			{
				cout << "Case #" << u << ": " << p.first.second << " " << p.first.first << "\n";
				break;
			}
			x = -p.second.first;
			y = -p.second.second;
			z = (x + y) / 2;
			l = z - x;
			g.first = mp((l-1)/2,(l-1)/2 + (l-1)%2);
			g.second = mp(-x, -z + 1);

			l = y - z;
			h.first = mp((l - 1) / 2, (l - 1) / 2 + (l - 1) % 2);
			h.second = mp(-z - 1, -y);

			q.push(g);
			q.push(h);
		}
	}
	return 0;
}