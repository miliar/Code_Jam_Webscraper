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

string problemName = "B";
string smallFileName = problemName + "-small-attempt0";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
//string fileName = smallFileName;
string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

string solve(string s) {
  bool original = true;
  REP (i, sz(s)-1) {
    if (s[i] > s[i+1]) original = false;
  }
  if (original) return s;
  for (int i = sz(s) - 1; i >= 0; --i) if (s[i] != '0') {
      bool bad = false;
      REP (j, i) {
	if (s[j] > s[j+1] - (j + 1 == i)) {
	  bad = true;
	  break;
	}
      }
      if (!bad) {
	s[i]--;
	FOR (j, i+1, sz(s)) {
	  s[j] = '9';
	}
	if (i == 0 && s[i] == '0')
	  s.erase(s.begin());
	return s;
      }
  }
}

string naive(string s) {
  istringstream str(s);
  int x;
  str>>x;
  for (int i = x; i >= 1; --i) {
    ostringstream str2;
    str2<<i;
    string s = str2.str();
    bool bad = false;
    REP (j, sz(s)-1)
      if (s[j] > s[j+1])
	bad = true;
    if (!bad)
      return s;
  }
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
	string s;
	cin >> s;
	cout << solve(s) << endl;
	// if (solve(s) == naive(s))
	//   return 1;
    }
    return 0;
}
