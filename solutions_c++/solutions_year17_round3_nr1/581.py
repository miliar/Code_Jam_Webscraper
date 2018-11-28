#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <cstdio>
using namespace std;

int main() {
  int t;
  cin >> t;
  for(int nr = 1; nr <= t; nr ++) {
    int n, k;
    cin >> n >> k;
    pair <long long, long long> p[n];
    for(int i = 0; i < n; i ++) {
      cin >> p[i].second >> p[i].first;
      p[i].first = -1 * p[i].first * p[i].second * 2LL; 
      p[i].second *= -1;
    }
    
    sort(p, p+n);
    
    for(int i = 0; i < n; i ++) {
      p[i].first *= -1;
      p[i].second *= -1;
    }
    
    long long mr = 0;
    long long w = 0;
    for (int i = 0; i < k - 1; i ++) {
      w += p[i].first;
      mr = max(mr, p[i].second);
    }
    long long mw = w + mr * mr, amr;
    for(int i = k-1; i < n; i ++) {
      amr = max(mr, p[i].second);
      mw = max(mw, w + p[i].first + amr * amr);
    }
    double mw2 = mw;
    mw2  = mw2 * M_PI;
    cout << "Case #" << nr <<": ";
    printf("%lf", mw2);
    cout << endl;
  }
  
}
