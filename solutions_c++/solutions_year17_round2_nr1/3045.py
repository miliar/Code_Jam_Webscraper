#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>

using namespace std;

int n, d;
double vet_a[1001], vet_b[1001];
int min_d, min_v;

int main(){
  int T; cin >> T;
  int cs = 0;
  while(T--){
    //min_d = min_h = 1000000000;
    printf("Case #%d: ", ++cs);
    cin >> d >> n;
    double max_time = -1000000001;
    double minv;
    for(int i = 0; i < n; i++){
      cin >> vet_a[i] >> vet_b[i];
      double h = d - vet_a[i];
      //printf("h eh %lf\n", h);
      double times = h / vet_b[i];
      //printf("times eh %lf\n", times);
      if(times > max_time){
        max_time = times;
        minv = vet_b[i] / max_time;
      }
    }
    printf("%lf\n", d / max_time);
  }
  return 0;
}
