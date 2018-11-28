#include <bits/stdc++.h>

using namespace std;

// cases:
// swap at midnight
// no swap at midnight

// starts with Cameron
// starts with Jamie

int C[101];
int D[101];

int J[101];
int K[101];

int DC[1441][1441];// C dolgozott epp, min. csere
int DJ[1441][1441];// J dolgozott epp, min. csere
int T[1441];

#define CC 1
#define JJ 2
// T[i] == 1 => Cameron
void fillD() {
  for (int i = 2; i <= 1440; i++) {
    if (T[i] == JJ) DC[i][0] = 1442;
    else DC[i][0] = DC[i-1][0];
    int x = i; if (x > 720) x = 720;
    for (int j = 1; j <= x; j++) {
      if (T[i] == CC) {
        DJ[i][j] = 1442;
      } else {
        DJ[i][j] = min(1+DC[i-1][j-1], DJ[i-1][j-1]);
      }
      if (T[i] == JJ) {
        DC[i][j] = 1442;
      } else {
        DC[i][j] = min(DC[i-1][j], 1+DJ[i-1][j]);
      }
    }
  }
}

int main() {
  int TT;
  scanf("%d", &TT);
  for (int TTT = 1; TTT <= TT; TTT++) {
    printf("Case #%d: ", TTT);
    int nc, nj;
    scanf("%d%d", &nc, &nj);

    // init T
    for (int i = 0; i <= 1440; i++)
      T[i] = 0;
    for (int i = 0; i < nc; i++) {
      int a,b;
      scanf("%d%d", &a, &b);
      for (int j = a; j < b; j++) T[j+1] = CC; // C
    }
    for (int i = 0; i < nj; i++) {
      int a,b;
      scanf("%d%d", &a, &b);
      for (int j = a; j < b; j++) T[j+1] = JJ; // J
    }

    // init D?
    for (int i = 0; i <= 1440; i++)
      for (int j = 0; j <= 1440; j++)
        DC[i][j] = DJ[i][j] = 1442;

    // GO!
    if (T[1] != JJ) {DC[1][0] = 0;
    fillD();}
    int a = DC[1440][720];
    int b = DJ[1440][720]+1;
    // DEBUG
/*      printf("\n");
    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        if (DC[i][j] < 1442) printf("%d", DC[i][j]);
        else printf("-");
        printf("|");
        if (DJ[i][j] < 1442) printf("%d", DJ[i][j]);
        else printf("-");
        printf(" ");
      }
      printf("\n");
    }*/
    // Init D
    for (int i = 0; i <= 1440; i++)
      for (int j = 0; j <= 1440; j++)
        DC[i][j] = DJ[i][j] = 1442;
    // GO!
    if (T[1] != CC) {DJ[1][1] = 0;
    fillD();}

    int c = DC[1440][720]+1;
    int d = DJ[1440][720];
    
    // DEBUG
/*      printf("\n");
    for (int i = 0; i < 10; i++) {
      for (int j = 0; j < 10; j++) {
        if (DC[i][j] < 1442) printf("%d", DC[i][j]);
        else printf("-");
        printf("|");
        if (DJ[i][j] < 1442) printf("%d", DJ[i][j]);
        else printf("-");
        printf(" ");
      }
      printf("\n");
    }
      printf("\n");
    for (int i = 1431; i <= 1440; i++) {
      for (int j = 1431; j <= 1440; j++) {
        if (DC[i][j] < 1442) printf("%d", DC[i][j]);
        else printf("-");
        printf("|");
        if (DJ[i][j] < 1442) printf("%d", DJ[i][j]);
        else printf("-");
        printf(" ");
      }
      printf("\n");
    }*/
    // eval
    //printf("(C,n)%d (C,y)%d (J,y)%d (J,n)%d)\n", a, b, c, d);
    int mn = min(min(a,b),min(c,d));
    printf("%d\n", mn);
  }
  return 0;
}
