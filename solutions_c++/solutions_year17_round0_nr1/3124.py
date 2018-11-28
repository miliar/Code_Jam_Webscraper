#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

int tn;
string s;
int k;

int main() {
  //assert(freopen("input.txt","r",stdin));
  //assert(freopen("output.txt","w",stdout));

  scanf("%d\n", &tn);

  for (int test = 1; test <= tn; test++) {
    getline(cin, s, ' ');
    scanf("%d\n", &k);

    int len = (int) s.length();
    int ans = 0;

    for (int i = 0; i < len; i++) {
      if (s[i] == '-' && i + k <= len) {
        ans++;
        for (int j = i; j < i + k; j++) {
          if (s[j] == '-') {
            s[j] = '+';
          } else {
            s[j] = '-';
          }
        }
      }
    }

    bool ok = true;
    for (int i = 0; i < len; i++) {
      if (s[i] != '+') {
        ok = false;
      }
    }

    printf("Case #%d: ", test);
    if (!ok) {
      puts("IMPOSSIBLE");
    } else {
      cout << ans << endl;
    }

  }

  return 0;
}