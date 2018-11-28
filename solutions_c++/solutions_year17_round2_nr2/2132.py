#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

const int MAXN = 1111;
char s[MAXN];

int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    int N;
    int R, O, Y, G, B, V;
    cin >> N;
    cin >> R >> O >> Y >> G >> B >> V;
    s[N] = 0;
    printf("Case #%d: ", cases + 1);
    if (2 * R > N || 2 * Y > N || 2 * B > N) {
      printf("IMPOSSIBLE\n");
    } else if (R + Y > N / 2) {
      int RR = R, YY = Y;
      char CR = 'R', CY = 'Y';
      if (RR < YY) {
        swap(RR, YY);
        swap(CR, CY);
      }
      for (int i = 0; i < N; i += 2) {
        if (RR > 0) {
          s[i] = CR;
          --RR;
        } else {
          s[i] = CY;
          --YY;
        }
      }
      int BB = B;
      for (int i = 1; ; i += 2) {
        if (YY > 0) {
          s[i] = CY;
          --YY;
        } else if (BB > 0) {
          s[i] = 'B';
          --BB;
        } else {
          break;
        }
      }
      printf("%s\n", s);
    } else if (Y + B > N / 2) {
      int BB = B, YY = Y;
      char CB = 'B', CY = 'Y';
      if (BB < YY) {
        swap(BB, YY);
        swap(CB, CY);
      }
      for (int i = 0; i < N; i += 2) {
        if (BB > 0) {
          s[i] = CB;
          --BB;
        } else {
          s[i] = CY;
          --YY;
        }
      }
      int RR = R;
      for (int i = 1; ; i += 2) {
        if (YY > 0) {
          s[i] = CY;
          --YY;
        } else if (RR > 0) {
          s[i] = 'R';
          --RR;
        } else {
          break;
        }
      }
      printf("%s\n", s);
    } else if (R + B > N / 2) {
      int BB = B, RR = R;
      char CR = 'R', CB = 'B';
      if (RR < BB) {
        swap(RR, BB);
        swap(CR, CB);
      }
      for (int i = 0; i < N; i += 2) {
        if (BB > 0) {
          s[i] = CB;
          --BB;
        } else {
          s[i] = CR;
          --RR;
        }
      }
      int YY = Y;
      for (int i = 1; ; i += 2) {
        if (RR > 0) {
          s[i] = CR;
          --RR;
        } else if (YY > 0) {
          s[i] = 'Y';
          --YY;
        } else {
          break;
        }
      }
      printf("%s\n", s);
    } else {
      printf("IMPOSSIBLE\n");
    }
  }
}