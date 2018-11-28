#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <iterator>

#if DEBUG
#include "prettyprint.hpp"
#define print_container(c) cout << c << endl;
#endif

using namespace std;

string FILENAME = "A-large";

vector<int> read(string s){
  vector<int> ret;
  int n;
  istringstream sin(s);
  while(sin>>n)
    ret.push_back(n);
  return ret;
}

int main () {
  setvbuf(stdout, NULL, _IONBF, 0);
  freopen((FILENAME + ".in").c_str(), "r", stdin);
  freopen((FILENAME + ".out").c_str(), "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  for (int case_id = 1; case_id <= testcases; case_id++) {
    printf("Case #%d: ", case_id);
    char c[1000];
    int k;
    scanf("%s %d", c, &k);
    string s(c);
    int flips = 0;
    for (int i = 0; i < s.size() - k + 1; i++) {
      if (s[i] == '-') {
        flips++;
        for (int j = 0; j < k; j++) {
          if (s[i+j] == '+') {
            s[i+j] = '-';
          } else {
            s[i+j] = '+';
          }
        }
      }
    }
    bool impossible = false;
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '-') {
        printf("IMPOSSIBLE\n");
        impossible = true;
        break;
      }
    }
    if (!impossible) {
      printf("%d\n", flips);
    }
  }
  fflush(stdout);
}
