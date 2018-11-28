#include <stdio.h>
#include <queue>
using namespace std;
int main(void)
{
  int T;
  long long N;
  int K;
  long long tmp;
  long long a, b;

  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    scanf("%lld %d", &N, &K);
    priority_queue<long long> pq;
    pq.push(N);
    for (int i = 1; i <= K; i++) {
      tmp = pq.top()-1;
      pq.pop();
      if (tmp%2) {
        a = tmp/2+1;
        b = tmp/2;
      } else {
        a = tmp/2;
        b = tmp/2;
      }

      if (i == K) {
        printf("%d %d\n", a, b);
      } else {
        pq.push(a);
        pq.push(b);
      }

    }

  }


  return 0;
}

