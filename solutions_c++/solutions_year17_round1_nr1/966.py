#include<cstdio>
#include<iostream>
using namespace std;

char tab[30][30];
int m,n;

void flood(int i, int j, int c) {
  if(tab[i][j]!='?')
    return;
  tab[i][j] = c;
  flood(i-1,j,c);
  flood(i,j-1,c);
}


int main(){
  int t;
  cin >> t;
  for(int c=1;c<=t;c++) {
    int m,n;
    cin >> m >> n;
    for(int i=0;i<=m+1;i++)
      for(int j=0;j<=n+1;j++)
        tab[i][j]='#';
    for(int i=1;i<=m;i++)
      for(int j=1;j<=n;j++)
        scanf(" %c", &tab[i][j]);
    for(int i=1;i<=m;i++) {
      char last = '#';
      for(int j=1;j<=n;j++)
        if(tab[i][j]!='?') {
          flood(i-1,j,tab[i][j]);
          flood(i,j-1,tab[i][j]);
          last = tab[i][j];
        }
      if(last!='#') {
          flood(i,n,last);
      }
    }
    for(int i=1;i<=m;i++)
      for(int j=1;j<=n;j++)
        if(tab[i][j]=='?')
          tab[i][j]=tab[i-1][j];

    printf("Case #%d:\n", c);
    for(int i=1;i<=m;i++){
      for(int j=1;j<=n;j++)
        printf("%c", tab[i][j]);
      printf("\n");
    }
  }
  return 0;
}
