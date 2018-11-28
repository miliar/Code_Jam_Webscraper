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

ll N,T,K;

ifstream fin("C.in");
ofstream fout("C.out");

int main() {
  fin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Working on Case #" << tt << "\n";
    fin >> N >> K;
    ll ns=1,s=N,nl=0,l=N;
    while (K > ns+nl) {
      K -= ns+nl;
      ll temp1 = (s-1)/2;
      ll temp2 = l/2;
      ll temp3 = ns;
      ll temp4 = nl;
      if (s/2 == temp2) temp4 += ns;
      else temp3 += ns;
      if ((l-1)/2 == temp1) temp3 += nl;
      else temp4 += nl;
      s = temp1;
      l = temp2;
      ns = temp3;
      nl = temp4;
      //cout << K << " " << ns << " " << s << " " << nl << " " << l << "\n";
    }
    ll ans1,ans2;
    if (K <= nl) {
      ans1 = l/2;
      ans2 = (l-1)/2;
    }
    else {
      ans1 = s/2;
      ans2 = (s-1)/2;
    }
    fout << "Case #" << tt << ": " << ans1 << " " << ans2 << "\n";
  }
  return 0;
}