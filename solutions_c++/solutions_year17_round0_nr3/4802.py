#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <cmath>
#include <stack>
#include <queue>
#include <exception>
#include <numeric>
#include <algorithm> 
#include <sstream>
#include <cstring>
#include <deque>
using namespace std;
 
typedef long long lo;
typedef vector< vector<long long> > vvl;
typedef vector< long long> vl;
typedef pair<lo, lo> ll;
typedef vector< pair<lo, lo> > vll;
typedef vector< vll > vvll;
typedef pair<long, pair<long, long> > lll;
typedef vector<lll> vlll;
typedef vector<vvl> vvvl;
typedef vector<set<lo> > vs;
typedef map<lo, map<lo, lo> > mm;

#define N 1000

// apparently every new person divides the available set in two parts that have the highest possible sizes each. after the first division, the solution can be explored for each set separately. Apparently it is optimal to start with the biggest interval each time. On each iteration the processed interval gets its length decremented and separated in two intervals, of their sizes being determined by the half of the original interval, and the second one by the decremented length minus the length of the first interval.
// probably the optimal solution is to apply the lazy computaton and the map for the solution function.
// f(n, k) = max(n/2) is the next optimal size of the interval after the/ decrement of the original function. 

void solve(lo caseNum)  {
	lo n, k;
	cin >> n >> k;
	
	map<lo, lo> s;
	s[n]++;
	for (lo i=0;i<k-1;i++){
		lo last=s.rbegin()->first;
		s[last]--;
		if (s[last]==0) s.erase(last);
		last--;
		s[last/2]++;
		s[last - last/2]++;
	}
	lo last=s.rbegin()->first;
	last--;
	lo mn = last/2, mx= last - last/2;
	
	cout << "Case #" << caseNum << ": " << mx << " " << mn <<"\n";
}

int main() {
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
	lo t;
	cin >> t;
	for (lo i=0;i<t;i++)
		solve(i+1);
	return 0;
}