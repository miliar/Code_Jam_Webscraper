#include <cstdio>
#include <cstring>
#include <queue>
#include <map>
using namespace std;

void solve() {
  long long D, N;
  scanf("%lld %lld", &D, &N);

  double finish_time = -1;
  for (int i = 0; i < N; i++) {
    long long K, S;
    scanf("%lld %lld", &K, &S);
    double time = double(D-K) / double(S);
    finish_time = max(finish_time, time);
  }

  printf("%f\n", double(D) / finish_time);
}

int main() {
    int T;
    scanf("%d ", &T);
    for (int t = 0; t < T; t++) {
      printf("Case #%d: ", t+1);
      solve();
    }
}