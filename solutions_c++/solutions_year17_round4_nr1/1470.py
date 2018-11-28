
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  int t;
  cin >> t;
  for(int k = 1; k <= t; k++){
    int n, p, num;
    cin >> n >> p;
    int *g = new int[p];
    for(int i = 0; i < p; i++)
      g[i] = 0;
    for(int i = 0; i < n; i++){
      cin >> num;
      if(num % p != 0)
        g[num % p]++;
    }

    cout << "Case #" << k << ": ";

    if(p == 2)
      cout << n - g[1] / 2 << endl;
    if(p == 3){
      int v;
      v = 2 * (max(g[1], g[2]) - min(g[1], g[2])) / 3 + min(g[1], g[2]);
      cout << n - v << endl;
    }
    if(p == 4){
      int v = 0;
      v += g[2] / 2;
      g[2] %= 2;

      int m = min(g[1], g[3]);
      v += m;
      g[1] -= m;
      g[3] -= m;

      if(g[2] == 1){
        if(g[1] >= g[3] && g[1] > 1){
          g[1] -= 2;
          g[2] = 0;
          v += 2;
        }
        else if(g[3] >= g[1] && g[3] > 1){
          g[3] -= 2;
          g[2] = 0;
          v += 2;
        }
      }

      v += 3 * (max(g[1], g[3]) + g[2]) / 4;

      cout << n - v << endl;


    }

  }

  return 0;
}
