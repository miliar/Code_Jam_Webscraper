#include <algorithm>
#include <cstdio>
#include <vector>
#include <set>

using namespace std;
typedef int64_t i64;

struct Entry {
  Entry(i64 s, i64 l) {
    size = s;
    left = l;
    min = (size - 1) / 2;
    max = (size) / 2;
  }
  i64 size;
  i64 left;
  i64 min; 
  i64 max;

  bool operator<(const Entry& e) const {
    return min > e.min || (min == e.min && max > e.max) || (min == e.min && max == e.max && left < e.left);
  }
};

int main() {
  i64 T;
  scanf("%lld", &T);
  for (i64 zz = 1; zz <= T; zz++) {
    i64 N, K;
    scanf("%lld %lld", &N, &K);
    set<Entry> S;
    S.insert(Entry(N, 0));
    i64 min, max;
    for (i64 i = 0; i < K; i++) {
      Entry e = *S.begin();
      S.erase(S.begin());
      max = e.max;
      min = e.min;

      S.insert(Entry(min, e.left));
      S.insert(Entry(max, e.left + min + 1));
    }

    printf("Case #%lld: %lld %lld\n", zz, max, min);
  }
}
