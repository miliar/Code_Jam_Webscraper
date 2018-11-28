#include <stdio.h>
#include <string.h>

int main(void) {
  int tc,i,j,k,l,len,cnt;
  char data[1001];

  FILE *in = fopen("input.txt", "r");
  FILE *out = fopen("output.txt", "w");

  fscanf(in,"%d",&tc);

  for (k=0; k<tc; k++) {
    fscanf(in,"%s %d",data,&l);

    len = strlen(data);
    cnt = 0;
    for (i=0; i<len-l+1; i++) {
      if (data[i] == '-') {
        //flip
        for (j=i; j<i+l; j++) {
          if (data[j] == '+')
            data[j] = '-';
          else
            data[j] = '+';
        }
        cnt++;
      }
    }

    for (i=0; i<len; i++) {
      if (data[i] == '-') {
        break;
      }
    }

    if (i==len) {
      fprintf(out, "Case #%d: %d\n", k+1, cnt);
    }
    else {
      fprintf(out, "Case #%d: IMPOSSIBLE\n", k+1);
    }
  }

  return 0;
}
