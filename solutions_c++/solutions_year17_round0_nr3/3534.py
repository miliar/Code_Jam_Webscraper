#include <string.h>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
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
  long n,k,kmax,kmin,n1,n2,n3;
  int t;
  //long a[1000002];
  scanf(" %d", &t);
  
  
  for(int te=1;te<=t;++te){
    std::priority_queue<long> mypq;  
    scanf(" %ld %ld", &n, &k);
    //while(!mypq.empty()){mypq.pop();}
    mypq.push(n);
    
    
    for(long i=0;i<k;i++){
      n1=mypq.top();
      n2=n1/2;
      n3=n2 + (n1%2);
      n3--;
      //printf(" hello%ld %ld \n", n2,n3);
      mypq.pop();
      mypq.push(n2);
      mypq.push(n3);
      
      
    }
    
    printf("Case #%d: %ld %ld\n", te, n2, n3);
    
    
    
    
    
  }
  
  
  return 0;
}

