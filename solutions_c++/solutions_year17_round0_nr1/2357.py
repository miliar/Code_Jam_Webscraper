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
  for (int t = 0; t < T; t++) {
    string s;
    int k, len, flips = 0;
    bool possible = true;
    cin >> s >> k;
    len = s.size();
    for (int i = 0; i < len; i++) {
      if (s[i] == '-') {
	if (i + k > len) {
	  possible = false;
	  break;
	}
	for (int j = i + 1; j < i + k; j++) {
	  if (s[j] == '-') {
	    s[j] = '+';
	  }
	  else {
	    s[j] = '-';
	  }
	}
	flips++;
      }
      else {
	continue;
      }
    }
    cout << "Case #" << t + 1 << ": ";
    if (possible) {
      cout << flips << endl;
    }
    else {
      cout << "IMPOSSIBLE" << endl;
    }
  }
  return 0;
}
