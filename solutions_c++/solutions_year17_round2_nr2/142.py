#include <stdio.h>

int pchar(int i, int r) {
  if (i == 0 && r == 0) return 'R';
  if (i == 1 && r == 0) return 'Y';
  if (i == 2 && r == 0) return 'B';
  if (i == 0 && r == 1) return 'G';
  if (i == 1 && r == 1) return 'V';
  if (i == 2 && r == 1) return 'O';
}
int main() {
  int t;
  int c[5],r[5];
  int res[10000];
  int num = 0;
  scanf("%d",&t);
  for (int e = 0 ; e< t ;e ++) {
    int n;
    int imp = 0;
    num = 0;
    scanf("%d%d%d%d%d%d%d",&n, &c[0], &r[2], &c[1], &r[0], &c[2], &r[1]);
    // TODO: n = 1
    int tc[5];
    int fin = 0;
    printf("Case #%d: ", e+1);
    if (n == 1) {
      for(int i = 0 ; i < 3 ; i++) {
        if (c[i] > 0) printf("%c", pchar(i,0));
        if (r[i] > 0) printf("%c", pchar(i,1));
      }
      printf("\n");
      continue;
    }
    for(int i = 0; i < 3; i++) {
      tc[i] = c[i]-r[i];
      // printf("%d %d\n",c[i],r[i]);
      if (c[i] > 0 && c[i] == r[i]) {
        for(int j = 0 ; j < 3 ; j++) {
          if (i != j && (c[j] > 0 || r[j] > 0)) {
            imp = 1;
          }
        }
        if (!imp) {
          for(int j = 0 ; j < c[i] ; j++) {
            printf("%c",pchar(i,0));
            printf("%c",pchar(i,1));
          }
          printf("\n");
          fin = 1;
          break;
        }
      }
      if (tc[i] < 0) imp = 1;
    }
    if (fin) continue;
    if(imp) {
      printf("IMPOSSIBLE\n");
      continue;
    }
    int cur;
    int maxx = -1;
    for(int i = 0 ;i < 3; i++) {
      if( tc[i] > maxx) {
        cur = i;
        maxx = tc[i];
      }
    }
    if (tc[0] > 0) cur = 0;
    while(1) {
      res[num++] = cur;
      tc[cur]--;
      maxx = -1;
      int new_cur;
      for(int i = 0 ; i < 3 ; i++) {
        if (i != cur & tc[i] > maxx && tc[i] > 0) {
          maxx = tc[i];
          new_cur = i;
        }
      }
      if (maxx == -1) {
        break;
      }
      cur = new_cur;
    }
    if (res[num-1] == res[0] || tc[0] > 0 || tc[1] > 0 || tc[2] > 0) {
      printf("IMPOSSIBLE\n");
      continue;
    }

    int ch[5];
    ch[0] = ch[1] = ch[2] = 0;

    for(int i = 0 ; i < num ; i++ ){
      if (ch[res[i]] == 0) {
        ch[res[i]] = 1;
        for(int j = 0 ; j < r[res[i]] ; j++) {
          printf("%c", pchar(res[i], 0));
          printf("%c", pchar(res[i], 1));
        }
      }
      printf("%c", pchar(res[i],0));
    }
    printf("\n");
  }
}
