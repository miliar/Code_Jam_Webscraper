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

string problemName = "C";
string smallFileName = problemName + "-small-attempt0";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
//string fileName = smallFileName;
string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

int s[128], v[128];
ll a[128][128];
double t[128];
bool vis[128];

int main () {
    freopen(inputFileName.data(), "r", stdin);
    if (fileName == smallFileName || fileName == largeFileName)
    {
	freopen(outputFileName.data(), "w", stdout);
    }
    int T;
    cin >> T;
    int n, q;
    REP (test, T) {
	cout << "Case #" << (test + 1) << ": ";
	cin >> n >> q;
	REP (i, n) {
	  cin >> s[i] >> v[i];
	}
	REP (i, n) {
	  REP (j, n) {
	    cin >> a[i][j];
	  }
	}
	REP (k, n) {
	  REP (i, n) {
	    REP (j, n) {
	      if (a[i][k] != -1 && a[k][j] != -1 && (a[i][j] == -1 || a[i][j] > a[i][k] + a[k][j])) {
		a[i][j] = a[i][k] + a[k][j];
	      }
	    }
	  }
	}
	REP (qq, q) {
	  int x, y;
	  cin >> x >> y;
	  --x, --y;
	  REP (i, n) {
	    t[i] = 1e40;
	    vis[i] = false;
	  }
	  t[x] = 0;
	  REP (i, n) {
	    int k = -1;
	    REP (j, n) {
	      if (t[j] < 1e39 && !vis[j] && (k == -1 || t[k] > t[j])) {
		k = j;
	      }
	    }
	    if (k == -1) break;
	    vis[k] = true;
	    REP (j, n) if (a[k][j] != -1 && a[k][j] <= s[k]) {
	      t[j] = min(t[j], t[k] + (double) a[k][j] / v[k]); 
	    }
	  }
	  if (qq) cout << ' ';
	  printf("%.9lf", t[y]);
	}
	cout << endl;
    }
    return 0;
}
