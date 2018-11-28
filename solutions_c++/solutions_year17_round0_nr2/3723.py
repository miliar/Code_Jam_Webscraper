#include <stdio.h>
#include <stdint.h>
#include <string.h>
int judge(uint64_t n){
  uint64_t pre,now,i=1;
  pre=n%10;
  n=n/10;
  while(n>0){
    now = n%10;
    if(pre < now){
      return -1*i;
    }
    pre=now;
    n=n/10;
    i++;
  }
  return 1;
}

int main(){
#ifdef small
  int T,i;
  uint64_t N;
  scanf("%d",&T);
  for(i=0;i<T;i++){
    scanf("%ld",&N);
    while(judge(N)<0){
      N=N-1;
      //printf("%ld\n",N);
    }
    printf("Case #%d: %ld\n",i+1,N);
  }
#else
  int T,i,tidy,len,j;
  char s[20];
  scanf("%d",&T);
  for(i=0;i<T;i++){
    scanf("%s",s);
    len=strlen(s);
    tidy=0;
    while(tidy==0){
      tidy=1;
      for(j=0;j<len-1;j++){
        if(s[j]>s[j+1] ){
          s[j]-=1;
          j++;
          while(j<len){
          
            s[j]='9';
            j++;
          }
          tidy=0;
          break;
        }
      }
    }
    for(j=0;j<len;j++){
      if(s[j]!='0') break;
    }
    printf("Case #%d: ",i+1);
    for(;j<len;j++){
      printf("%c",s[j]);
    }
    printf("\n");
  }


#endif
  


  return 0;
}
