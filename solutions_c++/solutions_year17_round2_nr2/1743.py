#include <stdio.h>

int main(void) {
  int tc,i,j,k,l;
  int d,n;
  int data[6];
  int c;

  FILE *in = fopen("input.txt", "r");
  FILE *out = fopen("output.txt", "w");

  fscanf(in,"%d", &tc);

  for (k=1; k<=tc; k++) {
    fscanf(in,"%d",&n);
    for (i=0; i<6; i++) {
      fscanf(in,"%d",&data[i]);
    }

    fprintf(out, "Case #%d: ", k);

    if (data[0] > data[2] + data[4] || data[2] > data[0] + data[4] || data[4] > data[0] + data[2]) {
      fprintf(out, "IMPOSSIBLE\n");
      continue;
    }

    if (data[0] > 0) {
      fprintf(out, "R");
      data[0]--;
    }
    c = data[2] + data[4] - data[0];
    if (data[2] < data[4]) {
      for (i=0; i<c/2; i++) {
        fprintf(out,"BY");
        data[2]--; data[4]--;
      }
      if (c % 2 == 1) {
        fprintf(out,"B");
        data[4]--;
      }
    }
    else {
      for (i=0; i<c/2; i++) {
        fprintf(out,"YB");
        data[2]--; data[4]--;
      }
      if (c % 2 == 1) {
        fprintf(out,"Y");
        data[2]--;
      }
    }

    for (i=0; i<data[0]; i++) {
      fprintf(out,"R");
      if (data[2] > 0) {
        fprintf(out,"Y");
        data[2]--;
      }
      else {
        fprintf(out,"B");
        data[4]--;
      }
    }

    fprintf(out, "\n");
  }

  return 0;
}
