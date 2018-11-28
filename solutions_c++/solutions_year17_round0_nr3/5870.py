#include <cstdio>
#include <algorithm>
#include <queue>
#include <map>
using namespace std;

typedef pair<long long,long long> ii;
long long N,K;
void run(){
  scanf("%lld %lld",&N,&K);

  map <long long, long long> M;
  priority_queue<ii> Q;
  ii now = ii(N,1), new_node;
  Q.push(now);
  while(K > 0){
    now = Q.top(); Q.pop();

    if(M.count(now.first)){
      now = ii(now.first, M[now.first]);
      M.erase(now.first);
    }

    printf("now = [%lld %lld] K = %lld\n",now.first,now.second,K);
    K -= now.second;
    if( K <= 0 ){
      if(now.first % 2) printf("%lld %lld\n",now.first/2,now.first/2);
      else printf("%lld %lld\n",now.first/2,now.first/2-1);
      break;
    }

    
    if(now.first % 2 == 1){
      if(now.first/2){
        Q.push(ii(now.first/2, now.second*2));
        if(!M.count(now.first/2)) M[now.first/2] = 0;
        M[now.first/2] += now.second * 2;
      }
    }else{
      if(now.first/2){
        Q.push(ii(now.first/2, now.second));
        if(!M.count(now.first/2)) M[now.first/2] = 0;
        M[now.first/2] += now.second;
      }
      if(now.first/2-1 > 0){
        Q.push(ii(now.first/2-1, now.second));
        if(!M.count(now.first/2-1)) M[now.first/2-1] = 0;
        M[now.first/2-1] += now.second;
      }
    }

  }
}

int A[1005];
int B[1005];
void run_slow(){
  scanf("%lld %lld",&N,&K);
  memset(A,0,sizeof A);
  memset(B,0,sizeof B);
  A[0] = A[(int)N+1] = 1;
  B[0] = 1;
  for(int i=1;i<=(int)N+1;i++) B[i] = B[i-1] + A[i];

  for(int i=1;i<=(int)K;i++){
    int minLR = 0, maxLR = 0;
    int idbest = -1;
    for(int j=1;j<=(int)N;j++){
      if(A[j]) continue;

      // findRight
      int idright = lower_bound(&B[j+1], &B[(int)N+2], B[j]+1) - B;
      // findLeft
      int idleft = lower_bound(B, &B[j], B[j]) - B;
      
      int valleft = j - idleft - 1;
      int valright = idright - j - 1;
      // printf("valleft = %d %d\n",valleft,valright);
      if(min(valleft,valright) > minLR){
        minLR = min(valleft,valright);
        maxLR = max(valleft, valright);
        idbest = j;
      }else if(min(valleft, valright) == minLR){
        if(max(valleft, valright) > maxLR){
          maxLR = max(valleft,valright);
          idbest = j;
        }
      }
    }
    A[idbest] = 1;
    for(int j=idbest;j<=(int)N+1;j++) B[j] = B[j-1] + A[j];
    if(i == (int)K)printf("%d %d\n",maxLR,minLR);

    //    printf("[%d]",i);
  }
}

int main(){
  //freopen("C-small-1-attempt0.in","r",stdin);
  int T;
  scanf("%d",&T);
  for(int i=1;i<=T;i++){
    printf("Case #%d: ",i);
    run_slow();
  }
}
