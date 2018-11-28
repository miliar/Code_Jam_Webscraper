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

void getPossible(vector<int> &ans, vector<int> &possible, int pos) {
  if (pos == 0) {
    possible.push_back(0);
    possible.push_back(1);
    possible.push_back(2);
  }
  else if (pos != ans.size() - 1) {
    int prev = ans[pos - 1];
    if (prev == 0) {
      possible.push_back(1);
      possible.push_back(2);
    }
    else if (prev == 1) {
      possible.push_back(0);
      possible.push_back(2);
    }
    else if (prev == 2) {
      possible.push_back(0);
      possible.push_back(1);
    }
  }
  else {
    set<int> alls;
    alls.insert(0);
    alls.insert(1);
    alls.insert(2);
    int prev = ans[pos - 1];
    alls.erase(prev);
    if (pos != 1 && prev != ans[0]) {
      alls.erase(ans[0]);
    }
    for (int v: alls) {
      possible.push_back(v);
    }
  }
}

void print_vector(vector<int> v) {
  for (int val: v) {
    cout << val << " ";
  }
  cout << endl;
}

int main () {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    int total = n;
    vector<pair<int,int> > arr(3);
    arr[0] = make_pair(r, 0);
    arr[1] = make_pair(y, 1);
    arr[2] = make_pair(b, 2);
    sort(arr.rbegin(), arr.rend());
    vector<int> ans(total, -1);
    bool impossible = false;
    for (int i = 0; i < total; i++) {
      vector<int> possible(0);
      getPossible(ans, possible, i);
      // print_vector(ans);
      int maxval = 0, bit = 0;
      for (int j = 0; j < 3; j++) {
	for (int i = 0; i < possible.size(); i++) {
	  if (arr[j].second == possible[i]) {
	    if (arr[j].first > maxval) {
	      maxval = arr[j].first;
	      bit = possible[i];
	    }
	  }
	}
      }
      if (!maxval) {
	impossible = true;
	break;
      }
      for (int i = 0; i < 3; i++) {
	if (arr[i].second == bit) {
	  arr[i].first--;
	  break;
	}
      }
      ans[i] = bit;
    }
    cout << "Case #" << t << ": ";
    if (impossible) {
      cout << "IMPOSSIBLE" << endl;
    }
    else {
      for (int i = 0; i < total; i++) {
	if (ans[i] == 0) {
	  cout << 'R';
	}
	else if (ans[i] == 1) {
	  cout << 'Y';
	}
	else {
	  cout << 'B';
	}
      }
      cout << endl;
    }
  }
  return 0;
}
