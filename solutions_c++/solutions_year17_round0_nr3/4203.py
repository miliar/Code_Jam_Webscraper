#include <cstdio>
#include <queue>

using namespace std;

int main(){
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    int N,K,low=0;
    scanf("%d %d",&N,&K);
    priority_queue<int,vector<int> > pq;
    pq.push(N);
    for(int i=0;i<K-1;i++){
      int X = pq.top(); pq.pop();
      X--;
      if(X==0) continue;
      else if(X%2==0){
        pq.push(X/2);
        pq.push(X/2);
      }
      else{
        pq.push(X/2);
        pq.push(X/2+1);
      }
    }
    printf("Case #%d: ",t);
    int X = pq.top();
    X--;
    if(X%2==0)
      printf("%d %d\n",X/2,X/2);
    else
      printf("%d %d\n",X/2+1,X/2);
  }
}
