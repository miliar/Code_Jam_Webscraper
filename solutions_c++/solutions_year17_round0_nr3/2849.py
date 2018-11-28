
#define  _CRT_SECURE_NO_WARNINGS

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <queue>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
#include <stdio.h>
#include <complex>
#include <cstdint>
#include <tuple>

#define M_PI       3.14159265358979323846

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) { int v; istringstream sin(s); sin >> v; return v; }
template<class T> inline string toString(T x) { ostringstream sout; sout << x; return sout.str(); }

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef pair<int, PII> TIII;
typedef long long LL;
typedef unsigned long long ULL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;

//container util

//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

#define MOD 1000000007

string filename = "c_large";


int main() {
	freopen((filename + ".txt").c_str(), "r", stdin);
	freopen((filename + "_out.txt").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	REP(t, T) {
		printf("Case #%d: ", t + 1);
		//solve
		LL n, k, d, l[2], s[2], lc[2], sc[2], r;
		REP(i, 2)l[i] = s[i] = lc[i] = sc[i] = 0;
		scanf("%lld%lld", &l[0], &k);
		lc[0] = 1;
		int x = 0;
		while (k) {
			if (l[x] & 1) {//odd
				//large
				l[x ^ 1] = l[x] / 2;
				d = min(k, lc[x]);
				if (d)r = l[x];
				lc[x ^ 1] = d * 2;
				lc[x] -= d;
				k -= d;
				//small
				if (k == 0)break;				
				d = min(k, sc[x]);
				if (d)r = s[x];
				lc[x ^ 1] += d;
				s[x ^ 1] = l[x ^ 1] - 1;
				sc[x ^ 1] = d;
				sc[x] -= d;
				k -= d;
			}
			else {//even
				//large
				l[x ^ 1] = l[x] / 2;
				s[x ^ 1] = l[x ^ 1] - 1;
				d = min(k, lc[x]);
				if (d)r = l[x];
				lc[x ^ 1] = d;
				sc[x ^ 1] = d;
				lc[x] -= d;
				k -= d;
				//small
				if (k == 0)break;
				d = min(k, sc[x]);
				if (d)r = s[x];
				sc[x ^ 1] += d*2;
				sc[x] -= d;
				k -= d;
			}
			x = x^1;
		}
		printf("%lld %lld\n", r/2, r-1-r/2);
	}
	return 0;
}