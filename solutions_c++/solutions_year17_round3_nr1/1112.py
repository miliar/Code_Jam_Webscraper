#include <vector>
#include <utility>
#include <string>
#include <iostream>
#include <map>
#include <queue>
#include <cstdio>
using namespace std;
const double PI= 3.14159265358979323846;

int main() {
  int T;
  cin >> T;
  for (int tc=1; tc<=T; tc++ ){
    int N, K;
    cin >> N >> K;
    vector<pair<int, int> > in(N);
    vector<long long> rad(N);
    vector<long long> height(N);
    for(int i=0; i<N; i++) {
      int r, h;
      cin >> r >> h;
      in[i] = make_pair(-r, -h);
    }
    sort(in.begin(), in.end());
    for(int i=0; i<N; i++) {
      in[i] = make_pair(-in[i].first, -in[i].second);
      rad[i] =in[i].first;
      height[i] = 2LL*in[i].first*in[i].second;
    }
    vector<pair<long long, long long> > Q;
    for(int i=0; i<K; i++) {
      Q.push_back(make_pair(rad[i],height[i]));
    }
    for(int i=K; i<N; i++) {
      long long m = 1e18;
      int idx = 0;
      for(int j=0; j<K; j++) {
        if(j==0) {
          long long nxt = K==1? rad[i] : Q[1].first;
          if(m > ((Q[0].first*Q[0].first)-(nxt*nxt) + Q[0].second)) {
            m = (Q[0].first*Q[0].first)-(nxt*nxt) + Q[0].second;
            idx = j;
          }
        }else {
          if(m > Q[j].second) {
            m = Q[j].second;
            idx = j;
          }
        }
      }
      if(m >= height[i]) {
        continue;
      }
      Q.erase(Q.begin() + idx);
      Q.push_back(make_pair(rad[i], height[i]));
    }
    double res =(double)Q[0].first*(double)Q[0].first*PI;
    for(int i=0; i<K; i++) {
      res+= (double)Q[i].second*PI;
    }
    printf("Case #%d: %.8lf\n", tc, res);
  }

}


