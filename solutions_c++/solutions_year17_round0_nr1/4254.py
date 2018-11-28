#include <bits/stdc++.h>

using namespace std;

char flip(char a){
  if(a == '-') return '+';
  return '-';
}

int main(void){
  int t, game = 1, k, n;
  string a;
  cin >> t;
  while(t--){
    cin >> a >> k;
    n = a.length();
    int flips = 0;
    for(int i=0; i<n; i++){
      if(i+k > n) break;
      if (a[i] == '-'){
        for(int j=0; j<k; j++)
          a[i+j] = flip(a[i+j]);
        flips++;
      }
    }
    for(int i=0; i<n; i++)
      if(a[i] == '-'){
        flips = -1;
        break;
      }
    cout << "Case #" << game++ << ": " << (flips == -1 ? "Impossible" : to_string(flips)) << endl;
  }
}
