#include <bits/stdc++.h>
#define REP(x, n) for (int x = 0; x < (int)(n); x++)
#define RREP(x, n) for (int x = (int)(n)-1; x >= 0; --x)
#define FOR(x, m, n) for (int x = (int)m; x < (int)(n); x++)
#define EACH(itr, cont) \
  for (typeof((cont).begin()) itr = (cont).begin(); itr != (cont).end(); ++itr)
#define ALL(X) (X).begin(), (X).end()
#define mem0(X) memset((X), 0, sizeof(X))
#define mem1(X) memset((X), 255, sizeof(X))

using namespace std;
typedef long long LL;
typedef pair<LL, LL> PLL;

void doStuff() {
  LL K, N, next = -1, cnt = 0;
  scanf("%lld %lld", &N, &K);
  priority_queue<PLL> q;
  q.push(PLL(N, 1));
  while (true) {
    if(next==-1 or (q.size()>0 and q.top().first==next))
      next = q.top().first, cnt += q.top().second, q.pop();
    else {
      LL cur = next - 1;
      LL low = cur / 2;
      LL high = cur - low;
      if(cnt>=K){
        printf("%lld %lld\n", high, low);
        return;
      }else{
        q.push(PLL(high,cnt));
        q.push(PLL(low, cnt));
        K -= cnt, next = -1, cnt = 0;
      }
    }
  }
 }

int main() {
  int T;
  scanf("%d", &T);
  REP(t, T) printf("Case #%d: ", t + 1), doStuff();
  return 0;
}