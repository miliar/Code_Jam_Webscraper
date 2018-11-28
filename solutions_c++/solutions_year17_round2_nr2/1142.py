#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int tests; cin >> tests;
  for(int test = 0; test<tests; ++test) {
    int n; cin >> n;
    int colors[6];
    for(int i = 0; i<6; ++i) {
      cin >> colors[i];
    }
    int mx = max(colors[0], max(colors[2], colors[4]));
    if(mx > (n/2)) {
      cout << "Case #" << test+1 << ": " << "IMPOSSIBLE" << endl;
      continue;
    }
    vector<char> ret;
    int a, b;
    char ca, cb;
    if(mx == colors[0]) {
      while(colors[0]--) {
        ret.push_back('R');
      }
      if(colors[2] > colors[4]) {
        a = 2;
        b = 4;
        ca = 'Y';cb = 'B';
      }
      else {
        a = 4;
        b = 2;
        ca = 'B';cb = 'Y';
      }
    }
    else if(mx == colors[2]) {
      while(colors[2]--) {
        ret.push_back('Y');
      }
      if(colors[0] > colors[4]) {
        a = 0;
        b = 4;
        ca = 'R';cb = 'B';
      }
      else {
        a = 4;
        b = 0;
        ca = 'B';cb = 'R';
      }
    }
    else {
      while(colors[4]--) {
        ret.push_back('B');
      }
      if(colors[0] > colors[2]) {
        a = 0;
        b = 2;
        ca = 'R';cb = 'Y';
      }
      else {
        a = 2;
        b = 0;
        ca = 'Y';cb = 'R';
      }
    }


    int sz = ret.size();
    for(int i = sz; i>0; i-=1) {
      if(sz - i + 1 <= colors[a]) {
        ret.insert(ret.begin()+i, ca);
      }

      if(i <= colors[b]) {
        ret.insert(ret.begin()+i, cb);
      }
    }

    cout << "Case #" << test+1 << ": ";
    for(int i = 0; i<(int)ret.size(); ++i) {
      cout << ret[i];
    }
    cout << endl;
  }
}
