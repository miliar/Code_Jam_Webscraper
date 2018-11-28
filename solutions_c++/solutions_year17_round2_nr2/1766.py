#include <bits/stdc++.h>
using namespace std;

#ifdef HELTHAZAR
	#define DEBUG true
#else
	#define DEBUG false
#endif

#define dout if (DEBUG) cout

string oneLetter(map<char, int> mp, char r, char g, int n) {
	if (2 * mp[r] != n || 2 * mp[g] != n) {
		return "IMPOSSIBLE";
	}

	string res = "";
	for (int i = 0; i < mp[r]; i++) {
		res += r;
		res += g;
	}

	return res;
}

string twoLetters(map<char, int> mp, char r, char g, char y, char v) {
	if (mp[g] + 1 > mp[r] || mp[v] + 1 > mp[y] || mp[r] - mp[g] != mp[y] - mp[v]) {
		return "IMPOSSIBLE";
	}

	string res = "";
	res += r;
	for (int i = 0; i < mp[g]; i++) {
		res += g;
		res += r;
	}
	res += y;
	for (int i = 0; i < mp[v]; i++) {
		res += v;
		res += y;
	}

	for (int i = 0; i < mp[r] - mp[g] - 1; i++) {
		res += r;
		res += y;
	}

	return res;
}

string threeLetters(map<char, int> mp, int n) {
	if (mp['G'] + 1 > mp['R'] || mp['V'] + 1 > mp['Y'] || mp['O'] + 1 > mp['B']) {
		return "IMPOSSIBLE";
	}

	map<string, int> mps;
	mps["BR"] = mps["BY"] = mps["RY"] = 0;
	mps["Y"] = mps["R"] = mps["B"] = 0;
	set<pair<int, char> > st;
	if (mp['R'] > mp['G'] +1) {
		st.insert(make_pair(mp['R'] - mp['G'] - 1, 'R'));
	}
	if (mp['B'] > mp['V'] +1) {
		st.insert(make_pair(mp['B'] - mp['V'] - 1, 'B'));
	}
	if (mp['Y'] > mp['O'] + 1) {
		st.insert(make_pair(mp['Y'] - mp['O'] - 1, 'Y'));
	}

	while (st.size() > 1) {
		pair<int, char> p1 = *st.rbegin();
		st.erase(*st.rbegin());
		pair<int, char> p2 = *st.rbegin();
		st.erase(*st.rbegin());

		string res = "";
		res += p1.second;
		res += p2.second;
		if (res[0] > res[1]) {
			swap(res[0], res[1]);
		}
		mps[res]++;

		p1.first--;
		if (p1.first > 0) {
			st.insert(p1);
		}
		p2.first--;
		if (p2.first > 0) {
			st.insert(p2);
		}
	}

	if (st.size() == 1) {
		pair<int, char> p = *st.begin();
		st.erase(*st.begin());

		if (p.first != 1) {
			return "IMPOSSIBLE";
		}
		string res = "";
		res += p.second;
		mps[res]++;
	}

	string res = "";
	res += 'R';
	for (int i = 0; i < mp['G']; i++) {
		res += 'G';
		res += 'R';
	}
	for (int i = 0; i < mps["BR"]; i++) {
		res += 'B';
		res += 'R';
	}
	if (mps["Y"] != 0) {
		res += 'Y';
	}
	res += 'B';
	for (int i = 0; i < mp['O']; i++) {
		res += 'O';
		res += 'B';
	}
	for (int i = 0; i < mps["BY"]; i++) {
		res += 'Y';
		res += 'B';
	}
	if (mps["R"] != 0) {
		res += 'R';
	}
	res += 'Y';
	for (int i = 0; i < mp['V']; i++) {
		res += 'V';
		res += 'Y';
	}
	for (int i = 0; i < mps["RY"]; i++) {
		res += 'R';
		res += 'Y';
	}
	if (mps["B"] != 0) {
		res += 'B';
	}

	return res;
}

void solve() {
	int n, r, o, y, g, b, v;
	cin >> n >> r >> o >> y >> g >> b >> v;

	map<char, int> mp;
	mp['R'] = r;
	mp['O'] = o;
	mp['Y'] = y;
	mp['G'] = g;
	mp['B'] = b;
	mp['V'] = v;

	if (y == 0 && b == 0) {
		cout << oneLetter(mp, 'R', 'G', n);
		return;
	}
	else if (r == 0 && y == 0) {
		cout << oneLetter(mp, 'B', 'O', n);
		return;
	}
	else if (r == 0 && b == 0) {
		cout << oneLetter(mp, 'Y', 'V', n);
		return;
	}

	if (y == 0) {
		cout << twoLetters(mp, 'R', 'G', 'B', 'O');
		return;
	}
	else if (r == 0) {
		cout << twoLetters(mp, 'Y', 'V', 'B', 'O');
		return;
	}
	else if (b == 0) {
		cout << twoLetters(mp, 'Y', 'V', 'R', 'G');
		return;
	}

	cout << threeLetters(mp, n);
}

int main() {
	int test;
	cin >> test;

	for (int t = 1; t <= test; t++) {
		//printf("Case #%d: ", t);
		cout << "Case #" << t << ": ";

		solve();

		cout << endl;
		//printf("\n");
	}
}
