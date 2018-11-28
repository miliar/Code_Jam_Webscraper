#include <iostream>
#include <cmath>
#include <set>
using namespace std;

typedef signed long long longf;
typedef unsigned long long ulongf;

struct Interval {
	ulongf start, end, duration;

	Interval(ulongf start, ulongf end) {
		this->start = start;
		this->end = end;
		getDuration();
	}


	int getDuration() {
		return duration = end - start + 1;
	}

	ulongf ls, rs;

	void calc() {
		if (duration & 1) {  // odd
			ls = rs = (duration >> 1);
		} else {  // even
			ls = (duration >> 1) - 1;
			rs = (duration >> 1);
		}
	}
};

struct Less {
 	bool operator() (const Interval &a, const Interval &b) {
 		if (a.duration == b.duration)
 			return (a.start < b.start);
 		return a.duration > b.duration;
 	}
};

int t;

int main() {
	cin >> t;

	for (int tt = 1; tt <= t; ++tt) {
		ulongf n, k;
		cin >> n >> k;
		cout << "Case #" << tt << ": ";

		if (k >= n) {
			cout << "0 0" << endl;
			continue;
		}

		set<Interval, Less> m;
		m.insert(Interval(1, n));

		for (int kk = 1; kk < k; ++kk) {
			auto it = m.begin();
			auto i = *it;

			m.erase(it);
			int mid = i.start + ((i.duration + 1) >> 1) - 1;
			if (i.start <= mid - 1)
				m.insert(Interval(i.start, mid - 1));
			if (mid + 1 <= i.end)
				m.insert(Interval(mid + 1, i.end));
		}

		if (m.empty()) cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
		// for (auto &i : m) cout << i.start << " - " << i.end << endl;

		auto i = *m.begin();
		i.calc();
		cout << i.rs << " " << i.ls << endl;
	}

	return 1;
}