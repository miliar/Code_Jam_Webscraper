#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    ofstream fout;
    ifstream fin;
    fin.open("input.txt");
    fout.open("output.txt");
    int t; fin >> t;
    for(int tc = 1; tc <= t; tc++) {
      int n, p; fin >> n >> p;
      int g[p];
      for(int i = 0; i < p; i++) {
        g[i] = 0;
      }
      for(int i = 0; i < n; i++) {
        int temp; fin >> temp;
        g[temp % p]++;
      }
      int ans = g[0]; g[0] = 0;
      cout << ans << ' ' << g[0] << ' ' << g[1] << ' ' << g[2] << ' ' << g[3] << endl;
      for(int i = 1; i < p; i++) {
        int tmp;
        if(i*2 == p) {
          tmp = g[i]/2;
        } else {
          tmp = min(g[i], g[p-i]);
        }
        ans += tmp;
        g[i] -= tmp;
        g[p-i] -= tmp;
      }
      if(p == 2) {
        if(g[1] > 0) {
          ans++;
        }
      } else if(p == 3) {
        ans += g[1]/3;
        g[1] %= 3;
        ans += g[2]/3;
        g[2] %= 3;
        if(g[1] > 0 || g[2] > 0) {
          ans++;
        }
      } else {
        ans += g[1]/4;
        g[1] %= 4;
        ans += g[3]/4;
        g[3] %= 4;
        if(g[2] == 1 && g[1] >= 2) {
          g[2]--;
          g[1] -= 2;
          ans++;
        }
        if(g[2] == 1 && g[3] >= 2) {
          g[2]--;
          g[3] -= 2;
          ans++;
        }
        if(g[1] > 0 || g[2] > 0 || g[3] > 0) {
          ans++;
        }
      }
      fout << "Case #" << tc << ": " << ans << endl;
        
    }
    return 0;
}
