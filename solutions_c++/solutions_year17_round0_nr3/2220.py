#include <fstream>
#include <algorithm>
#include <vector>
#include <map>

#define ll long long
using namespace std;

struct Mus 
{ 
	ll lf, rt;

	bool operator<(const Mus &mus2) const
	{
		if (min(lf, rt) != min(mus2.lf, mus2.rt))
			return min(lf, rt) < min(mus2.lf, mus2.rt);

		if (max(lf, rt) != max(mus2.lf, mus2.rt))
			return max(lf, rt) < max(mus2.lf, mus2.rt);
	}

} mus;

ifstream fin("A.in");
ofstream fout("A.out");

ll n, k;
vector<Mus> co;
map<pair<ll, ll>, ll> dex;

Mus NextLf(Mus mus)
{
	Mus nxt;
	nxt.lf = (mus.lf - 1) / 2;
	nxt.rt = mus.lf - nxt.lf - 1;

	return nxt;
}

Mus NextRt(Mus mus)
{
	Mus nxt;
	nxt.lf = (mus.rt - 1) / 2;
	nxt.rt = mus.rt - nxt.lf - 1;

	return nxt;
}

void Push(Mus mus, ll nr)
{
	pair<ll, ll> p = make_pair(mus.lf, mus.rt);

	if (dex.find(p) == dex.end())
	{
		co.push_back(mus);
		push_heap(co.begin(), co.end());
	}
	
	dex[p] += nr;
}

int main()
{
	int t;
	fin >> t;

	for (int i = 1; i <= t; i++)
	{
		fin >> n >> k;

		ll poz = (n + 1) / 2; 
		mus.lf = poz - 1; mus.rt = n - mus.lf - 1;

		co.clear(); dex.clear();
		co.push_back(mus); dex[make_pair(mus.lf, mus.rt)] = 1;

		while(k > 0)
		{
			mus = co.front();
			pop_heap(co.begin(), co.end());
			co.pop_back();

			ll nr = dex[make_pair(mus.lf, mus.rt)];
			if (nr >= k)
				break;
			else
				k -= nr;

			if (mus.lf != 0)
				Push(NextLf(mus), nr);
			if (mus.rt != 0)
				Push(NextRt(mus), nr);
		}

		fout << "Case #" << i << ": " << max(mus.lf, mus.rt) << " " << min(mus.lf, mus.rt) << '\n';
	}

	return 0;
}