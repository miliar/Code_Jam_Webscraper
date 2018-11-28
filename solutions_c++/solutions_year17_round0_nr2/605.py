#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

ll N,T;

ifstream fin("B.in");
ofstream fout("B.out");

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    fin >> N;
    ll cur = N%10;
    N/=10;
    ll top = cur;
    ll ans = 0;
    ll mult = 1;
    while (N>0) {
      if (N%10 > cur) {
        ans = (mult*10)-1;
        cur = N%10-1;
      }
      else {
        ans += mult*cur;
        cur = N%10;
      }
      mult*=10;
      N/=10;
    }
    ans += mult*cur;
    fout << "Case #" << tt << ": " << ans << "\n";
  }
  return 0;
}