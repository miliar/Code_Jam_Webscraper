#include <stdio.h>
#include <string.h>
int main(){
  int T,i,K,j,m,flip;
  char cake[1001];
  
  scanf("%d",&T);
  
  for(i=0;i<T;i++){
    scanf("%s",cake);
    scanf("%d",&K);
    flip=0;
    //printf("%d,%d\n",strlen(cake),K);
    for(j=0; j<strlen(cake)-K+1 ;j++){
      
      if(cake[j]=='-'){
        for(m=j;m<j+K;m++){
          if(cake[m]=='-'){
            cake[m]='+';//printf("%c ",cake[m]);
          }else{
            cake[m]='-';//printf("%c ", cake[m]);
          }
        
        }
        //printf("\n%d,%s\n",j,cake);
        flip++;
      }
    }
    for(;j<strlen(cake);j++){
      if(cake[j]=='-'){
        flip = -1;
        break;
      }
    }
    printf("Case #%d: ",i+1);
    if(flip==-1){
      printf("IMPOSSIBLE\n");
    }else{
      printf("%d\n",flip);
    }
  }


  return 0;
}
