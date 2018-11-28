#include <stdio.h>
#include <stdlib.h>
#include <unordered_map>
#include <queue>

#define TESTING if(false)
void doTestCase(std::vector<bool> &s, int K);
bool isGoal(std::vector<bool> &s);

int main(){
  int T;
  scanf("%d",&T);
  TESTING printf("T = %d\n",T);
  for (int i = 1; i<=T; i++){
    printf("Case #%d: ",i);
    int c;
    int K;

    c = getchar();

    std::vector<bool> state;

    while(c!=' '){
      if (c!='\n'){
        state.push_back(c=='+');
        TESTING printf("c is + %d\n", c=='+');
      }
      c = getchar();
    }

    scanf("%d", &K);
    doTestCase(state, K);
    printf("\n");
  }

  return EXIT_SUCCESS;
}

void doTestCase(std::vector<bool> &s, int K){
  int N = s.size();

  int inversions = 0;
  for (int i = 0; i<N-K+1; i++){
    if (!s[i]){
      inversions++;
      for (int j = 0; j<K; j++){
        s[i+j] = !s[i+j];
      }
    }
  }

  for (int i = 0; i<N;i++){
    if (!s[i]){
      printf("IMPOSSIBLE");
      return;
    }
  }


  printf("%d",inversions);
}

bool isGoal(std::vector<bool> &s){
  for (bool b: s){
    if (!b) return false;
  }

  return true;
}
