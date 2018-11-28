#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <vector>

using namespace std;

long long N;

int main() {
  int T;

  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++) {
    scanf("%lld", &N);

    long long r = 1;
    for(long long i = 2; i <= N; i++){
      char s[256];
      sprintf(s, "%lld", i);

      int ok = 1;
      for(int j = 1; ok && s[j]; j++)
        if (s[j] < s[j-1])
          ok = 0;

      if (ok) r = i;
    }

    printf("Case #%d: %lld\n", caso, r);
  }
  return 0;
}

