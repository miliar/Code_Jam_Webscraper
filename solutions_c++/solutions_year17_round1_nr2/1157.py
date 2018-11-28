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

int N, P;
vector<int> serving, inds;
vector<vector< vector<int> > > alls;

void get_servings(int val, int one, vector<int> &servings) {
  int v1 = (val / one) * one;
  int v2 = v1 + one;
  for (int v = v1; (10 * val <= 11 * v) && (v / one > 0); v = v - one) {
    servings.push_back(v/one);
  }
  for (int v = v2; 10 * val >= 9 * v; v = v + one) {
    servings.push_back(v/one);
  }
  sort(servings.begin(), servings.end());
}

int main () {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    cin >> N >> P;
    serving.clear();
    serving.resize(N);
    inds.clear();
    inds.resize(N, 0);
    alls.clear();
    alls.resize(N, vector< vector<int> >());
    for (int i = 0; i < N; i++) {
      cin >> serving[i];
    }
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < P; j++) {
	int cur;
	cin >> cur;
	vector<int> servings(0);
	get_servings(cur, serving[i], servings);
	if (servings.size()) {
	  alls[i].push_back(servings);
	}
      }
    }
    for (int i = 0; i < N; i++) {
      sort(alls[i].begin(), alls[i].end(),
          [](const std::vector<int>& a, const std::vector<int>& b)
	   {return a < b;});
      /*
      for (int j = 0; j < alls[i].size(); j++) {
	cout << "(";
	for (int k = 0; k < alls[i][j].size(); k++) {
	  cout << alls[i][j][k] << ",";
	}
	cout << ") ";
      }
      cout << endl;*/
    }
    int ans = 0, curv1 = 0, curv2 = 0;
    while (curv1 < alls[0].size()) {
      if (curv2 >= alls[0][curv1].size()) {
	curv2 = 0;
	curv1++;
	continue;
      }
      bool found = true;
      for (int i = 1; i < N; i++) {
	int j = inds[i];
	bool foundj = false;
	//cout << cur << " " << j  << " " << i << endl;
	for (; j < alls[i].size() && !foundj; j++) {
	  bool notfound = false;
	  for (int k = 0; k < alls[i][j].size(); k++) {
	    if (alls[i][j][k] == alls[0][curv1][curv2]) {
	      foundj = true;
	      break;
	    }
	    else if (alls[i][j][k] > alls[0][curv1][curv2]) {
	      notfound = true;
	      break;
	    }
	  }
	  if (notfound) {
	    break;
	  }
	}
	inds[i] = j;
	if (!foundj) {
	  found = false;
	  break;
	}
      }
      if (found) {
	ans++;
	curv1++;
	curv2 = 0;
      }
      else {
	curv2++;
      }
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
