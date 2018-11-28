#include <cstdio>
#include <queue>

using namespace std;

typedef priority_queue< int, vector<int>, less<int> > pq;
int main(){
  int T; scanf("%d\n",&T);
  for(int i = 1; i <= T; i++){
    pq res; int N, k; scanf("%d %d\n",&N,&k);
    int shi = 1; res.push(N);
    int L , R,y,z;
    while(shi <= k){
      int temp = res.top(); res.pop();
      if(temp%2 ==1){
        L = (temp -1)/2 ;
        R = (temp -1)/2;
      }
      else{
        L = temp/2 -1 ;
        R = temp/2 ;
      }
      res.push(L); res.push(R);
      y = max(L,R);
      z = min(L,R);
      shi++;
    }
    printf("Case #%d: %d %d\n",i,y,z );
  }
  
  return 0;
}
