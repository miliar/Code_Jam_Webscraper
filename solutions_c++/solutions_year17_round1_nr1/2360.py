#include <stdio.h>
#include <stdint.h>
#define U64 uint64_t
#define U32 uint32_t
#define S64 int64_t
#define S32 int32_t

int main(){
  U32 T,tt,k,m,n,R,C;
  int namemap[26],i,j,start;
  char name,result[26][26],re;
  scanf("%d",&T);
  for(tt=0;tt<T;tt++){
    scanf("%d %d\n",&R,&C);
    /*for(i=0;i<R;i++){
      for(j=0;j<C;j++){
        namemap[i][j]=0;
      }
    }*/
    
    for(i=0;i<R;i++){
      for(j=0;j<C;j++){
        scanf("%c",&name);
        /*if(name!='?'){
          //namemap[(name-'A')]=1;
          re=name;
        }*/
        result[i][j]=name;
      }
      scanf("\n");
    }



    for(i=0;i<R;i++){
      j=0;start=0;
      while(j<C){
        
        while(result[i][j]=='?' && j<C){
          j++;
        }
        if(j<C){
          re=result[i][j];
        }else if(start>0){
          re=result[i][start-1];
        }else{
          re='?';
        }
          for(m=start;m<j;m++){
            result[i][m]=re;
          }
        
          
        
        while(result[i][j]!='?' && j<C){
          j++;
        }
        start=j;
      }
    }

    for(i=0;i<R;i++){
      if(result[i][0]=='?'){
        for(m=i+1;m<R;m++){
          if(result[m][0]!='?')break;
        }
        if(m>=R){
          for(m=i-1;m>=0;m--){
            if(result[m][0]!='?')break;
          }
        }
        for(j=0;j<C;j++){
          result[i][j]=result[m][j];
        }
      }
    }

    printf("Case #%d:\n",tt+1);
    for(i=0;i<R;i++){
      for(j=0;j<C;j++){
        printf("%c",result[i][j]);
      }
      printf("\n");
      
    }
  }


  return 0;
}
