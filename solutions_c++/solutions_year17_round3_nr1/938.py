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
#define PI 3.14159265358979323846

int N, _T;

int main(){
  scanf("%d", &_T);
  for(int _t = 0; _t < _T; ++_t){
    printf("Case #%d: ", _t + 1);
    int K;
    scanf("%d%d", &N, &K);
    vector<pair<double, double> > heights;
    for(int i = 0; i < N; ++i){
      int a, b;
      scanf("%d%d", &a, &b);
      double sa = (double) b * 2.0 * PI * (double) a;
      heights.push_back(make_pair(sa, (double) a));
    }
    // printf("size:%d\n", heights.size());

    sort(heights.begin(), heights.end());
    reverse(heights.begin(), heights.end());
    /*
    for(int i = 0; i < N; ++i){
      printf("%d: %lf, %lf\n", i, heights[i].second, heights[i].first);
    }
    */

    double best = -1;
    for(int i = 0; i < N; ++i){
      double base = heights[i].first + (double)(heights[i].second) * double(heights[i].second) * PI;
      int ct = 1;
     // printf("for %d!\n", i);
      for(int j = 0; j < N; ++j){
        if(i == j) continue;
        if(ct == K) break;
        if(heights[j].second > heights[i].second) continue;
        //printf("use %d!\n", j);
        base += heights[j].first;
        ct++;
      }
      if(ct < K) continue;
      //printf("base:%lf\n", base);
      //if(base > best) printf("better!\n");
      best = max(base, best);
    }
    printf("%lf\n", best);
  }
}
