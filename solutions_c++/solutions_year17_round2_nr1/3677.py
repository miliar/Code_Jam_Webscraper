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
    int D;
    vector<pair<int, int> > horses;
    scanf("%d %d", &D, &N);
    for(int i = 0; i < N; ++i){
      int a, b;
      scanf("%d %d", &a, &b);
      horses.push_back(make_pair(a,b));
    }
    /*

    sort(horses.begin(), horses.end());

    double d_left = horses[N-1].first;
    double speed = horses[N-1].second;
    
    for(int i = N-2; i >= 0; --i){
      double t = double(d_left - (double) horses[i].first) / double(horses[i].second - (double) speed);

      if(t <= 0){ // diverge
        d_left = horses[i].first;
        speed = horses[i].second;
      }else{
        d_left = horses[i+1].first;
        speed = horses[i+1].second;
        speed = min(horses[i+1].second, horses[i].second);
      }
    }
*/

    double annie_time = (double)(D-horses[0].first) / (double)(horses[0].second);

    for(int i = 0; i < N; ++i){
      annie_time = max((double)(D-horses[i].first) / (double)(horses[i].second), annie_time);




      //for(int j = i+1; j < N; ++j){


        /*
        double min_speed = INF;
        if(horses[i].second == horses[j].second) {
          double dist = max(horses[i].first, horses[j].first);
          annie_time = min(annie_time, double(D-dist)/(double)horses[i].second);
          continue;
        }

        //double t = double(horses[i].first - horses[j].first) / double(horses[j].second - horses[i].second);
        //if(t > 0){
          //double dist = min(horses[i].first, horses[j].first);
          //min_speed = min(horses[i].second, horses[j].second);
        double max_time = max(double(D-horses[i].first)/(double)horses[i].second, double(D-horses[j].first)/(double) horses[j].second);
        annie_time = max(annie_time, max_time);
        //}
        */
      //}
    }

    //double ttime = (((double) D)-d_left) / speed;
    //printf("%lf\n", ((double) D / ttime));
    printf("%lf\n", (double)D/annie_time);
  }
}
