#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;
typedef long long ll;
#define F first
#define S second
#define N 1010

int t[N], s[N];

bool ok(int n, int d, double k){
  for(int i=0; i<n; ++i){
    double t1 = (double) (d-t[i]) / (double)s[i];
    double t2 = (double) d / k;
    if(t2 < t1) return 0;
  }
  return 1;
}

int main(){
  int T; cin >> T;
  for(int j=0; j<T; ++j){
    int d, n; cin >> d >> n;
    double V = 0;
    for(int i=0; i<n; ++i) {
      cin >> t[i] >> s[i];
      V = max(V, (double)(d-t[i])/(double) s[i]);
    }
    V = d/V;
    cout << fixed;
    cout << setprecision(7) << "Case #" << j+1 << ": " << V << "\n";
  }
}
