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

string FILENAME = "B-large";

bool is_tidy(int n) {
  string s = to_string(n);
  for (int j = 0; j < s.size() - 1; j++) {
    if (s[j] > s[j + 1]) {
      return false;
    }
  }
  return true;
}

int main () {
  setvbuf(stdout, NULL, _IONBF, 0);
  freopen((FILENAME + ".in").c_str(), "r", stdin);
  freopen((FILENAME + ".out").c_str(), "w", stdout);
  int testcases;
  scanf("%d", &testcases);
  for (int case_id = 1; case_id <= testcases; case_id++) {
    printf("Case #%d: ", case_id);
    long long n;
    cin >> n;
    /*
    for (int i = n; i >= 0; i--) {
      if (is_tidy(i)) {
        printf("%d\n", i);
        break;
      }
    }
    */
    string s = to_string(n);
    for (int i = 0; i < s.size() - 1; i++) {
      if (s[i + 1] < s[i]) {
        if (s[i] == '1') {
          int back_index = i;
          while (back_index >= 0 && s[back_index] == '1') {
            s[back_index--] = '9';
          }
          if (back_index < 0) {
            string copy_str;
            for (int j = 0; j < s.size() - 1; j++) {
              copy_str.push_back('9');
            }
            s = copy_str;
          }
        } else {
          int change_index = i;
          while (change_index - 1 >= 0 && s[change_index] == s[change_index - 1]) {
            s[change_index] = '9';
            change_index--;
          }
          s[change_index]--;
        }
        for (int j = i + 1; j < s.size(); j++) {
          s[j] = '9';
        }
        break;
      }
    }
    printf("%s\n", s.c_str());
  }
  fflush(stdout);
}
