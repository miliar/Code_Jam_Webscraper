#include <stdio.h>
#include <cstring>

#define ll long long

char arr[20];

void run(int iter){
  scanf("%s\n", arr+1);
  int l = strlen(arr+1);

  for(int i=0;i<l-1;i++){
    if(arr[i+1]>arr[i+2]){
      while(arr[i+1]==arr[i])i--;
      arr[i+1]--;
      i++;
      for(;i<l;i++){
        arr[i+1] = '9';
      }
      break;
    }
  }
  printf("Case #%d: %s\n", iter, arr[1]=='0'?arr+2:arr+1);
}

int main(){
  int t;
  scanf("%d", &t);
  for(int i=0;i<t;i++){
    run(i+1);
  }
}
