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

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);

    lglg num, k;

    scanf("%lld %lld", &num, &k);

    map<lglg, lglg> lennum;

    lennum[num] = 1;

    while(k > 0) {
      auto lenp = *(lennum.rbegin());

      lglg len = lenp.first;
      lglg lendb = lenp.second;
//      printf("%lld %lld\n", len, lendb);

      if(k <= lendb) {
        lglg h1 = (lenp.first - 1) / 2;
        lglg h2 = (lenp.first - 1) / 2 + (lenp.first - 1) % 2;
        printf("%lld %lld\n", h2, h1);
      } else {
        lglg h1 = (lenp.first - 1) / 2;
        lglg h2 = (lenp.first - 1) / 2 + (lenp.first - 1) % 2;
        if(lennum.count(h1) > 0) {
          lennum[h1] = lennum[h1] + lendb;
        } else {
          lennum[h1] = lendb;
        }
        if(lennum.count(h2) > 0) {
          lennum[h2] = lennum[h2] + lendb;
        } else {
          lennum[h2] = lendb;
        }
        lennum.erase(lennum.find(len));
      }

      k -= lenp.second;
    }
  }

  return 0;
}
