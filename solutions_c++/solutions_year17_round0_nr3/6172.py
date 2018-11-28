#include <iostream>
#include <queue>
#include <utility>

using namespace std;

class Compare {
public:

	bool operator() (const pair<long, long> &a, const pair<long, long> &b) const {
		long al = a.second - a.first;
		long bl = b.second - b.first;

		if (al < bl)
			return true;
		if (al > bl)
			return false;

		if (a.first > b.first)
			return true;
		if (a.first < b.first)
			return false;

		cerr << "compared equal pairs" << endl;
		return true;
	}

};

void solve(int num) {
	priority_queue <pair<long, long>, vector<pair<long, long> >, Compare> p;

	long n, k;

	long ls, rs;

	cin >> n >> k;

	bool occ [n+2];
	occ[0] = true;
	occ[n+1] = true;

	p.push(pair<long, long> (1, n));

	for (long i=0; i<k; i++) {
		pair<long, long> it = p.top();
		p.pop();

		long stall = (it.first + it.second) / 2;

		occ[stall] = true;

		if (it.first <= stall-1)
			p.push(pair<long, long> (it.first, stall-1));
		if (stall+1  <= it.second)
			p.push(pair<long, long> (stall+1,  it.second));

		ls = stall - it.first;
		rs = it.second - stall;
	}

	if (ls > rs) {
		long temp = ls;
		ls = rs;
		rs = temp;
	}

	cout << "Case #" << num << ": " << rs << " " << ls << endl;
}

int main () {
	int N;
	cin >> N;

	for (int i=0; i<N; i++)
		solve(i+1);

	return 0;
}