#include <bits/stdc++.h>

using namespace std;

bool myfunction (pair <int, int> i, pair <int, int> j) {
  if (i.first == j.first)
    return (i.second > j.second);
  return (i.first > j.first);
}

int main () {
  int t, i, n, caso, k, x;
  
  cin >> t;  
  for (caso = 1; caso <= t; caso++) {
    cin >> n >> k;
    vector < pair <int, int> > v;
    v.push_back (make_pair (n/2, (n-1)/2));
    
    for (i = 0; i < n; i++) {
      x = v[i].first;
      if (x > 0)
        v.push_back (make_pair (x/2, (x-1)/2));
      x = v[i].second;
      if (x > 0)
        v.push_back (make_pair (x/2, (x-1)/2));
    }
    sort (v.begin (), v.end(), myfunction);
    
    cout << "Case #" << caso << ": " << v[k-1].first << " " << v[k-1].second << endl;
  }
  
  return 0;
}

