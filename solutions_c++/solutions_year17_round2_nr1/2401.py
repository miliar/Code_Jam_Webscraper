#include <bits/stdc++.h>

using namespace std;

int main(void){
  ios::sync_with_stdio(false);
  int t;
  double ki, si, di, time, max_time, max_speed;
  cin >> t;
  int game = 1;
  while(t--){
    int d, n;
    cin >> d >> n;
    max_time = 0.0;
    for(int i = 0; i < n; i += 1){
      cin >> ki >> si;
      di = d - ki;
      time = di / si;
      max_time = max(time, max_time);
    }
    max_speed = d / max_time;
    printf("Case #%d: %0.6lf\n", game++, max_speed);
  }
}
