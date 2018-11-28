#include <cstdio>
#include <algorithm>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  for(int x=0;x<T;x++){
    printf("Case #%d: ",x+1);
    int d,n;
    scanf("%d %d",&d,&n);
    double longest = 0;
    for(int i=0;i<n;i++){
      int k,s;
      scanf("%d %d",&k,&s);
      if((d-k) / (double)s > longest)
        longest = (d-k) / (double)s;
    }
    printf("%lf\n",d / longest);
  }
}
