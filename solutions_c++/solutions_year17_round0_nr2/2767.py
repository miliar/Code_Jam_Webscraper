
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

string filename = "b_large";

char buf[22];

int main() {
	freopen((filename + ".txt").c_str(), "r", stdin);
	freopen((filename + "_out.txt").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	REP(t, T) {
		printf("Case #%d: ", t + 1);
		//solve
		scanf("%s", buf);
		int n = strlen(buf);
		int k = -1;
		REP(i, n - 1) {
			if (buf[i] > buf[i + 1]) {
				k = i;
				buf[k]--;
				break;
			}
		}
		if (k != -1) {
			FOR(i, k+1, n)buf[i] = '9';
			while (k) {
				if (buf[k] < buf[k - 1]) {
					buf[k] = '9';
					buf[k - 1]--;
				}
				else break;
				k--;
			}
		}
		printf("%lld\n", atoll(buf));
	}
	return 0;
}