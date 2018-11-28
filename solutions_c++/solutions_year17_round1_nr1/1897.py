
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

string filename = "a_large";

char board[33][33];
void dfs(int xs, int xe, int ys, int ye) {
	char f0[256];
	memset(f0, 0, sizeof(f0));
	int sum = 0;
	FOR(i, ys, ye)FOR(j, xs, xe)f0[board[i][j]]=1;
	FOR(i, 'A', 'Z' + 1)sum += f0[i];
	if (sum == 1) {
		char c = 0;
		FOR(i, 'A', 'Z' + 1)if(f0[i])c=i;
		FOR(j, xs, xe)FOR(i, ys, ye)board[i][j] = c;
		return;
	}
	

	FOR(i, xs+1, xe) {//x
		char f1[256];
		char f2[256];
		memset(f1, 0, sizeof(f1));
		memset(f2, 0, sizeof(f2));
		//Area L
		FOR(j, xs, i) FOR(k, ys, ye)if (board[k][j] != '?')f1[board[k][j]] = 1;
		//Area R
		FOR(j, i, xe) FOR(k, ys, ye)if (board[k][j] != '?')f2[board[k][j]] = 1;
		int sum1 = 0, sum2 = 0, sum12 = 0;
		FOR(j, 'A', 'Z' + 1) sum12 += f1[j] * f2[j];
		FOR(j, 'A', 'Z' + 1) sum1 += f1[j];
		FOR(j, 'A', 'Z' + 1) sum2 += f2[j];
		if (sum12 == 0 && sum1 != 0 && sum2 != 0) {//OK
			dfs(xs, i, ys, ye);
			dfs(i, xe, ys, ye);
			return;
		}
	}
	FOR(i, ys + 1, ye) {//y
		char f1[256];
		char f2[256];
		memset(f1, 0, sizeof(f1));
		memset(f2, 0, sizeof(f2));
		//Area L
		FOR(j, xs, xe) FOR(k, ys, i)if (board[k][j] != '?')f1[board[k][j]] = 1;
		//Area R
		FOR(j, xs, xe) FOR(k, i, ye)if (board[k][j] != '?')f2[board[k][j]] = 1;
		int sum1 = 0, sum2 = 0, sum12 = 0;
		FOR(j, 'A', 'Z' + 1) sum12 += f1[j] * f2[j];
		FOR(j, 'A', 'Z' + 1) sum1 += f1[j];
		FOR(j, 'A', 'Z' + 1) sum2 += f2[j];
		if (sum12 == 0 && sum1 != 0 && sum2 != 0) {//OK
			dfs(xs, xe, ys, i);
			dfs(xs, xe, i, ye);
			return;
		}
	}
}

int main() {
	freopen((filename + ".txt").c_str(), "r", stdin);
	freopen((filename + "_out.txt").c_str(), "w", stdout);
	int T;
	scanf("%d", &T);
	REP(t, T) {
		printf("Case #%d: ", t + 1);
		memset(board, 0, sizeof(board));
		//solve
		int r, c;
		scanf("%d%d", &r, &c);
		REP(i, r)scanf("%s", board[i]);
		dfs(0, c, 0, r);
		printf("\n");
		REP(i, r)printf("%s\n", board[i]);
		
	}
	return 0;
}