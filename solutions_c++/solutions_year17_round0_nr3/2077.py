#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>

using namespace std;

const int MAXN = 1000010;

struct Point {
	long long len;
	long long cnt;
	Point(int _len = 0, int _cnt = 0) {
		len = _len;
		cnt = _cnt;
	}
	friend bool operator < (const Point &a, const Point &b) {
		if (a.len != b.len)
			return a.len < b.len;
		return a.cnt < b.cnt;
	}
};

priority_queue<long long> lens;
map<long long, long long> cnt;
long long n, k;

void solve() {
/*	while (!q.empty())
		q.pop();
	cin >> n >> k;
	q.push(Point(n, 1));
	int ls = 0, rs = 0;
	for (int i = 1; i <= k; ++i) {
		int len = q.top().len;
		int idx = q.top().idx;
		q.pop();
		if (len == 1) {
			ls = rs = 0;
			continue;
		}
		if (len % 2 == 0) {
			ls = (len / 2) - 1;
			rs = (len / 2);
		}
		else {
			ls = (len / 2);
			rs = (len / 2);
		}
		if (ls > 0)
			q.push(Point(ls, idx));
		q.push(Point(rs, idx + ls + 1));
	}
	cout << max(ls, rs) << " " << min(ls, rs);*/
	cnt.clear();
	cin >> n >> k;
	long long cur = 0;
	cnt[n] = 1;
	lens.push(n);
	long long ls = 0, rs = 0;
	while (cur < k) {
		long long len = lens.top();
		lens.pop();
		long long cur_cnt = cnt[len];
		cur += cur_cnt;
		cnt.erase(len);
		if (len % 2 == 0) {
			ls = (len / 2) - 1;
			rs = (len / 2);
		}
		else {
			ls = (len / 2);
			rs = (len / 2);
		}
		if (ls > 0) {
			if (cnt.find(ls) == cnt.end())
				lens.push(ls);
			cnt[ls] += cur_cnt;
		}
		if (cnt.find(rs) == cnt.end())
			lens.push(rs);
		cnt[rs] += cur_cnt;
	}
	cout << max(ls, rs) << " " << min(ls, rs);
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl;
	}
	fclose(stdin);
	fclose(stdout);
}
