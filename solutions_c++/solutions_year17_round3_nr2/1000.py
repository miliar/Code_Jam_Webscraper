#include <bits\stdc++.h>
#define PI (2 * acos(0))
using namespace std;

struct Interval {
	int L, R;
	int flag;
	int length() {
		return R - L;
	}
	Interval() {
		L = 0, R = 1440, flag = 0;
	}
	Interval(int L, int R) :L(L), R(R) { flag = 0; }
	Interval(int L, int R, int flag) :L(L), R(R), flag(flag) { }
};

bool cmp(Interval a, Interval b) {
	return a.L < b.L;
}

int AC, AJ;
vector<Interval> I;

int solve() {
	int CRemaining = 720, JRemaining = 720;
	sort(I.begin(), I.end(), cmp);

	do {
		int i;
		for (i = 0; i + 1 < I.size(); i++) {
			if (I[i].flag == I[i + 1].flag && I[i].R == I[i + 1].L) {
				I.push_back(Interval(I[i].L, I[i + 1].R, I[i].flag));
				I.erase(I.begin() + i, I.begin() + i + 2);
			}
		}
		sort(I.begin(), I.end(), cmp);
		if (i + 1 >= I.size())
			break;
	} while (true);

	for (int i = 0; i < I.size(); i++) {
		if (I[i].flag == 1) {
			JRemaining -= I[i].length();
		}
		else if (I[i].flag == 2) {
			CRemaining -= I[i].length();
		}
	}

	// Small cases.
	if (I.size() == 1)
		return 2;
	else {
		if (AC == 1 && AJ == 1)
			return 2;

		for (int i = 0; i + 1 < I.size(); i++) {
			if (I[i].flag == I[i + 1].flag) {
				if (I[i].flag == 1 && JRemaining >= I[i + 1].L - I[i].R)
					return 2;
				else if (I[i].flag == 2 && CRemaining >= I[i + 1].L - I[i].R)
					return 2;
			}
		}

		if(I[0].flag == 1 && JRemaining >= I[0].L + 1440 - I[I.size() - 1].R)
			return 2;
		if (I[0].flag == 2 && CRemaining >= I[0].L + 1440 - I[I.size() - 1].R)
			return 2;
		return 4;
	}
}

int main() {
	freopen("B-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t, c = 1;
	cin >> t;
	while (t--) {
		int ans = 0;;
		cin >> AC >> AJ;
		I.clear();
		for (int i = 0; i < AC; i++) {
			int L, R;
			cin >> L >> R;
			I.push_back(Interval(L, R, 1));
			
		}
		for (int i = 0; i < AJ; i++) {
			int L, R;
			cin >> L >> R;
			I.push_back(Interval(L, R, 2));
		}

		
		printf("Case #%d: %d\n", c++, solve());
	}
	return 0;
}