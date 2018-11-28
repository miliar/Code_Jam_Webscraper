#include <string>
#include <vector>
#include <cstring>
#include <cmath>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <list>
#include <iomanip>
#include <ctime>
#include <cassert>
#include <stack>
#include <unordered_map>
#include <unordered_set>

#define what_is(x) cout << #x << " is " << x << endl;

using namespace std;

typedef long long ll;

int main () {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int ac, aj;
    int ans = 2;
    cin >> ac >> aj;
    vector<pair<int,int> > t1, t2;
    t1.resize(ac);
    t2.resize(aj);
    for (int i = 0; i < ac; i++) {
      cin >> t1[i].first >> t1[i].second;
    }
    for (int i = 0; i < aj; i++) {
      cin >> t2[i].first >> t2[i].second;
    }
    if (ac == 2 && aj == 0) {
      sort(t1.begin(), t1.end());
      if (t1[1].second - t1[0].first <= 720) {
	ans = 2;
      }
      else{
	t1[0].second += 720*2;
	if (t1[0].second - t1[1].first <= 720) {
	  ans = 2;
	}
	else {
	  ans = 4;
	}
      }
    }
    else if (ac == 0 && aj == 2) {
      sort(t2.begin(), t2.end());
      if (t2[1].second - t2[0].first <= 720) {
	ans = 2;
      }
      else{
	t2[0].second += 720*2;
	if (t2[0].second - t2[1].first <= 720) {
	  ans = 2;
	}
	else {
	  ans = 4;
	}
      }
    }
    cout << "Case #" << t << ": " << ans << endl; 
  }
  return 0;
}
