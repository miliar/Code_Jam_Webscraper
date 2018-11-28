#include <cstdio>
#include <cstring>
#include <queue>
#include <map>
using namespace std;

char buf[100];

void solve() {
  scanf("%s", buf);
  int N = strlen(buf);

  for (int i = 0; i < N-1; i++) {
    if (buf[i] > buf[i+1]) {
      while (i > 0 && buf[i-1] == buf[i])
        i--;
      buf[i]--;
      for (int j = i+1; j < N; j++)
        buf[j] = '9';
      break;
    }
  }

  int beg = 0;
  while (buf[beg] == '0')
    beg++;
  printf("%s\n", buf+beg);
}

int main() {
    int T;
    scanf("%d ", &T);
    for (int t = 0; t < T; t++) {
      printf("Case #%d: ", t+1);
      solve();
    }
}