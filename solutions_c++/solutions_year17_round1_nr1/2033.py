#include <cstdio>
#include <cstdint>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

char d[27][27];
int r, c;

void print_row(int ir) {
  for (int ic=0; ic<c; ++ic) putchar(d[ir][ic]);
  putchar('\n');
}


bool is_row_empty(int ir) {
  for (int i=0; i<c; ++i) {
    if (d[ir][i] != '?') return false;
  }
  return true;
}

void fill_row(int ir) {
  for (int i=0, ipr=-1; i<c; ++i) {
    if (d[ir][i] != '?') {
      for (int j=ipr+1; j<i; ++j) d[ir][j] = d[ir][i];
      ipr = i;
    } else if (i==c-1) {
      for (int j=ipr+1; j<c; ++j) d[ir][j] = d[ir][ipr];
    }
  }
}

void copy_row(int to, int from) {
  for (int i=0; i<c; ++i) d[to][i] = d[from][i];
}

void fill() {
  for (int i=0, ipr=-1; i<r; ++i) {
    if (!is_row_empty(i)) {
      fill_row(i);
//printf("\tfound non empty row %d: ", i); print_row(i);
//printf("\tfilling backward from %d to %d\n", ipr+1, i-1);
      for (int j=ipr+1; j<i; ++j) copy_row(j, i);
      ipr = i;
    } else if (i==r-1) {
//printf("\tfilling forward from %d to %d\n", ipr+1, r-1);
      for (int j=ipr+1; j<r; ++j) copy_row(j, ipr);
    }
  }
}

void print() {
  for (int ir=0; ir<r; ++ir) {
    for (int ic=0; ic<c; ++ic) putchar(d[ir][ic]);
    putchar('\n');
  }
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i=1; i<=n; ++i) {
    scanf("%d %d\n", &r, &c);
    for (int ir=0; ir<r; ++ir) {
      char buf[32];
      scanf("%s", buf);
      for (int ic=0; ic<c; ++ic) d[ir][ic] = buf[ic];
    }
//print();
    fill();
    printf("Case #%d:\n", i);
    print();
  }
}
