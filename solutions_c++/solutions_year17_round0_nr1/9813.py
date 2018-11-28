// very useful, common imports
#include <iostream>
#include <string>
#include <stdlib.h>
#include <memory>
#include <cassert>
#include <climits>
#include <cctype>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <algorithm>
#include <cmath>
#include <set>

// bost library for printing out complex data structs. useful for debugging
// can be found http://louisdx.github.io/cxx-prettyprint/
#include "../common/prettyprint.h"

#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define mp make_pair
#define pb push_back
#define all(v) v.begin(),v.end()
#define sz size()

using namespace std;

using pii = pair<int, int>;
using vpii = vector<pii>;
using vi = vector<int>;
using vb = vector<bool>;
using vd = vector<double>;
using vii = vector<vector<int> >;

int k;

int recurse(string& data, int index, int flips) {
  //base case
  if (data.find_first_not_of('+') == string::npos) {
    return flips;
  } else {
    // check for imposiblle
    if (k > data.length() - index) {
      return -1;
    }
    // snag num if we don't flip at this ind
    int dont = recurse(data, index + 1, flips);
    // now flip and recurse
    for (int i = index; i < index + k; ++i) {
      data[i] = data[i] == '+' ? '-' : '+';
    }
    int did = recurse(data, index + 1, flips + 1);
    // unflip
    for (int i = index; i < index + k; ++i) {
      data[i] = data[i] == '+' ? '-' : '+';
    }
    if (dont == -1) return did;
    if (did == -1) return dont;
    return min(dont, did);
  }
}

void solve(int case_n)
{
  string line;
  cin >> line >> k;

  int x = recurse(line, 0, 0);

  if (x == -1) {
    cout << "Case #" << case_n << ": IMPOSSIBLE\n";
  } else {
    cout << "Case #" << case_n << ": " << x << "\n";
  }
}

int main()
{
	int N;
	cin >> N;

	for (int i = 0; i < N; ++i) {
		solve(i+1);
	}
}
