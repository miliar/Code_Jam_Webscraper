#include <map>
#include <set>
#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long lint;
#define pp(a,b) push_back(make_pair((a),(b)))
#define pb push_back
#define mp make_pair
#define buybuy {printf("-1\n");return 0;}

int next() {int x; cin >> x; return x;}
lint lnext() {lint x; cin >> x; return x;}
//template<typename T> outln(T x) {cout << x; cout << "\n";}
#define prt(a) cout << a << "\n";
#define prtn(a, n) for(int iiiiiiiiiii = 0; iiiiiiiiiii < n; iiiiiiiiiii++) cout << a[iiiiiiiiiii] << " "; cout << "\n;"
#define prtall(a) for (auto iiiiiiiiiii : a) cout << iiiiiiiiiii << " "; cout << "\n";

int main() {

	int tests = next();
	for (int test = 1; test <= tests; test++) {
		//cout << test << endl;

		int n = next();
		int p = next();

		vector<int> c(4, 0);
		for (int i = 0; i < n; i++) c[next() % p]++;
		
		//cout << n << " " << p << endl;
		//prtall(c)
		//cout << endl;
		
		vector<vector<vector<vector<int>>>> mx(c[1] + 1, vector<vector<vector<int>>>(c[2] + 1, vector<vector<int>>(c[3] + 1, vector<int>(p, -1000))));
		mx[c[1]][c[2]][c[3]][0] = 0;
		for (int i = c[1]; i >= 0; i--)
			for (int j = c[2]; j >= 0; j--)
				for (int k = c[3]; k >= 0; k--)
					for (int t = 0; t < p; t++) {
						int s = (t + 1) % p;
						if (i > 0) mx[i - 1][j][k][s] = max(mx[i - 1][j][k][s], mx[i][j][k][t] + !t);
						s++; if (s == p) s = 0;
						if (j > 0) mx[i][j - 1][k][s] = max(mx[i][j - 1][k][s], mx[i][j][k][t] + !t);
						s++; if (s == p) s = 0;
						if (k > 0) mx[i][j][k - 1][s] = max(mx[i][j][k - 1][s], mx[i][j][k][t] + !t);
					}
					
		int answ = -1;
		for (int i = 0; i < p; i++) answ = max(answ, mx[0][0][0][i]);

		//prtall(mx[0][0][0])
		
		printf("Case #%d: %d\n", test, answ + c[0]);
	}
}