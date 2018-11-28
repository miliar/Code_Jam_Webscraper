#include <cstdio>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

const long double pi = 3.1415926535897932384626433832795;
int T, N, K;

struct Area { 
	int n;
	int r, h;
	long long area;
	Area(int _n, int _r, int _h, long long _a) : n(_n), r(_r), h(_h), area(_a) {}
};

struct Circle : public Area{
	Circle(int _n, int _r, int _h) : Area(_n, _r, _h, (long long)_r*_r) {}
};

struct Side : public Area {
	Side(int _n, int _r, int _h) : Area(_n, _r, _h, (long long)_r*_h * 2) {}
};

inline bool operator==(const Area& lhs, const Area& rhs) {
	return lhs.n == rhs.n;
}
inline bool operator<(const Area& lhs, const Area& rhs) {
	return lhs.area > rhs.area || (lhs.area == rhs.area && lhs.r < rhs.r);
}

vector<Circle> carr;
vector<Side> sarr;

long double GetOptSurf(const multiset<Circle>& cset, const multiset<Side>& sset)
{
	long long maxSurfL = 0;

	multiset<Circle>::const_iterator citb = cset.cbegin();
	multiset<Circle>::const_iterator cite = cset.cend();
	multiset<Circle>::const_iterator cit;
	for (cit = citb; cit != cite; ++cit) {
		int curNum = cit->n;
		multiset<Side>::const_iterator sitb = sset.cbegin();
		multiset<Side>::const_iterator site = sset.cend();
		multiset<Side>::const_iterator sit;
		int remain = K - 1;
		long long curArea = cit->area + Side(0, cit->r, cit->h).area;
		for (sit = sitb; sit != site && remain > 0; ++sit) {
			if (sit->n == curNum) {
				continue;
			}
			if (sit->r > cit->r) {
				continue;
			}
			curArea += sit->area;
			remain--;
		}
		if (remain > 0) {
			continue;
		}
		if (curArea > maxSurfL) {
			maxSurfL = curArea;
		}
	}

	return pi * maxSurfL;
}

int main(void) {
	std::cin >> T;
	for (int tc = 1; tc <= T; tc++) {
		std::cin >> N >> K;
		carr.clear();
		sarr.clear();
		multiset<Circle> cset;
		multiset<Side> sset;
		for (int num = 0; num < N; num++) {
			int R, H;
			std::cin >> R >> H;
			Circle c = Circle(num, R, H);
			Side s = Side(num, R, H);
			carr.push_back(c);
			sarr.push_back(s);
			cset.insert(c);
			sset.insert(s);
		}
		printf("Case #%d: %.15lf\n", tc, GetOptSurf(cset, sset));
	}


	return 0;
}