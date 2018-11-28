#include <bits/stdc++.h>

using namespace std;

struct Segment
{
	int l, r;
	Segment(int _l = 0, int _r = 0)
	{
		l = _l;
		r = _r;
	}
	bool operator < (const Segment &s) const
	{
		if ((r - l + 1) != (s.r - s.l + 1))
			return (r - l + 1) > (s.r - s.l + 1);
		if (l != s.l)
			return l < s.l;
		return r < s.r;
	}
};

int t, mx, mn;

int main()
{
	cin >> t;
	for (int tt = 1; tt <= t; tt++)
	{
		int n, k;
		cin >> n >> k;
		set<Segment> st;
		st.insert(Segment(1, n));
		for (int i = 1; i <= k; i++)
		{
			if (st.empty())
				break;
			Segment s = *(st.begin());
			int mid = (s.l + s.r) / 2;
			st.erase(s);
			if (mid - 1 >= s.l)
				st.insert(Segment(s.l, mid - 1));
			if (s.r >= mid + 1)
				st.insert(Segment(mid + 1, s.r));
			mn = mid - s.l;
			mx = s.r - mid;
		}
		cout << "Case #" << tt << ": " << mx << " " << mn << endl;
	}
	return 0;
}