#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cassert>
using namespace std;

int main() {
  int T; scanf("%d", &T);
  for(int tc = 1;tc <= T;++tc) {
    printf("Case #%d: ", tc);
    int ac, aj;
    scanf("%d%d", &ac, &aj);
    if(ac < aj) swap(ac, aj);

    pair<int,int> d[5];
    for(int i = 0;i < ac+aj;++i)
      scanf("%d%d", &d[i].first, &d[i].second);

    if(ac == 1) { // bisa ada aj, bisa juga nggak
      puts("2");
    } else {
      assert(ac == 2);
      if(d[0].first > d[1].first) swap(d[0], d[1]);

      if(d[1].second - d[0].first <= 12*60 || d[0].second+24*60 - d[1].first <= 12*60) puts("2");
      else {
        puts("4");
      }
    }
  }
}
