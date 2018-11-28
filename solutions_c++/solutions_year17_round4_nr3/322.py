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
string smallFileName = problemName + "-small-attempt1";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
string fileName = smallFileName;
//string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

bool can[55][1<<5][1<<5][1<<5];
string how[55][1<<5][1<<5][1<<5];
int from1[55][1<<5][1<<5][1<<5], from2[55][1<<5][1<<5][1<<5], from3[55][1<<5][1<<5][1<<5];

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
	int n, m;
	cin >> n >> m;
	vector<string> a(n);
	REP (i, n) {
	  cin >> a[i];	  
	}
	memset(can, 0, sizeof(can));
	can[0][0][0][0] = true;
	REP (j, m) {
	  REP (left, 1<<n)
	    REP (portal, 1<<n)
	    REP (should, 1<<n)
	    if (can[j][left][portal][should]) {
	    REP (hor, 1<<n) {
	      string s(n, ' ');
	      REP (y, n) {
		if (a[y][j] == '.' || a[y][j] == '#') {
		  s[y] = a[y][j];
		  continue;
		}
		if (hor & (1<<y)) s[y] = '-'; else s[y] = '|';
	      }
	      bool ok = true;
	      int next_left = 0;
	      int next_portal = 0;
	      int next_should = 0;
	      REP (i, n) {
		if (s[i] == '#') {
		  if (should & (1<<i)) {
		    ok = false;
		    break;
		  }
		  continue;
		}
		bool cov_vert = false;
		for (int y = i-1; y >= 0 && (s[y] == '|' || s[y] == '.'); --y) {
		  if (s[y] == '|') {
		    cov_vert = true;
		    break;
		  }
		}
		for (int y = i+1; y < n && (s[y] == '|' || s[y] == '.'); ++y) {
		  if (s[y] == '|') {
		    cov_vert = true;
		    break;
		  }
		}
		bool cov_hor = (left & (1<<i)) ? true : false;
		if (s[i] == '.') {
		  if (cov_hor) next_left |= 1<<i;
		  if (portal & (1<<i)) next_portal |= 1<<i;
		  if ((should & (1<<i)) || (!cov_hor && !cov_vert)) next_should |= 1<<i;
		  continue;
		}
		if (s[i] == '|' || s[i] == '-') {
		  if (cov_hor || cov_vert) {
		    ok = false;
		    break;
		  }
		  if (s[i] == '-' && (portal & (1<<i))) {
		    ok = false;
		    break;
		  }
		  if (s[i] == '-') next_left |= 1<<i;
		  if (s[i] == '|') next_portal |= 1<<i;
		  if (s[i] == '|' && (should & (1<<i))) {
		    ok = false;
		    break;
		  }
		  continue;
		}
	      }
	      if (ok) {
		can[j+1][next_left][next_portal][next_should] = true;
		how[j+1][next_left][next_portal][next_should] = s;
		from1[j+1][next_left][next_portal][next_should] = left;
		from2[j+1][next_left][next_portal][next_should] = portal;
		from3[j+1][next_left][next_portal][next_should] = should;
	      }
	    }	    
	  }
	}
	int mask1 = -1, mask2 = -1, mask3 = 0;
	REP (i, 1<<n) REP (j, 1<<n) {
	  if (can[m][i][j][0]) mask1 = i, mask2 = j;
	}
	if (mask1 == -1) {
	  cout << "IMPOSSIBLE" << endl;
	  continue;
	}
	cout << "POSSIBLE" << endl;
	int j = m;
	vector<string> b = a;
	while (j) {
	  REP (i, n)
	    b[i][j-1] = how[j][mask1][mask2][mask3][i];
	  int tmask1 = from1[j][mask1][mask2][mask3];
	  int tmask2 = from2[j][mask1][mask2][mask3];
	  int tmask3 = from3[j][mask1][mask2][mask3];
	  mask1 = tmask1;
	  mask2 = tmask2;
	  mask3 = tmask3;
	  j--;
	}
	REP (i, n)
	  cout << b[i] << endl;
    }
    return 0;
}
