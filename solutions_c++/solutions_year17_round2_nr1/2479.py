//Author: Andres-Felipe Ortega-Montoya
//A.cpp
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int INF = 1 << 30;

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  ll TC;
  cin >> TC;
  for(int t = 1; t <= TC; ++t){
    double goal, maxtime = -INF;
    ll h;
    cin >> goal >> h;
    for(ll i=0; i < h; ++i){
      double pos, speed;
      cin >> pos >> speed;
      //cout << (goal-pos)/speed << "\n";
      maxtime = max(maxtime, (goal-pos)/speed);
    }
    //cout << maxtime;
    cout << "Case #" << t << ": " << fixed << setprecision(6) << goal/maxtime << "\n";
  }
}
