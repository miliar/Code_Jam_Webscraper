#include <vector>
#include <utility>
#include <string>
#include <iostream>
#include <map>
#include <cstdio>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; tc++ ){
    int N, K;
    cin >> N >> K;
    double U;
    cin >> U;
    vector<double> prob(N);
    for(int i=0; i<N; i++) {
      cin >> prob[i];
    }
    sort(prob.begin(), prob.end());
    bool flag = false;
    for(int i=1; i<N; i++) {
      double sm = 0.0;
      for(int j=0; j<i; j++) {
        double diff = prob[i]-prob[j];
        sm += diff;
      }
      if(U >= sm) {
        for(int j=0; j<i; j++) {
          double diff = prob[i]-prob[j];
          prob[j] += diff;
          U-=diff;
        }
      }else {
        double halt = U/(double)i;
        for(int j=0; j<i; j++) {
          prob[j] += halt;
          U-=halt;
        }
        flag = true;
      }
      if(flag) break;
    }
    double sum = 0.0;
    double res = 1.0;
    if(flag) {
      for(int i=0; i<N; i++) {
        res*=prob[i];
      }
      printf("Case #%d: %.8f\n", tc, res);
      continue;
    }
    for(int i=0; i<N; i++) {
      sum += 1.0-prob[i];
    }
    if(U >= sum) {
      for(int i=0; i<N; i++)
      {
        prob[i] = 1.0;
        res*=prob[i];
      }
    }else {
      double halt = U/(double)N;
      for(int i=0; i<N; i++) {
        prob[i] += halt;
        U-=halt;
        res*=prob[i];
      }
    }
    printf("Case #%d: %.8f\n", tc, res);
  }

}


