#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>

using namespace std;

#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'
#define rep(i,a)      for(int i=0;i<a;i++)
#define rep2(i,a,b)      for(int i=a;i<b;i++)
using namespace std;
int test = 1;
bool happy[1000];
int n_pancakes = 0;

int solve(int tool_size) {
  int flip = 0;

  // linear swipe.
  rep(i, n_pancakes) {
    if (happy[i])
      continue;

    // Check feasibility.
    if (n_pancakes - i < tool_size)
      return -1;

    // Flip tool_size pancakes: makes I happy ;-)
    ++flip;
    rep(j, tool_size) happy[i + j] = !happy[i + j];
  }

  return flip;
}

void parse() {
  cout << "Case #" << test++ << ": ";

  string line, sizeS;

  getline(cin, line);
  int n = line.length();
  n_pancakes = 0;
  for (int i = 0; i < n; i++) {
    if (line[i] == '+' || line[i] == '-') {
      ++n_pancakes;
      happy[i] = line[i] == '+' ? true : false;
    } else if (line[i] == ' ')
      continue;
    else
      sizeS += line[i];
  }
  int tool_size = atoi(sizeS.c_str());

  int res = solve(tool_size);
  if (res == -1)
    cout << "IMPOSSIBLE" << endl;
  else
    cout << res << endl;
}

signed main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  int t = 1;
  cin >> t;

  // Skip the number of testcases line.
  string s;
  getline(cin, s);

  while (t--) {
    parse();
  }
  return 0;
}
