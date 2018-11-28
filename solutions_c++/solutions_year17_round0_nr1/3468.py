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

char a[1010];

int main(){
  int t,k,start,count,poss;
  scanf(" %d", &t);
  for(int te=1;te<=t;te++){

    scanf(" %s %d", a, &k);
    //printf(" %s,%d\n",a,k);
    start=0;count=0;poss=1;
    int len=strlen(a);
    for(int i=0;i<len;i++){
      //printf("%s\n",a);
      int l;    
      for(l=start;l<len;l++){
        if(a[l]=='-'){ start=l; break;}
      }

      if(l==len) break;
      if(start+k-1 >=len){poss=0;break;}


      for( l=0;l<k;l++){
        if(a[l+start]=='+') a[start+l]='-';
        else a[l+start]='+';
      }
      count++;

      // for(int l=0;l<k;l++){

      // }


      i=start; //update i to start
    }
    //print the count

    if(poss)
    printf("Case #%d: %d\n", te,count);
    else printf("Case #%d: IMPOSSIBLE\n",te);


  }







  return 0;
}


