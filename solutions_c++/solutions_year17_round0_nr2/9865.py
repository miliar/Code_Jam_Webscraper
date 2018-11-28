#include<cstdio>
#include<algorithm>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<map>
#include<queue>
#include<cstdlib>
#include<cstring>
#include<string>
#include<set>

using namespace std;

typedef long long int huge;
const int inf = 0x3f3f3f3f;
const huge maxn = 1000000000000000000; //10ˆ8
char number[32];
int size;

int verify(){
  int maximum;
  //printf("%s\n", number);

  maximum = (int) number[0];
  //maximum = (int) number[size-1];
  //printf("maximum %d number %s\n", maximum, number);
  //for(int i = size-1; i >= 0; ++i){
  for(int i = 1; number[i]; ++i){
    if(maximum > (int) number[i])
      return 0;
    else
      maximum = (int) number[i];
  }
  return 1;
}

int main(){
  int t, count=0;
  huge n;

  scanf("%d", &t);

  while(t--){
    scanf("%lld", &n);
    size = sprintf(number, "%lld", n);
    //printf("blah\n");

    while(!verify()){
      n--;
      size = sprintf(number, "%lld", n);
    }

    printf("Case #%d: %lld\n", ++count, n);
  }
  return 0;
}
