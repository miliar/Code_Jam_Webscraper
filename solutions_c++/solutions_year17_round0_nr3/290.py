#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define eb emplace_back

typedef long long ll;
typedef pair<ll, ll> pii;

void addSegs(map<ll, pii> &m, ll width, ll nr)
{
	if (width == 0) return;
	if (width % 2 == 0) m[width/2].y += nr;
	else				m[width/2+1].x += nr;
}

bool run(int tc)
{
	ll n, k;
	pii ans;
	map<ll, pii> pq;
	cin >> n >> k;

	pq[(n + 1) / 2] = pii(n % 2 == 1, n % 2 == 0);

	// k: number of things left.
	while (k > 0) {
		ll take = k;
		map<ll, pii>::iterator it = prev(pq.end());
		// cerr << "CURRENT ITEM: " << it->x << ", " << it->y.x << ", " << it->y.y << endl;
		if (it->y.y > 0) {
			take = min(take, it->y.y);
			it->y.y -= take;
			// reduce even
			ans = pii(it->x, it->x - 1);

			addSegs(pq, it->x, take);
			addSegs(pq, it->x - 1, take);
		} else {
			take = min(take, it->y.x);
			it->y.x -= take;
			// reduce odd
			ans = pii(it->x - 1, it->x - 1);

			addSegs(pq, it->x - 1, 2 * take);
		}

		k -= take;
		if (it->y == pii(0, 0)) pq.erase(it);
	}

	cout << "Case #" << tc << ": ";
	cout << ans.x << " " << ans.y;
	cout << endl;
	return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int ntc;
	cin >> ntc;
	for (int i = 1; i <= ntc; i++) {
		if (!run(i)) {
			cerr << "Something went wrong" << endl;
		}
	}
	return 0;
}
