#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long lglg;

int main()
{
  int T;
  scanf("%d", &T);

  char row[1005];
  int k;

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    scanf("%s %d\n", row, &k);
    int flips = 0;

    int len = strlen(row);
    for (int i = 0; i <= len-k; ++i) {
      if(row[i] == '-') {
        ++flips;
        for (int j = 0; j < k; ++j) {
          row[i+j] = '-' + '+' - row[i+j];
        }
      }
    }

    bool bad = false;
    for (int i = len-k+1; i < len; ++i) {
      if(row[i] == '-') {
        bad = true;
      }
    }

    if(bad) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", flips);
    }
  }

  return 0;
}
