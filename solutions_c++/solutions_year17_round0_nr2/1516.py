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
    char N[20];
    int fg, i, j, len;
    printf("Case #%d: ", ++test);
    fprintf(stderr, "r=%d\n", TEST);
    rd(N);
    len = strlen(N);
    for(i=0;i<len;i++){
      N[i] -= '0';
    }
    for(;;){
      fg = 0;
      for(i=1;i<len;i++){
        if(N[i-1] > N[i]){
          N[i-1]--;
          {
            int Lj4PdHRW;
            for(Lj4PdHRW= i;Lj4PdHRW< (len-1) + 1;Lj4PdHRW++){
              N[Lj4PdHRW] = 9;
            }
          }
          fg = 1;
          break;
        }
      }
      if(!fg){
        break;
      }
    }
    if(N[0]==0){
      len--;
      {
        int KL2GvlyY;
        for(KL2GvlyY= 0;KL2GvlyY< (len-1) + 1;KL2GvlyY++){
          N[KL2GvlyY] = N[KL2GvlyY - (0) + (1)];
        }
      }
      N[len] = '\0';
    }
    {
      int Q5VJL1cS;
      for(Q5VJL1cS= 0;Q5VJL1cS< (len-1) + 1;Q5VJL1cS++){
        N[Q5VJL1cS] += '0';
      }
    }
    wt_L(N);
    putchar_unlocked('\n');
  }
  return 0;
}
// cLay varsion 20170408-3 [beta]

// --- original code ---
// {
//   int test = 0, TEST;
//   rd(TEST);
//   while(TEST--){
//     printf("Case #%d: ", ++test);
//     fprintf(stderr, "r=%d\n", TEST);
// 
//     char N[20];
//     int i, j, len, fg;
// 
//     rd(N);
//     len = strlen(N);
// 
//     rep(i,len) N[i] -= '0';
//     for(;;){
//       fg = 0;
//       rep(i,1,len) if(N[i-1] > N[i]){
//         N[i-1]--;
//         N[i..len-1] = 9;
//         fg = 1;
//         break;
//       }
//       if(!fg) break;
//     }
// 
//     if(N[0]==0){
//       len--;
//       N[0..len-1] = N[1..];
//       N[len] = '\0';
//     }
//     N[0..len-1] += '0';
//     wt(N);
//   }
// }
