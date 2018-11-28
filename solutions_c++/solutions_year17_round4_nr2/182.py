#include <iostream>
#include <stdio.h>
using namespace std;

#define MAXN 2000

int main()
{
  int numTests;
  int a[MAXN], b[MAXN];
  cin >> numTests;
  for(int test = 1; test <= numTests; test++) {
    int N, C, M;
    cin >> N >> C >> M;
    for (int i = 0; i < MAXN; i++) {a[i] = 0; b[i] = 0;}
    int ans = 0;
    for (int i = 0; i < M; i++) {
      int Pos, Bin;
      cin >> Pos >> Bin;
      a[Pos] ++; b[Bin] ++;
      if (b[Bin] > ans) ans = b[Bin];
    }
    int accu = 0;
    for (int i = 1; i <= N; i++) {
      accu += a[i];
      while (ans * i < accu) ans++;
    }

    int ans2 = 0;
    for (int i = 1; i <= N; i++) {
      if (a[i] > ans) ans2 += a[i] - ans;
    }

    cout << "Case #" << test << ": " << ans << " " << ans2 << endl;
  }
}
