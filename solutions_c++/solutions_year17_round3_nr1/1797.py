#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;

typedef struct surf {
  double t;
  double s;
  int idx;
} surf;

int r[1001];
int h[1001];
surf a[1001];
surf b[1001];

bool funct(struct surf a, struct surf b) {
  return (a.t > b.t);
}

bool funct2(struct surf a, struct surf b) {
  return (a.s > b.s);
}

int main(void) {
  int tc,i,j,k,l;
  int n,o;

  FILE *in = fopen("input.txt", "r");
  FILE *out = fopen("output.txt", "w");

  fscanf(in,"%d", &tc);

  for (k=1; k<=tc; k++) {
    fscanf(in,"%d %d", &n, &o);
    for (i=0; i<n; i++) {
      fscanf(in,"%d %d",&r[i],&h[i]);
    }

    for (i=0; i<n; i++) {
      a[i].t = (double) r[i];
      a[i].s = (double) r[i] * h[i] * 2;
      b[i].t = (double) r[i];
      b[i].s = (double) r[i] * h[i] * 2;
      a[i].idx = i;
      b[i].idx = i;
    }

    sort(a, a+n, funct);
    sort(b, b+n, funct);
    sort(b, b+n, funct2);

    fprintf(out, "Case #%d: ", k);

    double max = 0.0;
    double temp = 0.0;
    for (i=0; i<o; i++) {
      temp += b[i].s;
      if (max < b[i].t) {
        max = b[i].t;
      }
    }
    temp += max * max;

    int cnt=0;
    double temp2 = a[0].t * a[0].t + a[0].s;
    for (i=0; i<n; i++) {
      if (cnt == o-1) {
        break;
      }
      if (b[i].idx != a[0].idx) {
        temp2 += b[i].s;
        cnt++;
      }
    }

    if (temp < temp2) {
      temp = temp2;
    }
    fprintf(out, "%.9lf", temp*M_PI);
    fprintf(out, "\n");
  }

  return 0;
}
