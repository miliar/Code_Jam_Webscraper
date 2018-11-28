#include <bits/stdc++.h>
using namespace std;

#ifdef DEBUG
#define D(x...) fprintf(stderr,x)
#else
#define D(x...)
#endif

#define M(x) (((x%MOD)+MOD)%MOD)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const ll MOD = (ll)(1e9)+7ll;

const int MAX_N = 105;

int N, P;
int nums[MAX_N];

int md[5];
int cache[MAX_N][MAX_N][MAX_N][5];

int main() {
  int T;
  scanf("%d",&T);

  for (int z=1;z<=T;z++) {
    printf("Case #%d: ",z);

    scanf("%d %d",&N,&P);
    for (int i=0;i<N;i++) {
      scanf("%d",&nums[i]);
      nums[i] %= P;
    }

    int ans = 0;
    for (int i=0;i<5;i++) {
      md[i] = 0;
    }
    for (int i=0;i<N;i++) {
      if (nums[i] == 0) {
        ans++;
      }
      md[nums[i]]++;
    }

    for (int a=0;a<=md[1];a++) {
      for (int b=0;b<=md[2];b++) {
        for (int c=0;c<=md[3];c++) {
          for (int d=0;d<=P;d++) {
            if (a == 0 && b == 0 && c == 0) {
              cache[a][b][c][d] = 0;
            } else {
              cache[a][b][c][d] = -MAX_N;
              if (a) {
                cache[a][b][c][d] = max(cache[a][b][c][d],
                    cache[a-1][b][c][(d-1+P+P+P)%P]);
              }
              if (b) {
                cache[a][b][c][d] = max(cache[a][b][c][d],
                    cache[a][b-1][c][(d-2+P+P+P)%P]);
              }
              if (c) {
                cache[a][b][c][d] = max(cache[a][b][c][d],
                    cache[a][b][c-1][(d-3+P+P+P)%P]);
              }
              if (d == 0) {
                cache[a][b][c][d]++;
              }
            }
          }
        }
      }
    }
    printf("%d\n", ans + cache[md[1]][md[2]][md[3]][0]);
  }
  return 0;
}
