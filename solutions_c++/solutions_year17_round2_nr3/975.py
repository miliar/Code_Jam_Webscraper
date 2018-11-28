#include "bits/stdc++.h"

using namespace std;

using ll = long long;
using dd = double;

using VL = vector<ll>;
using VVL = vector<VL>;

using VD = vector<dd>;
using VVD = vector<VD>;

int main() {
  freopen("CS.in", "r", stdin);
  freopen("CS.out", "w+", stdout);

  int tcase,cas =1 ;

  int n,q;
  cin>>tcase;

  while(tcase--) {
    cin>>n>>q;

    VVL dist(n, VL(n, -1));
    vector<pair<ll,ll>> vi(n);

    for(auto &p: vi) {
      cin>>p.first>>p.second;
    }

    for(int i = 0 ; i<n ; i++) {
      for(int j = 0 ; j<n ; j++) {
        cin>>dist[i][j];
      }
    }

    vector<pair<ll,ll>> vq(q);

    for(auto &p: vq) {
      cin>>p.first>>p.second;
    }

    // floyed wasrshal 

    for(int k = 0 ; k<n ; k++) {
      for(int i = 0 ; i<n ; i++) {
        for(int j =0 ; j<n ; j++) {
          if(dist[i][k] == -1 || dist[k][j] == -1) continue;
          if(dist[i][j] == -1) {
            dist[i][j] = dist[i][k] + dist[k][j];
          } else {
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
          }
        }
      }
    }

    VVD ct(n, VD(n, -1));

    for(int i = 0 ; i<n ; i++) {
      for(int j = 0 ; j<n ; j++) {
        if(dist[i][j] == -1 || dist[i][j] > vi[i].first) continue;
        ct[i][j] = (dd)dist[i][j] / (vi[i].second*1.0);
      }
    }

    for(int k = 0 ; k<n ; k++) {
      for(int i = 0 ; i<n ; i++) {
        for(int j = 0; j<n ; j++) {
          if(ct[i][k] < 0 || ct[k][j] < 0) continue;
          if(ct[i][j] < 0) {
            ct[i][j] = ct[i][k] + ct[k][j];
          } else ct[i][j] = min(ct[i][j], ct[i][k] + ct[k][j]);
        }
      }
    }

    dd mx = 0;
    int f = 0;
    printf("Case #%d:",cas++);
    for(auto &p: vq) {
      printf(" %.6lf", ct[p.first-1][p.second-1]);
    }
    printf("\n");
  }
  return 0;
}