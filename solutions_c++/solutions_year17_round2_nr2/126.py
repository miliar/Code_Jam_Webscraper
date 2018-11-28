#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define eb emplace_back

typedef long long ll;
typedef pair<int, int> pii;

bool impossible(int tc)
{
	cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
	return true;
}

char colch[6] = { 'R', 'O', 'Y', 'G', 'B', 'V' };

int fromcolch(char ch)
{
	if (ch == 'R') return 0;
	if (ch == 'O') return 1;
	if (ch == 'Y') return 2;
	if (ch == 'G') return 3;
	if (ch == 'B') return 4;
	if (ch == 'V') return 5;
	cerr << "NOT KNOWN: " << ch << " " << ((int) ch);
	assert(false);
	return -1;
}

bool allowed[6][6] = {
	{ 0, 0, 1, 1, 1, 0 },
	{ 0, 0, 0, 0, 1, 0 },
	{ 1, 0, 0, 0, 1, 1 },
	{ 1, 0, 0, 0, 0, 0 },
	{ 1, 1, 1, 0, 0, 0 },
	{ 0, 0, 1, 0, 0, 0 }
};

bool validstr(string s)
{
	int n = s.size();
	for (int i = 0, j = n - 1; i < n; j = i++) {
		int c1 = fromcolch(s[i]), c2 = fromcolch(s[j]);
		if (!allowed[c1][c2]) {
			return false;
		}
	}
	return true;
}

bool giveanswer(int tc, const stringstream &ss)
{
	string ans = ss.str();
	if (!validstr(ans)) {
		cerr << tc << " is wrong: " << ans << endl;
		return false;
	}
	cout << "Case #" << tc << ": " << ans << endl;
	return true;
}

string solveSimple(int col[6], bool &possible)
{
	int N = col[0] + col[2] + col[4];
	possible = !(2 * col[0] > N || 2 * col[2] > N || 2 * col[4] > N);
	if (!possible) return "";

	pii byF[3];
	for (int i = 0; i < 3; i++) byF[i] = pii(col[2*i], 2*i);
	sort(byF, byF + 3, greater<pii>());
	
	stringstream ss;
	for (int i = 0; i < byF[0].x; i++) {
		ss << colch[byF[0].y];
		if (i < byF[1].x) ss << colch[byF[1].y];
		if (byF[0].x - i <= byF[2].x) ss << colch[byF[2].y];
	}
	return ss.str();
}

int COL[6], COL2[6];

bool run(int tc)
{
	int N;
	cin >> N;
	for (int i = 0; i < 6; i++) cin >> COL[i];

	stringstream ans;
	for (int i = 0; i < 3; i++) {
		int i1 = 2 * i + 1, i2 = (i1 + 3) % 6;
		int c1 = COL[i1], c2 = COL[i2];

		if (c1 > 0 && c1 == c2) {
			if (c1 + c2 != N) return impossible(tc);
			// ABAB ... AB
			for (int j = 0; j < c1; j++)
				ans << colch[i1] << colch[i2];
			return giveanswer(tc, ans);
		}
		if (c1 > c2) return impossible(tc);
		// after this loop, c1 < c2
	}

	for (int i = 0; i < 6; i += 2) {
		COL2[i] = COL[i] - COL[(i + 3) % 6]; // >= 0
	}

	bool possible;
	string tans = solveSimple(COL2, possible);
	if (!possible) return impossible(tc);

	for (char ch : tans) {
		ans << ch;
		if (ch == 'R' && COL[3] > 0) { while (COL[3]--) ans << "GR"; }
		if (ch == 'Y' && COL[5] > 0) { while (COL[5]--) ans << "VY"; }
		if (ch == 'B' && COL[1] > 0) { while (COL[1]--) ans << "OB"; }
	}
	return giveanswer(tc, ans);
	// cout << "Case #" << tc << ": " << ans.str() << endl;
	// return true;
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int ntc;
	cin >> ntc;
	for (int i = 1; i <= ntc; i++) {
		if (!run(i)) {
			cerr << "Something went wrong" << endl;
		}
	}
	return 0;
}
