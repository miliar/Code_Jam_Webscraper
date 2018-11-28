#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

const ll INF = (sizeof(ll) == 8) ? 1e18 : 1e9;

string s;
bool can;
ll ret;

void rep(char &c)
{
	if (c == '+')
	{
		c = '-';
	}
	else
	{
		c = '+';
	}
}

void sol(ll k)
{
	ll ans = 0, p;
	set <ll> st;
	while (1)
	{
		p = -1;
		for (int i = s.size(); i >= 0; i--)
		{
			if (s[i] == '-')
			{
				p = i;
				break;
			}
		}
		if (p == -1)
		{
			ret = ans;
			can = 1;
			break;
		}
		p = max(p, k - 1);
		if (st.find(p) != st.end())
		{
			can = 0;
			break;
		}
		for (int i = p; i >= p + 1 - k; i--)
		{
			rep(s[i]);
		}
		st.insert(p);
		ans++;
	}
}

int main()
{
	srand(time(0));
	ios::sync_with_stdio(0);
#ifdef _F1A4X_
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
	ll t, k;
	cin >> t;
	for (int cas = 1; cas <= t; cas++)
	{
		cin >> s >> k;
		cout << "Case #" << cas << ": ";
		sol(k);
		if (can)
		{
			cout << ret << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}