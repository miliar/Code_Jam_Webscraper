#include <bits/stdc++.h>
using namespace std;
#if defined(ILIKEGENTOO)
void E(){}template<class A,class...B>void E(A _,B...$){cerr<<' '<<_;E($...);}
#define E($...) E(#$,'=',$,'\n')
#else
#define E($...) ;
#endif
#define all(x) begin(x), end(x)
struct ${$(){ios_base::sync_with_stdio(false);cin.tie(nullptr);}}$;

vector<vector<char>> f;
string letters;
int r, c;

void print() {
	for (const auto &ff: f) {
		for (char fff: ff)
			cout << fff;
		cout << '\n';
	}
}

bool good() {
	for (char ch: letters) {
		int i0 = r, i1 = -1, j0 = c, j1 = -1;
		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				if (f.at(i).at(j) == ch) {
					i0 = min(i0, i);
					i1 = max(i1, i);
					j0 = min(j0, j);
					j1 = max(j1, j);
				}
		assert(i0 <= i1 && j0 <= j1);
		for (int i = i0; i <= i1; ++i)
			for (int j = j0; j <= j1; ++j)
				if (f.at(i).at(j) != ch)
					return false;
	}
	return true;
}

bool rec(int i) {
	while (i < r * c && f.at(i % r).at(i / r) != '?')
		++i;
	if (i == r * c) {
		return good();
	}
	for (char ch: letters) {
		f.at(i % r).at(i / r) = ch;
		if (rec(i + 1)) return true;
	}
	f[i % r][i / r] = '?';
	return false;
}

void solve() {
	cin >> r >> c;
	f.resize(r);
	for (auto &ff: f) {
		ff.resize(c);
		for (auto &fff: ff)
			cin >> fff;
	}
	letters.resize(0);
	for (const auto &ff: f) {
		assert(ff.size() == size_t(c));
		for (char fff: ff)
			if (fff != '?')
				letters.push_back(fff);
	}
	sort(all(letters));
	letters.erase(unique(all(letters)), end(letters));
	E(letters);
	bool ok = rec(0);
	assert(ok);
	print();
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ":\n";
		solve();
	}
	return 0;
}
