#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define all(a) begin(a), end(a)
#define has(a, b) (a.find(b) != a.end())
#define fora(i, n) for(int i = 0; i < n; i++)
#define forb(i, n) for(int i = 1; i <= n; i++)
#define forc(a, b) for(const auto &a : b)
#define ford(i, n) for(int i = n; i >= 0; i--)

#define dbgs(x) #x << " = " << x
#define dbgs2(x, y) dbgs(x) << ", " << dbgs(y)
#define dbgs3(x, y, z) dbgs2(x, y) << ", " << dbgs(z)
#define dbgs4(w, x, y, z) dbgs3(w, x, y) << ", " << dbgs(z)

typedef long long ll;

void add(priority_queue<ll> &range, map<ll, ll> &num, ll elem, ll cnt)
{
	if (has(num, elem))
	{
		num[elem] += cnt;
	}
	else
	{
		range.push(elem);
		num[elem] = cnt;
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	forb(t, T)
	{
		priority_queue<ll> range;
		map<ll, ll> num;

		ll n, k;
		cin >> n >> k;

		range.push(n);
		num[n] = 1;

		while (k > num[range.top()])
		{
			ll top = range.top();
			ll cnt = num[top];

			range.pop();
			num.erase(num.find(top));

			ll last1 = top / 2;
			ll last2 = top / 2 - 1 + (top % 2);

			add(range, num, last1, cnt);
			add(range, num, last2, cnt);

			k -= cnt;
		}

		ll top = range.top();

		cout << "Case #" << t << ": "
			<< (top / 2) << " " << (top / 2 - 1 + (top % 2)) << endl;
	}
}
