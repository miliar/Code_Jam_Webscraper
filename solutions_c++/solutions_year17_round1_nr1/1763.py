#include<cstdio>
#include<vector>
#include<map>
using namespace std;

char cake[30][30];
map<char, vector<int>> child;

void clear()
{
  for(int i=0; i<30; i++) {
    for(int j=0; j<30; j++) {
      cake[i][j] = 0;
    }
  }
}

void printCake(int r, int c)
{
  for(int i=0; i<r; i++) {
    for(int j=0; j<c; j++) {
      printf("%c", cake[i][j]);
    }
    putchar('\n');
  }
}

int main()
{
  int T, R, C;
  scanf("%d", &T);
  for(int t=1; t<=T; t++) {
    clear();
    char x;
    scanf("%d %d", &R, &C);
    for(int r=0; r<R; r++) {
      for(int c=0; c<C; c++) {
        scanf(" %c", &x);
        cake[r][c] = x;
      }
    }
    char ch;
    for(int c=0; c<C; c++) {
      bool got = false;
      int cur=0;
      for(int r=0; r<R; r++) {
        if(cake[r][c] != '?'){
          got = true;
          ch = cake[r][c];
        }
        int i=cur;
        while(i<R && got) {
          cake[i++][c] = ch;
          if(cake[i][c]!='?' && cake[i][c]!=ch){
            got=false;
            r=i-1;
            cur=i;
          }
        }
      }
    }
    for(int r=0; r<R; r++) {
      bool got = false;
      int cur=0;
      for(int c=0; c<C; c++) {
        if(cake[r][c] != '?'){
          got = true;
          ch = cake[r][c];
        }
        int i=cur;
        while(i<C && got) {
          cake[r][i++] = ch;
          if(cake[r][i]!='?' && cake[r][i]!=ch){
            got=false;
            c=i-1;
            cur=i;
          }
        }
      }
    }
    printf("Case #%d:\n", t);
    printCake(R, C);
  }
}
