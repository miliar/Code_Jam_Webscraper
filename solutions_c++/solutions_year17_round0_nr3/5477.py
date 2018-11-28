#include <stdio.h>
#include <vector>
#include <assert.h>

#define TESTING false
void doTestCase(long long N, long long K);

int main(){
  int T;
  scanf("%d",&T);

  long long N,K;

  for (int i = 1; i<=T; i++){
    scanf("%lld %lld",&N,&K);

    printf("Case #%d: ",i);
    doTestCase(N,K);
    if (i!=T) printf("\n");
  }
}

void doTestCase(long long N, long long K){
  std::vector<bool> isTaken;
  std::vector<int> leftTally;
  std::vector<int> rightTally;

  for (int i = 0; i<N; i++){
    isTaken.push_back(false);
  }

  int min = -1;
  int max = -1;
  int best = -1;
  for (int j = 0; j<K; j++){
    if (TESTING)printf(" doing person %d\n",j);

    leftTally.clear();
    rightTally.clear();

    leftTally.push_back(0);
    for (int i = 0;i<N; i++){
      if (isTaken[i]){
        leftTally.push_back(0);
      } else{
        leftTally.push_back(leftTally[i]+1);
      }

      if (TESTING) printf("   added %d to leftTally\n",leftTally[i+1]);
    }

    rightTally.push_back(0);
    for (int i = 0;i<N; i++){
      if (isTaken[N-i-1]){
        rightTally.push_back(0);
      } else{
        rightTally.push_back(rightTally[i]+1);
      }
      if (TESTING) printf("   added %d to rightTally\n",rightTally[i+1]);
    }

    best = -1;
    min = -1;
    max = -1;

    for (int i = 0; i<N; i++){
      if (isTaken[i]) continue;
      int lS = leftTally[i+1]-1;
      int rS = rightTally[N-i]-1;
      int iMin = std::min(lS,rS);
      int iMax = std::max(lS,rS);
      if (TESTING) printf("   position %d has a min of %d and a max of %d (ls = %d rs = %d)\n",
      i,iMin, iMax, lS, rS);
      if (iMin>min || (iMin==min && iMax>max)){
        min = iMin;
        max = iMax;
        best = i;
      }
    }
    isTaken[best] = true;

    if (TESTING) printf("  best is at %d with min = %d, max = %d \n",best,min,max);
  }
  printf("%d %d",max,min);
}
