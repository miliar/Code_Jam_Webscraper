#include <stdio.h>
#include <stdint.h>
#define U64 uint64_t
#define U32 uint32_t
#define S64 int64_t
#define S32 int32_t

int main(){
  U32 T,tt,i,j,k,m,n,R,C,N[1001],S[1001];
  U32 pathlong,many;
  long double remainhour;
  long double max=-1;
  scanf("%d\n",&T);
  
  for(tt=0;tt<T;tt++){
    /*if(tt!=39){
      scanf("%d %d\n",&pathlong,&many);
      for(i=0;i<many;i++){
        scanf("%d %d\n",&N[i],&S[i]);
      }
      continue;
    }*/
    
    
    scanf("%d %d\n",&pathlong,&many);
    //printf("%d %d\n",pathlong,many);
    max=-1;
    for(i=0;i<many;i++){
      scanf("%d %d\n",&N[i],&S[i]);
      //printf("%d %d\n",N[i],S[i]);
      remainhour=(pathlong-(long double)N[i])/(long double)S[i];
      if((remainhour-max)>0)
        max=remainhour;
    }
    
    printf("Case #%d: %llf\n",tt+1,(double)((double)pathlong)/max);
  }


  return 0;
}
