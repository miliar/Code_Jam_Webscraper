#include <algorithm>
#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <limits>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <cmath>

using namespace std;

int INF = std::numeric_limits<int>().max();
double INFD = std::numeric_limits<double>().max();

double PI = acos(-1);

int main() {
  ios::sync_with_stdio(false);
  int t = 0;
  cin >> t;
  int q = 0;
  while(q < t) {
    string s;
    int k = 0;
    cin >> s >> k;
    int i = 0, j = k-1, res = 0;
    while(j < s.size()) {
      if(s[i] == '-') {
        res++;
        int r = i;
        while(r <= j) {
          s[r] = (s[r] == '-') ? '+' : '-';
          r++;
        }
      }
      i++;
      j++;
    }
    i = 0;
    cout << "Case #" << ++q << ": ";
    while(i < s.size()) {
      if(s[i] == '-') {
        cout << "IMPOSSIBLE";
        break;
      }
      i++;
    }
    if(i == s.size()) {
      cout << res;
    }
    cout << endl;
  }
  return 0;
}
