#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = (sizeof(ll) == 8) ? 1e18 : 1e9;

string ans;

void _case(ll cas)
{
	cout << "Case #" << cas << ": ";
}

bool cmp(pair <ll, char> &a, pair <ll, char> &b)
{
	if (a.first == b.first)
	{
		if (ans[0] == a.second)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
	return a.first > b.first;
}

void sol(ll cas)
{
	ll n, r, o, y, g, b, v, p;
	cin >> n >> r >> o >> y >> g >> b >> v;
	ll q = r + y + b;
	_case(cas);
	if ((q - r < r) || (q - y < y) || (q - b < b))
	{
		cout << "IMPOSSIBLE" << endl;
		return;
	}
	vector <pair <ll, char>> arr = { {r, 'r' }, {b, 'b' }, {y, 'y' } };
	sort(arr.rbegin(), arr.rend());
	ans = "";
	ans += arr[0].second;
	arr[0].first--;
	for (int i = 1; i < n; i++)
	{
		sort(arr.begin(), arr.end(), cmp);
		p = -1;
		for (int j = 0; j < 3; j++)
		{
			if (ans.back() != arr[j].second)
			{
				p = j;
				break;
			}
		}
		ans += arr[p].second;
		arr[p].first--;
	}
	for (int i = 0; i < n; i++)
	{
		ans[i] -= ('a' - 'A');
	}
	cout << ans << endl;
}

int main()
{
	srand(time(0));
	ios::sync_with_stdio(0);
#ifdef _F1A4X_
	//ifstream cin("input.txt");
	//ofstream cout("output.txt");
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	ll t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		sol(i + 1);
	}
#ifdef _F1A4X_
	cerr << endl << "\t" << clock() << " ms" << endl;
#endif
}