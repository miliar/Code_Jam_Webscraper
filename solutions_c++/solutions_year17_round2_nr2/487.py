/*
 * GCJ 2017 round 1B
 * Task: B. Stable Neigh-bors
 */
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <bitset>
using namespace std;

#define FOR(i,n) for (int i = 0; i < n; i++)
#define abs(x) ((x)<0?(-(x)):(x))
#define REP(i,v) for (unsigned i = 0; i < v.size(); i++)
#define RL(i,v) for (unsigned i = 0; i < v.length(); i++)
typedef long long ll;

const int INF = 999666111;
const int MAXN = 1001;

const string IMPOSSIBRU = "IMPOSSIBLE";
int n, r, o, y, g, b, v;
int m;

int MAXR, MAXY, MAXB;

char temp[MAXN];
string found;

enum Colour {
	Red,
	Yellow,
	Blue,
	Any
};

Colour charToEnum(char c)
{
	switch (c) {
		case 'R': return Red;
		case 'Y': return Yellow;
		case 'B': return Blue;
		default:
			return Any;
	}
}

vector<unsigned char> seen;

bool recu(Colour first, Colour last, int r, int y, int b)
{
	int i = m - r - y - b;
	
	if (i == m) {
		temp[i] = 0;
		found = temp;
		return true;
	}
	bool ret = false;
	
	int key = b * MAXY * MAXR * 16;
	key += y * MAXR * 16;
	key += r * 16;
	key += first * 4;
	key += last;
	if (seen[key]) return false;
	seen[key] = 1;
	
	if (r > 0 && last != Red && (i < m - 1 || first != Red)) {
		temp[i] = 'R';
		ret |= recu(first != Any ? first : Red, Red, r - 1, y, b);
	}
	if (!ret && y > 0 && last != Yellow && (i < m - 1 || first != Yellow)) {
		temp[i] = 'Y';
		ret = recu(first != Any ? first : Yellow, Yellow, r, y - 1, b);
	}
	if (!ret && b > 0 && last != Blue && (i < m - 1 || first != Blue)) {
		temp[i] = 'B';
		ret = recu(first != Any ? first : Blue, Blue, r, y, b - 1);
	}
	return ret;
}

string cornerCase(int c1, int c2, string rep)
{
	if (c1 != c2) return IMPOSSIBRU;
	string answer;
	FOR(i, c1) answer += rep;
	return answer;
}

string solve()
{
	scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &g, &b, &v);
	// o = r + y; can sit only with blues
	// g = y + b; can sit only with reds
	// v = r + b; can sit only with yellows
	
	// check for the "YVYV"-type corner cases:
	if (r + y + g + v == 0) return cornerCase(o, b, "OB");
	if (o + y + b + v == 0) return cornerCase(g, r, "GR");
	if (r + o + g + b == 0) return cornerCase(v, y, "VY");
	
	string answer;
	if (o) {
		while (o--) {
			answer += "BO";
			b--;
		}
		answer += "B";
		b--;
		if (b < 0) return IMPOSSIBRU;
	}

	if (g) {
		while (g--) {
			answer += "RG";
			r--;
		}
		answer += "R";
		r--;
		if (r < 0) return IMPOSSIBRU;
	}

	if (v) {
		while (v--) {
			answer += "YV";
			y--;
		}
		answer += "Y";
		y--;
		if (y < 0) return IMPOSSIBRU;
	}
	
	m = n - int(answer.length());
	MAXR = r + 1;
	MAXY = y + 1;
	MAXB = b + 1;
	Colour last = Any, first = Any;
	if (!answer.empty()) {
		first = charToEnum(answer[0]);
		last = charToEnum(answer[answer.length() - 1]);
	}

	seen.clear();
	seen.resize(MAXR * MAXY * MAXB * 16);
	if (recu(first, last, r, y, b)) {
		return answer + found;
	} else {
		return IMPOSSIBRU;
	}
}

int main(void)
{
	//freopen("/home/vesko/gcj/B.in", "rt", stdin);
	int T;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++) {
		//printf("Case #%d: %%d\n", tc, solve());
		cout << "Case #" << tc << ": " << solve() << endl;
	}
	return 0;
}
