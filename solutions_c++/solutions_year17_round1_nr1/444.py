#include<bits/stdc++.h>
using namespace std;
void rd(int &x){
  int k, m=0;
  x=0;
  for(;;){
    k = getchar_unlocked();
    if(k=='-'){
      m=1;
      break;
    }
    if('0'<=k&&k<='9'){
      x=k-'0';
      break;
    }
  }
  for(;;){
    k = getchar_unlocked();
    if(k<'0'||k>'9'){
      break;
    }
    x=x*10+k-'0';
  }
  if(m){
    x=-x;
  }
}
void rd(char c[]){
  int i, sz=0;
  for(;;){
    i = getchar_unlocked();
    if(i!=' '&&i!='\n'&&i!='\r'&&i!='\t'&&i!=EOF){
      break;
    }
  }
  c[sz++] = i;
  for(;;){
    i = getchar_unlocked();
    if(i==' '||i=='\n'||i=='\r'||i=='\t'||i==EOF){
      break;
    }
    c[sz++] = i;
  }
  c[sz]='\0';
}
void wt_L(int x){
  char f[10];
  int m=0, s=0;
  if(x<0){
    m=1;
    x=-x;
  }
  while(x){
    f[s++]=x%10;
    x/=10;
  }
  if(!s){
    f[s++]=0;
  }
  if(m){
    putchar_unlocked('-');
  }
  while(s--){
    putchar_unlocked(f[s]+'0');
  }
}
void wt_L(const char c[]){
  int i=0;
  for(i=0;c[i]!='\0';i++){
    putchar_unlocked(c[i]);
  }
}
int main(){
  int TEST, test=0;
  rd(TEST);
  while(TEST--){
    char mp[30][30];
    int X, Y, i, j, k;
    printf("Case #%d:\n", ++test);
    fprintf(stderr, "r=%d\n", TEST);
    rd(X);
    rd(Y);
    {
      int Lj4PdHRW;
      for(Lj4PdHRW=0;Lj4PdHRW<X;Lj4PdHRW++){
        rd(mp[Lj4PdHRW]);
      }
    }
    for(i=1;i<X;i++){
      for(j=0;j<Y;j++){
        if(mp[i][j]=='?'){
          mp[i][j] = mp[i-1][j];
        }
      }
    }
    for(i=X-1;i;i--){
      for(j=0;j<Y;j++){
        if(mp[i-1][j]=='?'){
          mp[i-1][j] = mp[i][j];
        }
      }
    }
    for(i=0;i<X;i++){
      for(j=1;j<Y;j++){
        if(mp[i][j]=='?'){
          mp[i][j] = mp[i][j-1];
        }
      }
    }
    for(i=0;i<X;i++){
      for(j=Y-1;j;j--){
        if(mp[i][j-1]=='?'){
          mp[i][j-1] = mp[i][j];
        }
      }
    }
    {
      int KL2GvlyY;
      for(KL2GvlyY=0;KL2GvlyY<X;KL2GvlyY++){
        wt_L(mp[KL2GvlyY]);
        putchar_unlocked('\n');
      }
    }
  }
  return 0;
}
// cLay varsion 20170413-1 [beta]

// --- original code ---
// {
//   int test = 0, TEST;
//   rd(TEST);
//   while(TEST--){
//     printf("Case #%d:\n", ++test);
//     fprintf(stderr, "r=%d\n", TEST);
// 
//     int X, Y;
//     char mp[30][30];
//     int i, j, k;
//     
//     rd(X,Y,mp(X));
// 
//     REP(i,1,X)       rep(j,Y)         if(mp[i][j]=='?')   mp[i][j] = mp[i-1][j];
//     for(i=X-1;i;i--) rep(j,Y)         if(mp[i-1][j]=='?') mp[i-1][j] = mp[i][j];
//     rep(i,X)         REP(j,1,Y)       if(mp[i][j]=='?')   mp[i][j] = mp[i][j-1];
//     rep(i,X)         for(j=Y-1;j;j--) if(mp[i][j-1]=='?') mp[i][j-1] = mp[i][j];
// 
//     wtLn(mp(X));
//   }
// }
