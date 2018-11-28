#include <stdio.h>
#include <string.h>

int main(void) {
  int tc,i,k,l,len,cnt;
  int s;
  char data[30];

  FILE *in = fopen("input.txt", "r");
  FILE *out = fopen("output.txt", "w");

  fscanf(in,"%d", &tc);

  for (k=1; k<=tc; k++) {
    fscanf(in,"%s",data);
    len = strlen(data);
    if (len==1) {
      fprintf(out, "Case #%d: %s\n", k, data);
      continue;
    }

    s=0;
    for (i=1; i<len; i++) {
      if (data[i] < data[i-1]) {
        break;
      }
      if (data[i] != data[i-1]) {
        s=i;
      }
    }
    if (i < len) {
      for (i=s+1; i<len; i++) {
        data[i] = '9';
      }
      data[s] -= 1;
    }

    fprintf(out, "Case #%d: ", k);
    for (i=0; i<len; i++) {
      if (data[i] != '0') {
        fprintf(out, "%c", data[i]);
      }
    }
    fprintf(out, "\n");
  }

  return 0;
}
