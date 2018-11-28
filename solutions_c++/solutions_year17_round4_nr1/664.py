#include <cstring>
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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define all(a) (a).begin(),(a).end()
#define UN(a) sort(all(a)),(a).resize(unique(all(a))-(a).begin())
#define sz(a) ((int) (a).size())
#define pb push_back
#define CL(a,b) memset ((a), (b), sizeof (a))
#define X first
#define Y second

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long ll;

string problemName = "A";
string smallFileName = problemName + "-small-attempt0";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
//string fileName = smallFileName;
string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

int d[102][102][102][102][4];

void mm (int& x, int y) {
  x = max(x, y);
}

int main () {
    freopen(inputFileName.data(), "r", stdin);
    if (fileName == smallFileName || fileName == largeFileName)
    {
	freopen(outputFileName.data(), "w", stdout);
    }
    int T;
    cin >> T;
    REP (test, T) {
	cout << "Case #" << (test + 1) << ": ";
	int n, p;
	cin >> n >> p;
	vector<int> a(4);
	REP (i, n) {
	  int x;
	  cin >> x;
	  a[x%p]++;
	}
	memset(d, -1, sizeof(d));
	d[0][0][0][0][0] = 0;
	REP (p0, a[0]+1) REP (p1, a[1]+1) REP (p2, a[2]+1) REP(p3, a[3]+1) REP (f, p)
	  if (d[p0][p1][p2][p3][f] != -1) {
	    int v = d[p0][p1][p2][p3][f] + (f == 0);
	    mm(d[p0 + 1][p1][p2][p3][(f + 0) % p], v);
	    mm(d[p0][p1 + 1][p2][p3][(f + 1) % p], v);
	    mm(d[p0][p1][p2 + 1][p3][(f + 2) % p], v);
	    mm(d[p0][p1][p2][p3 + 1][(f + 3) % p], v);
	  }
	int r = 0;
	REP (i, p)
	  r = max(r, d[a[0]][a[1]][a[2]][a[3]][i]);
	cout << r << endl;
    }
    return 0;
}
