#include <string.h>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <numeric>
#include <sstream>


int main(){
  long n,k,l,i,n2,n3;
  int t;
  char a[30]="";
  scanf(" %d", &t);
  
  
  for(int te=1;te<=t;++te){
    //std::priority_queue<long> mypq;  
    scanf(" %s", a);
    
    l=strlen(a);
    for(int p=0;p<l;p++){
      
    for(i=0;i<l-1;i++){
      if(a[i+1]<a[i]){
       a[i]--;
       for(int j=i+1;j<l;j++){a[j]='9';}
       break;
      }
      
    }
    
    if(i==l-1) break;
    }
    
    
    for(i=0;i<l;i++){
      if(a[i]!='0') break;
    }
    
    
    
    printf("Case #%d: %s\n", te, a+i);
    
    
    
    
    
  }
  
  
  return 0;
}

