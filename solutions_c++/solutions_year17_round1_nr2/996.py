#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

inline ull div_ceil(ull n, ull d)
{
    ull r = n / d;
    if (n % d)
	r += 1;
    return r;
}

struct interval
{
    ull l, r;

    interval():
	l(0), r(0)
    {
    }
    
    interval(ull x, ull w)
    {
	l = div_ceil(10 * x, 11 * w);
	r = 10 * x / (9 * w);
    }

    friend bool operator < (const interval & a, const interval & b)
    {
	if (a.l != b.l)
	    return a.l < b.l;
	return a.r < b.r;
    }
};

int main()
{
    int __; cin >> __;
    for (int _ = 0; _ < __; ++_) {
	int n, m; cin >> n >> m;
	vector<ull> w(n);
	vector<vector<interval> > v(n);
	vector<int> p(n, 0);
	for (int i = 0; i < n; ++i)
	    cin >> w[i];
	vector<ull> t;
	for (int i = 0; i < n; ++i) {
	    for (int j = 0; j < m; ++j) {
		ull x; cin >> x;
		interval it = interval(x, w[i]);
		if (it.l <= it.r) {
		    v[i].push_back(it);
		    t.push_back(it.l);
		    t.push_back(it.r);
		}
	    }
	    sort(v[i].begin(), v[i].end());
	    //for (int j = 0; j < v[i].size(); ++j) {
	    //	cout << "[" << v[i][j].l << ", " << v[i][j].r << "]";
	    //}
	    //cout << endl;
	}
	sort(t.begin(), t.end());
	t.erase(unique(t.begin(), t.end()), t.end());
	int ans = 0;
	auto check = [&](int t) {
	    for (int j = 0; j < n; ++j)
		if (p[j] >= v[j].size() || v[j][p[j]].l > t)
		    return false;
		return true;
	};
	for (int i = 0; i < t.size(); ++i) {
	    for (int j = 0; j < n; ++j) {
		while (p[j] < v[j].size() && v[j][p[j]].r < t[i])
		    ++p[j];
	    }
	    while (check(t[i])) {
		ans += 1;
		for (int j = 0; j < n; ++j)
		    ++p[j];
	    }
	}
	cout << "Case #" << (_+1) << ": ";
	cout << ans << endl;
    }
    return 0;
}

// [
