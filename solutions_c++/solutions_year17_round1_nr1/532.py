#include <cstdio>
#include <cctype>
#include <cstring>

const int maxn = 32;
char mtx[maxn][maxn];

void drag(int n, int m, int di, int dj) {
  for(int i=1; i<=n; ++i)
    for(int j=1; j<=m; ++j)
      if (isalpha(mtx[i][j])) {
	for(int ii=i+di, jj=j+dj; ; ii+=di, jj+=dj)
	  if (mtx[ii][jj]=='?')
	    mtx[ii][jj]=mtx[i][j];
	  else
	    break;
      }
}

int main() {
  int n, m;
  int tests;
  scanf(" %d", &tests);
  for(int test_number=1; test_number<=tests; ++test_number) {
    printf("Case #%d:\n", test_number);
    scanf(" %d %d", &n, &m);
    for(int i=0; i<n+2; ++i)
      mtx[i][0] = mtx[i][m+1] = '#';
    for(int j=0; j<m+2; ++j)
      mtx[0][j] = mtx[n+1][j] = '#';
    for(int i=1; i<=n; ++i)
      for(int j=1; j<=m; ++j)
	scanf(" %c", &mtx[i][j]);
    drag(n, m, -1, 0);
    drag(n, m, 1, 0);
    drag(n, m, 0, -1);
    drag(n, m, 0, 1);
    for(int i=1; i<=n; ++i) {
      for(int j=1; j<=m; ++j)
	printf("%c", mtx[i][j]);
      printf("\n");
    }
  }
  return 0;
}
