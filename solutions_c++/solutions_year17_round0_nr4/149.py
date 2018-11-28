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

string stringify(const vector<vector<char>> &f) {
	string res = "\n";
	for (const auto &vec: f) {
		for (char c: vec)
			res.push_back(int(c)[".+xo"]);
		res.push_back('\n');
	}
	return res;
}

void solve() {
	string s;
	int n, m;
	cin >> n >> m;
	vector<vector<char>> f(n, vector<char>(n));
	vector<char> usedR(n), usedC(n);
	vector<int> usedD(2 * n - 1), usedT(2 * n - 1);
	for (int i = 0; i < m; ++i) {
		int r, c;
		cin >> s >> r >> c;
		--r;
		--c;
		if (s == "+") {
			f[r][c] |= 1;
			usedD[r + c] = true;
			usedT[r - c + n - 1] = true;
		} else if (s == "x") {
			f[r][c] |= 2;
			usedR[r] = true;
			usedC[c] = true;
		} else if (s == "o") {
			// 'o' is just '+' and 'x' at the same place
			f[r][c] |= 3;
			usedR[r] = true;
			usedC[c] = true;
			usedD[r + c] = true;
			usedT[r - c + n - 1] = true;
		} else {
			assert(!"bad sign");
		}
	}
	auto old = f;
	// place 'x' one per row/column
	int ir = 0, ic = 0;
	while (true) {
		for (; ir < n && usedR[ir]; ++ir);
		for (; ic < n && usedC[ic]; ++ic);
		if (ir >= n || ic >= n) break;
		f[ir][ic] |= 2;
		usedR[ir] = true;
		usedC[ic] = true;
	}
	// place 'x' one per diagonal starting with the ones that have less free cells
	// O(n^3) time can easily be improved using sets
	while (true) {
		int v = 2 * n, ind = -1;
		for (int i = 0; i < 2 * n - 1; ++i) if (!usedD[i]) {
			int l = min(i, 2 * n - 2 - i);
			int cur = l + 1;
			for (int j = n - 1 - l; j <= n - 1 + l; j += 2)
				cur -= usedT[j];
			if (cur <= 0) {
				usedD[i] = true;
				continue;
			}
			if (cur <= v) {
				v = cur;
				ind = i;
			}
		}
		if (ind < 0) break;
		assert(!usedD[ind]);
		v = 2 * n;
		int li = min(ind, 2 * n - 2 - ind), jnd = -1;
		for (int i = n - 1 - li; i <= n - 1 + li; i += 2) if (!usedT[i]) {
			int l = min(i, 2 * n - 2 - i);
			int cur = l + 1;
			for (int j = n - 1 - l; j <= n - 1 + l; j += 2)
				cur -= usedD[j];
			assert(cur > 0);
			if (cur <= v) {
				v = cur;
				jnd = i;
			}
		}
		assert(jnd >= 0);
		assert(!usedT[jnd]);
		jnd -= n - 1;
		assert((ind + jnd) % 2 == 0);
		ir = (ind + jnd) / 2;
		ic = (ind - jnd) / 2;
		assert(0 <= ir && ir < n && 0 <= ic && ic < n);
		assert((f[ir][ic] & 1) == 0);
		f[ir][ic] |= 1;
		usedD[ir + ic] = true;
		usedT[ir - ic + n - 1] = true;
	}
	int score = 0;
	vector<pair<int, int>> ans;
	for (int i = 0; i < n; ++i) for (int j = 0; j < n; ++j) {
		if (f[i][j] & 1) ++score;
		if (f[i][j] & 2) ++score;
		if (f[i][j] != old[i][j])
			ans.emplace_back(i, j);
	}
	cout << score << ' ' << ans.size() << '\n';
	for (const auto &ij: ans) {
		int i, j;
		tie(i, j) = ij;
		cout << int(f[i][j])[".+xo"] << ' ' << (i + 1) << ' ' << (j + 1) << '\n';
	}
	return;
	E(stringify(old));
	E(stringify(f));
}

int main() {
	int tc;
	cin >> tc;
	for (int ti = 1; ti <= tc; ++ti) {
		cout << "Case #" << ti << ": ";
		solve();
	}
	return 0;
}
