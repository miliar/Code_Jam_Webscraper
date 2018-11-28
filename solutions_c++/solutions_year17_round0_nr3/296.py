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
string smallFileName1 = problemName + "-small-1-attempt0";
string smallFileName2 = problemName + "-small-2-attempt0";
string largeFileName = problemName + "-large";

//string fileName(1, tolower(problemName[0]));
//string fileName = smallFileName1;
//string fileName = smallFileName2;
string fileName = largeFileName;

string inputFileName = fileName + ".in";
string outputFileName = fileName + ".out";

int main () {
    freopen(inputFileName.data(), "r", stdin);
    if (fileName == smallFileName1 || fileName == smallFileName2 || fileName == largeFileName)
    {
	freopen(outputFileName.data(), "w", stdout);
    }
    int T;
    cin >> T;
    REP (test, T) {
	ll n, k;
	cin >> n >> k;
	n++;
	map<ll, ll> p;
	p[n] = 1;
	long long ans = -1;
	while (true) {
	  auto it = p.end();
	  --it;
	  if (it->Y >= k) {
	    ans = it->X;
	    break;
	  }
	  k -= it->Y;
	  if (it->X > 1) {
	    p[it->X / 2] += it->Y;
	    p[it->X - it->X / 2] += it->Y;
	  }
	  p.erase(it);
	  if (ans != -1) break;
	}
	cout << "Case #" << (test + 1) << ": ";
	cout << (ans - ans/2 - 1) << ' ' << (ans/2 - 1) << endl;
    }
    return 0;
}
