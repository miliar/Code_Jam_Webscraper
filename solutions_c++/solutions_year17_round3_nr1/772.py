#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

vector<pair<LL, LL>> p;

bool comp(pair<LL, LL> a, pair<LL, LL> b) {
  return a.first * a.second > b.first * b.second;
}

int main() {
  const double M_PI = acos(-1);
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n, k;
    cin >> n >> k;        
    p.clear();
    for (int j = 0; j < n; j++) {
      LL r, h;
      cin >> r >> h;
      p.push_back(make_pair(h, r));
    }
    sort(p.begin(), p.end());    
    LL res = 0;
    do {
      LL cur = p[0].second * p[0].second;
      for (int j = 0; j < k; j++) {
        cur += 2 * p[j].first * p[j].second;
      }
      res = max(res, cur);  
    } while (next_permutation(p.begin(), p.end()));        
    cout.precision(6);
    cout << "Case #" << (i + 1) << ": ";	
    cout << fixed << res * M_PI << endl;
  }
}