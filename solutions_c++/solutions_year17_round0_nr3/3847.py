#include <stdio.h>
#include <stdint.h>
#include <math.h>
typedef struct aaa{
  int many;
  int n;
}s_set;
typedef struct bbb{
  int number;
  int n1,n2;
}s_result;
void printstate(s_set odd,s_set even,s_result big){
  printf("ODD: n=%d, many=%d\n", odd.n, odd.many);
  printf("EVEN: n=%d, many=%d\n", even.n, even.many);
  printf("BIG: many=%d,n1=%d,n2=%d\n", big.number, big.n1,big.n2);
  printf("\n");
}


int main(){
  int T,i,j,floor,temp;
  uint64_t N,K,offset;
  s_set odd,even;
  s_result big,small;
  scanf("%d",&T);
  for(i=0;i<T;i++){
    scanf("%ld %ld",&N,&K);
    floor=(int)(log(K)/log(2));
    offset=(uint64_t)(K-pow(2,floor));
    //printf("%d %ld\n",floor,offset);
    if( (N&1) ==0){
      even.n=N;
      even.many=1;
      odd.many=0;
      odd.n=4;
    }
    else{
      odd.n=N;
      odd.many=1;
      even.many=0;
      even.n=0;
    }
    //printstate(odd,even,big);
    for(j=0;j<=floor;j++){
      if( ((odd.n/2) & 1) == 0  && ( ((even.n/2) & 1)==0))
      {//4 6 8 10  
        if(even.many>0){
          odd.n=even.n/2-1;
          even.n=odd.n+1;
        }else{
          even.n=odd.n/2;
          odd.n=even.n-1;
        }
        big.number=odd.many;
        big.n1=even.n;
        big.n2=even.n;
        small.n1=even.n;
        small.n2=odd.n;
        //printstate(odd,even,big);
        temp=odd.many;
        odd.many=even.many;
        even.many=even.many+temp*2;
        
      }
      else if( (((odd.n/2) & 1) == 0)  && ( ((even.n/2) & 1)==1))
      {
        if(even.many>0){
          odd.n=even.n/2;
          even.n=odd.n-1;
        }else{
          even.n=odd.n/2;
          odd.n=even.n+1;
        }
        big.number=even.many;
        big.n1=odd.n;
        big.n2=even.n;
        small.n1=even.n;
        small.n2=even.n;


        temp=odd.many;
        odd.many=even.many;
        even.many=even.many+temp*2;
      
      }
      else if( (((odd.n/2) & 1) == 1)  && ( ((even.n/2) & 1)==0))
      {
        if(even.many>0)
        {
          even.n=even.n/2;
          odd.n=even.n-1;
        }else{
          even.n=odd.n/2+1;
          odd.n=even.n-1;
        }
        big.number=even.many;
        big.n1=even.n;
        big.n2=odd.n;
        small.n1=odd.n;
        small.n2=odd.n;
        odd.many=even.many+odd.many*2;
        //printstate(odd,even,big);
      
      }
      else if( (((odd.n/2) & 1) == 1)  && ( ((even.n/2) & 1)==1))
      {
        if(even.many>0)
        {
          even.n=even.n/2-1;
          odd.n=even.n+1;
        }else{
          even.n=odd.n/2-1;
          odd.n=even.n+1;
        }
        big.number=odd.many;
        big.n1=odd.n;
        big.n2=odd.n;
        small.n1=odd.n;
        small.n2=even.n;

        odd.many=even.many+odd.many*2;
        
      }
      //printstate(odd,even,big);

    }
    //printf("Big number=%d,offset=%ld\n",big.number,offset);
    printf("Case #%d: ",i+1);
    if( big.number>=offset+1 && big.number>0){
      printf("%d %d\n",big.n1,big.n2);
    }else{
      printf("%d %d\n",small.n1,small.n2);
    }


  
  }

  return 0;
}
