#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<set>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<cmath>

using namespace std;

int main(){
  char val[20];
  int T,K;
  scanf("%d", &T);
  int t = T;
  while(T--){
    scanf("%s", val);
    K = strlen(val);
    int ninefit = K;
    for(int i=K-1; i>=1; i--){
      if(val[i-1]<=val[i]) continue;
      for(int j=i; j<ninefit; j++) {
        val[j] = '9';
      }
      ninefit = i;
      if(val[i-1] >= '0'+1){
        val[i-1] -= 1;
      }
      else{
        while(i>1){
          i--;
          val[i] = '9';
          ninefit = i;
          if(val[i-1] >='0'+1){
            val[i-1] -= 1;
            break;
          }
        }
      }
    }
    int start = 0;
    for(; start<K; start++){
      if(val[start] != '0') break;
    }
    printf("Case #%d: ", t - T);
    for(int i=start; i<K; i++)
      printf("%c", val[i]);
    printf("\n");
  }
  return 0;
}
