#include <stdio.h>

int main(void) {
  int tc,i,j,k,l;
  int d,n;
  int data[1001][2];
  double ans;
  double max;
  double tmp;
  int chk;

  FILE *in = fopen("input.txt", "r");
  FILE *out = fopen("output.txt", "w");

  fscanf(in,"%d", &tc);

  for (k=1; k<=tc; k++) {
    fscanf(in,"%d %d",&d, &n);
    for (i=0; i<n; i++) {
      fscanf(in,"%d %d",&data[i][0],&data[i][1]);
    }

    max = 0.0; chk = n;
    for (i=0; i<n; i++) {
      tmp = ((double)d - (double)data[i][0]) / (double)data[i][1];
      if (max < tmp) {
        chk = i;
        max = tmp;
      }
    }

    ans = d / max;

    fprintf(out, "Case #%d: %.6f", k, ans);
    fprintf(out, "\n");
  }

  return 0;
}
