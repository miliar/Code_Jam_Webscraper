#include <cstdio>
#include <string>
using namespace std;

#define INF 0x33433433

int T;
int K;
char buf[114514];

int main() {
  scanf("%d", &T);
  for (int Case=1; Case<=T; Case++) {
    scanf("%s%d", buf, &K);
    int ans = 0;
    string s = buf;
    int n = s.size() - K + 1;
    for (int i=0; i<n; i++) {
      if (s[i] == '+') continue;
      ans++;
      for (int j=0; j<K; j++) {
        if (s[i+j] == '-') s[i+j] = '+';
        else s[i+j] = '-';
      }
    }

    for (int i=0; i<s.size(); i++) {
      if (s[i] == '-') {
        ans = INF;
        break;
      }
    }

    printf("Case #%d: ", Case);
    if (ans == INF) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
  }
}
