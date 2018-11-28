// GCJ.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>
#include <cmath>
#include <set>

using namespace std;

struct str
{
	long long l, r;

	str() {}

	str(long long _l, long long _r)
	{
		l = _l;
		r = _r;
	}
};

bool operator<(str a, str b)
{
	long long p1 = a.l + (a.r - a.l) / 2;
	long long p2 = b.l + (b.r - b.l) / 2;

	long long l1 = p1 - a.l - 1;
	long long r1 = a.r - p1 - 1;

	long long l2 = p2 - b.l - 1;
	long long r2 = b.r - p2 - 1;

	if (min(l1, r1) > min(l2, r2))
	{
		return true;
	}
	else if (min(l1, r1) < min(l2, r2))
	{
		return false;
	}
	else
	{
		if (max(l1, r1) > max(l2, r2))
		{
			return true;
		}
		else if (max(l1, r1) < max(l2, r2))
		{
			return false;
		}
		else
		{
			return a.l < b.l;
		}
	}
}

int query;

int main()
{
	ofstream cout("small_output.txt");
	ifstream cin("inp.in");

	cin >> query;
	for (int asd = 0; asd < query; ++asd)
	{
		long long n, k, lres = 0, rres = 0;;
		cin >> n >> k;

		set<str> st;
		st.insert(str(0, n + 1));

		for (int i = 0; i < k; ++i)
		{
			str now = *st.begin();
			st.erase(now);
			st.insert(str(now.l, (now.l + now.r) / 2));
			st.insert(str((now.l + now.r) / 2, now.r));

			if (i == k - 1)
			{
				lres = (now.l + now.r) / 2 - now.l - 1;
				rres = now.r - (now.l + now.r) / 2 - 1;
			}
		}

		cout << "Case #" << (asd + 1) << ": ";
		cout << max(lres, rres) << " " << min(rres, lres);
		cout << endl;
	}
    return 0;
}

