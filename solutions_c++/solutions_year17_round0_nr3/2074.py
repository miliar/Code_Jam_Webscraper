#include <iostream>
#include <vector>

#define ll long long
using namespace std;

ll N, K;
vector< pair<ll, ll> > A;

inline void init()
{
	cin >> N >> K;
	A.clear();
	A.push_back(make_pair(N, 1LL));
}

inline void add(pair<ll, ll> pp)
{
	pair <ll, ll> p = pp;
	if (p.first == A.back().first)
	{
		p.second += A.back().second;
		A.pop_back();
		A.push_back(p);
	}
	else
		A.push_back(p);
}

inline pair<ll, ll> split(ll numm)
{
	ll num = numm;

	num--;
	if (num % 2)
		return make_pair(num / 2 + 1, num / 2);
	return make_pair(num / 2, num / 2);
}

inline pair<ll, ll> solve()
{
	int i = 0;
	pair<ll, ll> p;

	while (K)
	{
		if (A[i].second >= K)
			return split(A[i].first);
		K -= A[i].second;
		p = split(A[i].first);
		add(make_pair(p.first, A[i].second));
		add(make_pair(p.second, A[i].second));
		i++;
	}

	return p;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);

	int T, i;

	cin >> T;

	pair<ll, ll> ans;

	for (i = 1; i <= T; i++)
	{
		init();
		ans = solve();

		cout << "Case #" << i << ": " << ans.first << " " << ans.second << "\n";
	}

	return 0;
}