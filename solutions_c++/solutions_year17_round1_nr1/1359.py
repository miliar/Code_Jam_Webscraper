#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <vector>

using namespace std;

#define MAX 32
char s[MAX][MAX];
int T, R, C;

int main() {
  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++) {
    scanf("%d %d", &R, &C);
    for(int i = 0; i < R; i++)
      scanf("%s", s[i]);

    for(int i = 0; i < R; i++){
      for(int j = 0; j < C; j++){
        if (s[i][j] != '?'){
          for(int k = j-1; k >= 0 && s[i][k] == '?'; k--){
            s[i][k] = s[i][j];
          }

          for(int k = j+1; k < C && s[i][k] == '?'; k++){
            s[i][k] = s[i][j];
          }
        }
      }
    }

    for(int i = 0; i < R; i++){
      if (s[i][0] == '?'){
        int k = i-1;
        while(k >= 0 && s[k][0] == '?') k--;

        if (k < 0){
          k = i+1;
          while(k < R && s[k][0] == '?') k++;
        }

        for(int j = 0; j < C; j++) s[i][j] = s[k][j];
      }
    }

    printf("Case #%d:\n", caso);
    for(int i = 0; i < R; i++)
      printf("%s\n", s[i]);
  }
  return 0;
}

