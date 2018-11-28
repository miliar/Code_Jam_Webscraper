#include <cstdio>
#include <map>
using namespace std;

map<long long, long long> cnt;

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    printf("Case #%d: ", tt);

    long long N, K; scanf("%lld%lld", &N, &K);

    cnt.clear(); cnt[N] = 1;

    for(;;){
      auto it = cnt.end(); it--;
      long long x = it->first, y = it->second;
      long long l = (x - 1) / 2, r = x / 2;

      if(y < K){ // pass
        if(l > 0) cnt[l] += y;
        if(r > 0) cnt[r] += y;
        K -= y;
      }
      else{
        printf("%lld %lld\n", r, l);
        break;
      }

      cnt.erase(it);
    }
  }
  return 0;
}
