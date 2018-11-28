#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<string>
#include<set>
#include<queue>
#include<cstdlib>
#include<cmath>
#include<functional>

using namespace std;

class horse{
public:
  int K;
  int S;
  horse(){
    K=S=0;
  }
  horse(int k, int s){
    this->K=k;
    this->S=s;
  }
};

bool comp(horse a, horse b){
  return (a.K > b.K);
}

int main(){
  int t, T;
  int D, N;
  scanf("%d", &T);
  t = T;
  while(T--){
    int k, s;
    cin >> D >> N;
    priority_queue<horse, vector<horse>, std::function<bool(horse, horse)> > pq(comp);
    horse h = horse();
    for(int i=0; i<N; i++){
      scanf("%d %d", &k, &s);
      h = horse(k, s);
      pq.push(h);
    }
    double max = -1.0f;
    while(!pq.empty()){
      horse curr = pq.top();
      pq.pop();
      double value = (double)(D - curr.K) / (double)(curr.S);
      if(value > max){
        max = value;
      }
    }
    double c = (double)D/max;
    printf("Case #%d: %.6f\n", t - T, c);
  }
  return 0;
}
