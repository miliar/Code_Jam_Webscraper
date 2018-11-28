#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <tuple>
#include <cmath>
#include <cstring>
#include <map>
#include <set>
#include <functional>
#include <experimental/optional>

using namespace std;
using namespace std::experimental;

struct State
{
	const int hd, ad, hk, ak;

	bool operator< (const State &o) const
	{
		return make_tuple(hd, ad, hk, ak) < make_tuple(o.hd, o.ad, o.hk, o.ak);
	}

	State hit() const
	{
		return State({hd - ak, ad, hk, ak});
	}

	State attack() const
	{
		return State({hd, ad, hk - ad, ak}).hit();
	}

	State buff(int b) const
	{
		return State({hd, ad + b, hk, ak}).hit();
	}

	State cure(int o) const
	{
		return State({o, ad, hk, ak}).hit();
	}

	State debuff(int d) const
	{
		return State({hd, ad, hk, max(ak - d, 0)}).hit();
	}
};
ostream &operator<< (ostream &out, const State &s)
{
	return out << "(" << s.hd << ", " << s.ad << ", " << s.hk << ", " << s.ak << ")";
}

optional<int> mingood(optional <int> a, optional <int> b)
{
	if (make_pair(!bool(a), a) < make_pair(!bool(b), b))
		return a;

	return b;
}

optional<int> go(map <State, int> &G, set <State> &V, const State s, const int o, const int b, const int d)
{
	if (s.hk <= 0)
		return 0;

	if (s.hd <= 0)
		return optional<int>();

	if (G.find(s) != G.end())
		return G[s];

	if (V.find(s) != V.end())
		return optional<int>();

	V.insert(s);

	optional<int> m;
	m = mingood(m, go(G, V, s.attack(), o, b, d));
	m = mingood(m, go(G, V, s.cure(o), o, b, d));
	m = mingood(m, go(G, V, s.debuff(d), o, b, d));

	if (s.ad < s.hk)
		m = mingood(m, go(G, V, s.buff(b), o, b, d));


	if (m)
		G[s] = *m + 1;

	return m ? G[s] : m;
}

string solve(int hd, int ad, int hk, int ak, int b, int d)
{
	map <State, int> G;
	set <State> V;
	
	optional <int> r = go(G, V, State({hd, ad, hk, ak}), hd, b, d);
	if (!r)
		return "IMPOSSIBLE";

	return to_string(*r);
}

int main()
{
	int n; cin >> n;
	for (int z = 1; z <= n; z++)
	{
		int hd, ad, hk, ak, b, d;
		cin >> hd >> ad >> hk >> ak >> b >> d;

		printf("Case #%d: %s\n", z, solve(hd, ad, hk, ak, b, d).c_str());
	}

	return 0;
}
