#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <cstdio>
#include <map>
#include <unordered_map>
#include <string>
#include <iomanip>
#include <vector>
#include <memory.h>
#include <queue>
#include <set>
#include <unordered_set>
#include <stack> 
#include <algorithm>
#include <math.h>
#include <sstream>
#include <functional>
#include <bitset>
using namespace std;
#define mems(A, val) memset(A, val, sizeof(A))
#define mp(a, b) make_pair(a, b)
#define all(B) (B).begin(), (B).end()
#define forn(it, from, to) for(int it = from; it < to; ++it)
#define forit (it, coll) for(auto it = coll.begin(); it != coll.end(); ++it)
#define sz(a) (int)a.size()
#define pb push_back
const int MAXN = 2 * 1000 * 100 + 10;
const double EPS = 1e-9;
typedef long long LL;
const LL MOD = 1000 * 1000 * 1000 + 7;



int main(int argc, char* argv[]) {

#ifdef _DEBUG
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
	//freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	//freopen("data.in", "r", stdin); freopen("data.out", "w", stdout);
#endif
	ios::sync_with_stdio(0);
	cin.tie();

	int ttt;
	cin >> ttt;
	forn(tt, 0, ttt) {
		int n;
		cin >> n;
		int tmp;

		int r, y, b, o, g, v;
		cin >> r >> o >> y >> g >> b >> v;

		// R - G
		if (o == 0 && y == 0 && b == 0 && v == 0) {
			if (r != g) {
				cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}
			else {
				cout << "Case #" << tt + 1 << ": ";
				for (int i = 0; i < g; ++i) {
					cout << "GR";
				}
				cout << endl;
				continue;
			}
		}

		// O - B
		if (r == 0 && y == 0 && g == 0 && v == 0) {
			if (b != o) {
				cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}
			else {
				cout << "Case #" << tt + 1 << ": ";
				for (int i = 0; i < o; ++i) {
					cout << "BO";
				}
				cout << endl;
				continue;
			}
		}

		// Y - V
		if (r == 0 && o == 0 && g == 0 && b == 0) {
			if (y != v) {
				cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}
			else {
				cout << "Case #" << tt + 1 << ": ";
				for (int i = 0; i < v; ++i) {
					cout << "YV";
				}
				cout << endl;
				continue;
			}
		}

		string grstr = "R";
		if (g > 0) {
			if (r < g + 1) {
				cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}

			r -= (g);
			for (int i = 0; i < g; ++i) {
				grstr += "GR";
			}
		}


		string yvstr = "Y";
		if (v > 0) {
			if (y < v + 1) {
				cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}

			y -= (v);
			for (int i = 0; i < v; ++i) {
				yvstr += "VY";
			}
		}


		string bostr = "B";

		if (o > 0) {
			if (b < o + 1) {
				cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
				continue;
			}

			b -= (o);
			for (int i = 0; i < o; ++i) {
				bostr += "OB";
			}
		}


		if (r < 0 || b < 0 || y < 0) {
			cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
			continue;
		}

		n = r + b + y;

		vector<pair<int, char> > a;
		a.push_back(mp(r, 'R'));
		a.push_back(mp(y, 'Y'));
		a.push_back(mp(b, 'B'));

		sort(a.rbegin(), a.rend());

		if (a[0].first > n / 2) {
			cout << "Case #" << tt + 1 << ": IMPOSSIBLE" << endl;
			continue;
		}

		int ptr = 0;
		vector<char> ans(n);
		for (int i = 0; i < a[0].first; ++i) {
			ans[ptr] = a[0].second;
			ptr += 2;
		}

		ptr -= 2;
		ptr += n;
		ptr %= n;
		ptr++;
		ptr %= n;

		for (int i = 0; i < a[1].first; ++i) {
			if (ans[ptr] == 0) {
				ans[ptr] = a[1].second;
				ptr += 2;
				ptr %= n;
			}
			else {
				while (ans[ptr] != 0) {
					ptr++;
					ptr %= n;
				}

				ans[ptr] = a[1].second;
			}
		}

		ptr -= 2;
		ptr += n;
		ptr %= n;
		ptr++;
		ptr %= n;

		for (int i = 0; i < a[2].first; ++i) {
			if (ans[ptr] == 0) {
				ans[ptr] = a[2].second;
				ptr += 2;
				ptr %= n;
			}
			else {
				while (ans[ptr] != 0) {
					ptr++;
					ptr %= n;
				}

				ans[ptr] = a[2].second;
			}
		}

		forn(i, 0, n) {
			if (ans[i] == ans[(i + 1) % n]) {
				i = i;
			}
		}

		cout << "Case #" << tt + 1 << ": ";
		for (int i = 0; i < ans.size(); ++i) {
			if (ans[i] == 'R')
			{
				cout << grstr;
				grstr = "R";
			}
			if (ans[i] == 'B')
			{
				cout << bostr;
				bostr = "B";
			}
			if (ans[i] == 'Y')
			{
				cout << yvstr;
				yvstr = "Y";
			}

		}
		cout << endl;
	}


	return 0;
}