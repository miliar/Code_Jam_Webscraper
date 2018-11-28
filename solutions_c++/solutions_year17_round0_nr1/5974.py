#include <bits/stdc++.h>

using namespace std;

int main (){
  int t,k;
  string s;
  cin >> t;
  for (int i = 0 ; i < t ; ++i){
    cout << "Case #" << i+1 << ":" << " " ;
    cin >> s >> k;
    int size = s.size();
    int tail = 0 , ans = 0;
    while (tail + k - 1 < size){
      if (s[tail] == '-'){
        ans ++;
        bool nu_found = true;
        int nu_tail;
        for (int j  = 0 ; j < k ; ++j){
          if (s[tail+j] == '+' && nu_found) {
            nu_tail= tail+j;
            nu_found = false;
          }
          s[tail+j] = (s[tail+j] == '-') ? '+' : '-';
        }
        tail = (!nu_found) ? nu_tail : tail;
      } else {
        tail++;
      }
    }
    bool found = false;
    for (int j = 0 ; j < k ; ++j){
      if (s[tail+j] == '-') found = true;
    }
    if (found) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }

}
