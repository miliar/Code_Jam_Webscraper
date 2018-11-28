#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;

const double pi = 3.1415926535897932384; 



struct pancake {
	int r;
	int h;
	double area1;
	double area2;
	double total;
	int idx;
	pancake(int a1, int a2, double a3, double a4, double a5, int a6) {
		r = a1;
		h = a2;
		area1 = a3;
		area2 = a4;
		total = a5;
		idx = a6;
	}
};

const double eps = 1e-9;

bool comp(pancake p1, pancake p2)
{
	if (abs(p1.total - p2.total) < eps) return p1.r > p2.r;
	return p1.total > p2.total;
}

bool comp2(pancake p1, pancake p2)
{
	if (abs(p1.area2 - p2.area2) < eps) return p1.r > p2.r;
	return p1.area2 > p2.area2;
}

bool comp3(pancake p1, pancake p2)
{
	if (p1.r == p2.r) return p1.h > p2.h;
	return p1.r > p2.r;
}

void solve()
{
	int n, k;
	cin >> n >> k;
	vector<pancake> v;
	for(int i = 0; i < n; i++) {
		int r, h;
		cin >> r >> h;
		double area1 = pi * r * r;
		double area2 = 2.0 * pi * r * h;
		double total = area1 + area2;
		v.push_back(pancake(r, h, area1, area2, total, i));
	}

	if (k == 1) {
		sort(v.begin(), v.end(), comp);
		printf("%.9f", v[0].total);
		return;
	}

	sort(v.begin(), v.end(), comp2);
	double mx = 0;
	double res = 0, res2 = 0;
	set<int> st;
	for(int i = 0; i < k; i++) {
		res += v[i].area2;
		if (i < k - 1)
			res2 += v[i].area2, st.insert(v[i].idx);
		mx = max(mx, v[i].area1);
		
	}

	res += mx;

	sort(v.begin(), v.end(), comp3);
	for(int i = 0; i < k; i++) {
		if (st.count(v[i].idx) == 0) {
			res2 += v[i].total;
			break;
		}
	}

	printf("%.9f", max(res, res2));


}


int main()
{
	freopen("small.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}

	return 0;
}
