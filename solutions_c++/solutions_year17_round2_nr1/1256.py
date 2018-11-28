#include <bits/stdc++.h>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=1; t<=T; t++){
    int D, N;
    cin >> D >> N;
    double best = 0.0;
    for(int i=0; i<N; i++){
      int k, s;
      cin >> k >> s;
      double curr = ((double)(D-k)) / s;
      best = max(best, curr);
    }
    cout << "Case #" << t << ": " << fixed << setprecision(7) << ((double)D)/best << endl;
    //printf("Case #%d: %.7f\n", t, ((double)D)/best);
  }
  return 0;
}
