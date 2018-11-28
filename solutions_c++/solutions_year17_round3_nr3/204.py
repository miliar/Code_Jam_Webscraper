#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <limits>
#include <numeric>
#include <string>
#include <tuple>
#include <utility>
#include <vector>
using namespace std;

int main() {
  int cases;
  cin >> cases;
  for (int ca = 1; ca <= cases; ++ca) {
    int n;
    int k;
    cin >> n >> k;
    double u;
    cin>>u;
    vector<double> prob;
    for (int i=0;i<n;++i) {
      double p;
      cin>>p;
      prob.push_back(p);
    }
    sort(prob.begin(), prob.end());
    int split=0;
    double cum=0;
    while(split<n) {
      cum += split*(prob[split]-prob[split-1]);
      if(u<cum) {
        break;
      }
      ++split;
    }
    double ans = 1.0;
    cum=u;
    for(int i=0;i<split;++i){
      cum +=prob[i];
    }
    cum /= split;
    ans = pow(cum,split);
    for(int i=split;i<n;++i) {
      ans*=prob[i];
    }
    if (1<ans) {
      ans=1;
    }
    printf("Case #%d: %f\n", ca, ans);
  }
  return 0;
}
