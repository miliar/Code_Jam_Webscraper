/**
 * @Author:      H S-J
 * @DateTime:    2017-04-08 19:06:32
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
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, kase = 0;
	scanf("%d", &t);
	rep(i, 0, t) {
		string s;
		cin >> s;
		int k;
		cin >> k;
		int num = 0;
		for (int i = 0; i < s.length() - k + 1; ++i) {
			if (s[i] == '-') {
				for (int j = 0; j < k; ++j) {
					s[i + j] = (s[i + j] == '-') ? '+' : '-';  
				}
				++num;
			}
		}
		if (s.find('-') == s.npos)
			printf("Case #%d: %d\n", ++kase, num);
		else 
			printf("Case #%d: IMPOSSIBLE\n", ++kase);
	}
	return 0;
}