#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <functional>
#include <time.h>
#include <ctype.h>
#include <stack>
#include <bitset>

using namespace std;

typedef long long ll;
typedef unsigned long long llu;

const int MAXN = 30;

char str[MAXN][MAXN];

int R, C, T, test = 1;

void line(int x, int y, char c){
  str[x][y] = c;
  if(y > 1 && str[x][y - 1] == '?') line(x, y - 1, c);
  if(y < C && str[x][y + 1] == '?') line(x, y + 1, c);
}

int main(){
#ifdef DEBUG
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  scanf("%d", &T);
  while(T--){
    scanf("%d %d", &R, &C);
    for(int i=1; i<=R; ++i) scanf("%s", str[i] + 1);
    for(int i=1; i<=R; ++i)
      for(int j=1; j<=C; ++j) if(str[i][j] != '?') line(i, j, str[i][j]);
    for(int i=1; i<=R; ++i){
      if(str[i][1] == '?'){
        int pos = -1;
        for(int k=i-1; k>=1; --k){
          if(str[k][1] != '?'){ pos = k; break; }
        }
        if(pos == -1){
          for(int k=i+1; k<=R; ++k){
            if(str[k][1] != '?'){ pos = k; break; }
          }
        }
        for(int j=1; j<=C; ++j) str[i][j] = str[pos][j];
      }
    }
    printf("Case #%d:\n", test++);
    for(int i=1; i<=R; ++i) printf("%s\n", str[i] + 1);
  }
  return 0;
}
