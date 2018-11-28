#include <cstdio>
const int maxn = 128;
bool row_used[maxn]; //i
bool col_used[maxn]; //j
bool md_used[2*maxn]; //i+j
bool rd_used[2*maxn]; //i-j+n

char original[maxn][maxn];
char solution[maxn][maxn];

void add_plus(int row, int col, int n) {
  if (solution[row][col]=='.')
    solution[row][col]='+';
  else
    solution[row][col]='o';
  md_used[row+col]=rd_used[row-col+n]=true;
}
void add_x(int row, int col) {
  if (solution[row][col]=='.')
    solution[row][col]='x';
  else
    solution[row][col]='o';
  row_used[row]=col_used[col]=true;
}
void try_add_plus(int row, int col, int n) {
  if (!md_used[row+col] && !rd_used[row-col+n])
    add_plus(row, col, n);
}
void try_add_x(int row, int col) {
  if (!row_used[row] && !col_used[col])
    add_x(row, col);
}
int main() {
  int tests;
  int n, m;
  char sym;
  int row, col;
  int score, changes;
  scanf(" %d", &tests);
  for(int test_number=1; test_number<=tests; ++test_number) {
    printf("Case #%d:", test_number);
    scanf(" %d %d", &n, &m);
    for(int i=0; i<n; ++i) {
      row_used[i]=col_used[i]=false;
      for(int j=0; j<n; ++j) {
	original[i][j]=solution[i][j]='.';
      }
    }
    for(int i=0; i<2*n; ++i) {
      md_used[i]=rd_used[i]=false;
    }
    for(int i=0; i<m; ++i) {
      scanf(" %c %d %d", &sym, &row, &col);
      --row; --col;
      original[row][col]=solution[row][col]=sym;
      if (sym!='+') {
	row_used[row]=true;
	col_used[col]=true;
      }
      if (sym!='x') {
	md_used[row+col]=true;
	rd_used[row-col+n]=true;
      }
    }
    for(int i=0; i<n; ++i) {
      try_add_plus(0, i, n);
      try_add_plus(n-1, i, n);
      try_add_plus(i, 0, n);
      try_add_plus(i, n-1, n);
    }
    for(int i=1; i<n-1; ++i) {
      for(int j=1; j<n-1; ++j) {
	try_add_plus(i, j, n);
      }
    }
    for(int i=0; i<n; ++i) {
      for(int j=0; j<n; ++j) {
	try_add_x(i, j);
      }
    }
    score = 0;
    changes = 0;
    for(int i=0; i<n; ++i) {
      for(int j=0; j<n; ++j) {
	if (solution[i][j]=='o')
	  score+=2;
	else if (solution[i][j]!='.')
	  score++;
	if (solution[i][j]!=original[i][j])
	  ++changes;
      }
    }
    printf(" %d %d\n", score, changes);
    /* for(int i=0; i<n; ++i) {
      for(int j=0; j<n; ++j) {
	printf("%c", solution[i][j]);
      }
      printf("\n");
      }*/
    for(int i=0; i<n; ++i) {
      for(int j=0; j<n; ++j) {
	if (solution[i][j]!=original[i][j])
	  printf("%c %d %d\n", solution[i][j], i+1, j+1);
      }
    }
  }
  return 0;
}
