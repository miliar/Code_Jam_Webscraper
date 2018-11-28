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
using vd = vector<double>;
using vii = vector<vector<int> >;


// global map
vector<long long> data;

bool is_tidy(long long n) {
  string str = to_string(n);
  for (int i = 1; i < str.length(); ++i) {
    if (str[i - 1] > str[i]) return false;
  }
  return true;
}

void solve(int case_n)
{
  long long num;
  cin >> num;

  while (!is_tidy(num)){
    // cout << num << "\n";
    num--;
  }

	cout << "Case #" << case_n << ": "  <<  num    << "\n";
}

int main()
{
	int N;
	cin >> N;

	for (int i = 0; i < N; ++i) {
		solve(i+1);
	}
}
