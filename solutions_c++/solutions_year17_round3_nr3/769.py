#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;
typedef pair<pair<int, int>, int> iii;
typedef vector<ii> vii;
typedef set<int> si;
typedef map<string, int> msi;

#define I18F 1000000000000000000 // 10^18
#define INF 2139062143
#define MEMSET_INF 127 // about 2B
#define MEMSET_HALF_INF 63 // about 1B

int N, _T;

int main(){
  scanf("%d", &_T);
  for(int _t = 0; _t < _T; ++_t){
    printf("Case #%d: ", _t + 1);
    int N, K;
    scanf("%d %d", &N, &K);
    double U;
    scanf("%lf", &U);
    vector<double> energies;
    priority_queue<double, vector<double>, greater<double> > all;
    for(int i = 0; i < N; ++i){
      double a;
      scanf("%lf", &a);
      energies.push_back(a);
      all.push(a);
    }
    sort(energies.begin(), energies.end());
    int ct = 0;
    double cur = energies[0];
    for(int i = 0; i < energies.size(); ++i){
      if(U == 0) break;
      double req = ct * (energies[i] - cur);
      if(U < req){
        for(int j = 0; j < i; ++j) energies[j] += U/(double)ct;
        U = 0;
      }else{
        for(int j = 0; j < i; ++j) energies[j] = energies[i];
        U -= req;
        cur = energies[i];
        ct++;
      }
    }
    if(U > 0){
      for(int j = 0; j < energies.size(); ++j) energies[j] += U/(double) energies.size();
    }

    double p = 1;
    for(int i = 0; i < energies.size(); ++i) p *= energies[i];

    printf("%lf\n", p);
  }
}
