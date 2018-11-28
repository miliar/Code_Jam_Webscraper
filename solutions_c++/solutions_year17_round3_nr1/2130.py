#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <tuple>
#include <map>
#include <set>
#include <functional>
#include <queue>
#include <tuple>

long long INF = 1000000000000000005LL;
long long MOD = 1000000007;
#define ll long long
#define FOR(a,b,c) for (int (a)=(b);(a)<(c);++(a))
#define FORD(a,b,c) for (int (a)=(b);(a)>(c);--(a))

using namespace std;
int n, k;
vector<tuple<int, int, int>> p;
vector<int> s;
map<int, pair<int, int>> mp;

double pi = 3.1415926535897932384626;

void read() {
	p.clear();
	s.clear();
	mp.clear();
	cin >> n >> k;
	FOR(i, 0, n) {
		int r, h;
		cin >> r >> h;
		p.push_back(make_tuple(r, h, i));
		s.push_back(i);
		mp[i] = make_pair(r, h);
	}
}

struct c1
{
	inline bool operator() (const tuple<int, int, int>& struct1, const tuple<int, int, int>& struct2)
	{
		return (get<0>(struct1) * get<0>(struct1) * pi  + 2*pi * get<0>(struct1) * get<1>(struct1) >
			get<0>(struct2) * get<0>(struct2) * pi + 2 * pi * get<0>(struct2) * get<1>(struct2));
	}
};

struct c2
{
	inline bool operator() (const tuple<int, int, int>& struct1, const tuple<int, int, int>& struct2)
	{
		return ( 2 * pi * get<0>(struct1) * get<1>(struct1) > 2 * pi * get<0>(struct2) * get<1>(struct2));
	}
};

void solve(int test) {
	cout << "Case #" << test + 1 << ": ";
	ll ans = 0;
	sort(p.begin(), p.end(), c1());

	double h = 2 * pi*get<1>(p[0])*get<0>(p[0]);
	double r = get<0>(p[0]);
	int f = get<2>(p[0]);
	int total = 1;
	int l = 0;

	sort(p.begin(), p.end(), c2());
	while (total < k) {
		if (get<2>(p[l]) != f) {
			h += 2 * pi*get<1>(p[l])*get<0>(p[l]);
			r = max(r, (double)get<0>(p[l]));
			total++;
		}
		l++;
	}

	printf("%.10f\n", r*r*pi + h);
}

void solve_stupid(int test) {
	cout << "Case #" << test + 1 << ": ";
	
	double m = -1;
	std::sort(s.begin(), s.end());
	do {
		double h = 0;
		double r = -1;
		FOR(l, 0, k) {
			h += 2 * pi*(double)mp[s[l]].first*(double)mp[s[l]].second;
			r = max(r, (double)mp[s[l]].first);
		}
		m = max(m, r*r*pi + h);
	} while (std::next_permutation(s.begin(), s.end()));

	printf("%.10f\n", m);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int testCount;
	cin >> testCount;

	for (int test = 0; test < testCount; test++) {
		read();
		solve_stupid(test);
	}

	return 0;
}