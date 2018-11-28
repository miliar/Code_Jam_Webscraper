#include<iostream>
#include<cstdio>

using namespace std;

int main(){
  //ios_base::sync_with_stdio(true);
  int t; cin >> t;
  for (int i = 1; i <= t; i++){
    double d, n; cin >> d; cin >> n;
    double time = 0;
    for (int j = 0; j < n; j++) {
      long long int k, s; cin >> k; cin >> s;
      double rest = d - k;
      rest = rest > 0 ? rest : 0;
      rest = rest / s; // rest time      
      time = max(time, rest);
    }
//    cout << "Case #" << i << ": " << d << " " << time << " " << (long double) d/time  << endl;
    printf("Case #%d: %f\n", i,  d/time);
  }
}
