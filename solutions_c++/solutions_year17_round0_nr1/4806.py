#include <cstdio>
#include <cstring>

using namespace std;

char s[1005];

int main(){
  int T; scanf("%d\n",&T);
  for(int i = 1; i <= T ; i++){
    int k;int ctr = 0;
    scanf("%s %d\n",s,&k);
    for(int j = 0 ; j < strlen(s)-k+1; j++){
      if(s[j] == '-'){
        ctr ++;
        for(int zhi = 0 ; zhi < k; zhi++){
          if(s[zhi+j] == '-'){
            s[zhi+j] = '+';
          } 
          else{
            s[zhi+j] = '-';
          }
          
        }
      }
    }
    bool yes = true;
    for(int j = strlen(s)-k+1; j< strlen(s);j++ ){
      if(s[j] == '-') yes = false;
    }
    if(yes) {
      printf("Case #%d: %d\n",i,ctr );
    }
    else{
      printf("Case #%d: IMPOSSIBLE\n",i);
    }
  }
  return 0;
}
