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

string dirname = "../../GCJ/2017Qual/";
string filename = "a_large";

char buf[1111];

int main() {
	freopen((dirname + filename + ".txt").c_str(), "r", stdin);
	freopen((dirname + filename + "_out.txt").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	REP(t, T) {
		printf("Case #%d: ", t+1);
		int k,n,ans = 0;
		scanf("%s", buf);
		scanf("%d", &k);
		n = strlen(buf);
		REP(i, n - k + 1) {
			if (buf[i] == '-') {
				REP(j, k) buf[i + j] = (buf[i + j] == '+') ? '-' : '+';
				ans++;
			}
		}
		FOR(i, n - k, n)if (buf[i] == '-')ans = -1;
		if (ans < 0)printf("Impossible\n");
		else printf("%d\n", ans);
	}
	return 0;
}