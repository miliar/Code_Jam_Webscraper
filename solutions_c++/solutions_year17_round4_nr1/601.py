#include <cstdio>

int G[110];
int cnt[5];

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    int N, P; scanf("%d%d", &N, &P);
    for(int i = 1; i <= N; i++) scanf("%d", &G[i]);

    for(int i = 0; i < P; i++) cnt[i] = 0;
    for(int i = 1; i <= N; i++) cnt[G[i] % P]++;

    int ans = 0;

    if(P == 2){
      // 0, 1 - 1
      ans = cnt[0] + cnt[1] / 2;
      if(cnt[1] % 2 != 0) ans++;
    }

    if(P == 3){
      ans = cnt[0];

      int v = 0;
      for(int a = 0; ; a++){ // 1 - 2
        if(a > cnt[1] || a > cnt[2]) break;
        int b = (cnt[1] - a) / 3; // 1 - 1 - 1
        int c = (cnt[2] - a) / 3; // 2 - 2 - 2

        int v_ = a + b + c;
        if(a + 3 * b < cnt[1]
          || a + 3 * c < cnt[2]) v_++;

        if(v_ > v) v = v_;
      }

      ans += v;
    }

    if(P == 4){
      ans = cnt[0];

      int v = 0;
      for(int a = 0; ; a++){ // 1 - 3
        if(a > cnt[1] || a > cnt[3]) break;
        for(int b = 0; ; b++){ // 1 - 1 - 2
          if(a + 2 * b > cnt[1] || b > cnt[2]) break;
          for(int c = 0; ; c++){ // 2 - 3 - 3
            if(b + c > cnt[2] || a + 2 * c > cnt[3]) break;

            int d = (cnt[1] - a - 2 * b) / 4; // 1 - 1 - 1 - 1
            int e = (cnt[2] - b - c) / 2; // 2 - 2
            int f = (cnt[3] - a - 2 * c) / 4; // 3 - 3 - 3 - 3

            int v_ = a + b + c + d + e + f;

            if(a + 2 * b + 4 * d < cnt[1]
              || b + c + 2 * e < cnt[2]
              || a + 2 * c + 4 * f < cnt[3]) v_++;

            if(v_ > v) v = v_;
          }
        }
      }

      ans += v;
    }

    printf("Case #%d: %d\n", tt, ans);
  }
  return 0;
}
