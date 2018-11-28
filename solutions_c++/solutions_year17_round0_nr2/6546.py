/**
 * @Author:      H S-J
 * @DateTime:    2017-04-08 20:56:02
 * @Description: 
 */
#include <functional>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <numeric>
#include <cstring>
#include <cassert>
#include <cstdio>
#include <string>
#include <vector>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <ctime>
#include <list>
#include <set>
#include <map>
using namespace std;
#define MST(a, b) memset(a, b, sizeof(a));
#define CLR(a) MST(a, 0);
#define DBG(x) cout << '#' << " = " << (x) << endl;
#define ALL(x) x.begin(), x.end()
#define INS(x) inserter(x, x.begin())
#define lson(x) (x) << 1
#define rson(x) (x) << 1|1
#define pb push_back
#define rep(x, y, z) for (int x = y; x < z; ++x)
#define ech(x, y, z) for (auto x = z.begin(), y = z.end(); x != y; ++x)
#define eout(x) cout << *(x) << " "
#define eout2(x) cout << *(x)
#define eout3(x) cout << *(x) << endl
#define lowbit(x) (x & (-x))
#define opr operator
#define _st first
#define _nd second
#define prior_q1(x) priority_queue<x>
#define prior_q2(x) priority_queue<x, vector<x>, greater<x> >
typedef long long LL;
typedef vector<int> v_i;
typedef vector<LL> v_l;
typedef vector<string> v_s;
typedef map<int, int> mi_i;
typedef map<LL, LL> ml_l;
typedef map<string, int> ms_i;
typedef map<string, LL> ms_l;
typedef set<int> s_i;
typedef set<LL> s_l;
typedef set<string> s_s;
typedef set<double> s_d;
typedef stringstream strstm;
int main(int argc, char const *argv[]) {
	// ios::sync_with_stdio(0);cin.tie(0);
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t, kase = 0;
	cin >> t;
	rep(i, 0, t) {
		string s;
		cin >> s;
		for (int i = s.length() - 1; i > 0; --i) {
			if (s[i] < s[i - 1]) {
				s[i] = '9';
				--s[i - 1];
				for (int j = i + 1; j < s.length(); ++j)
					if (s[j] < s[i]) s[j] = '9';
			}
		}
		strstm ss(s);
		LL ans = 0;
		ss >> ans;
		printf("Case #%d: %lld\n", ++kase, ans);
	}
	return 0;
}