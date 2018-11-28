#include <cstdio>
#include <vector>

using namespace std;

const int maxn = 25;
char mat[maxn+5][maxn+5];
int r, c;
vector<vector<int> > hfilled;
vector<vector<int> > vfilled;

int main() {
  int tc;
  scanf("%d", &tc);
  for(int kase = 1; kase <= tc; kase++) {
    scanf("%d%d\n", &r, &c);
    for(int i = 0; i < r; i++)
      scanf("%s\n", mat[i]);
    for(int i = 0; i < r; i++) {
      bool ok = false;
      for(int j = 0; j < c; j++) {
	if(mat[i][j] != '?') {
	  ok = true;
	  break;
	}
      }
      if(!ok) {
	continue;
      }
      char prev = 0;
      for(int j = 0; j < c; j++) {
	if(mat[i][j] != '?') {
	  prev = mat[i][j];
	  continue;
	}
	if(prev == 0)
	  continue;
	mat[i][j] = prev;
      }
      prev = 0;
      for(int j = c - 1; j >= 0; j--) {
	if(mat[i][j] != '?') {
	  prev = mat[i][j];
	  continue;
	}
	if(prev == 0)
	  continue;
	mat[i][j] = prev;
      }
    }
    for(int j = 0; j < c; j++) {
      char prev = 0;
      for(int i = 0; i < r; i++) {
	if(mat[i][j] != '?') {
	  prev = mat[i][j];
	  continue;
	}
	if(prev == 0)
	  continue;
	mat[i][j] = prev;
      }
      prev = 0;
      for(int i = r - 1; i >= 0; i--) {
	if(mat[i][j] != '?') {
	  prev = mat[i][j];
	  continue;
	}
	if(prev == 0)
	  continue;
	mat[i][j] = prev;
      }
    }
    printf("Case #%d:\n", kase);
    for(int i = 0; i < r; i++)
      printf("%s\n", mat[i]);
  }
  return 0;
}
