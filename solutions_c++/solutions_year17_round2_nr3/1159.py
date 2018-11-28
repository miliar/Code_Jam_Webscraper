#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int tests; cin >> tests;
  for(int test = 0; test<tests; ++test) {
    int n, q; cin >> n >> q;
    vector<pair<long long,long long> > horses;
    long long end, d;
    for(int i = 0; i<n; ++i) {
      cin >> end >> d;
      horses.push_back(make_pair(end, d));
    }
    long long dists[n];
    for(int i = 0;i<n;++i) {
      for(int j = 0;j<n;++j) {
        long long temp;
        cin >> temp;
        if(temp != -1) {
          dists[j] = temp;
        }
      }
    }
    int temp;cin >> temp >> temp;

    double times[n];
    for(int i = 0; i<n;++i){times[i] = -1;}
    times[0] = 0;
    for(int i = 0; i<n; ++i) {
      long long currdist = horses[i].first - dists[i+1];
      double time = times[i] + 1.0 * dists[i+1] / horses[i].second;
      int currpos = i+1;
      while(currdist >= 0) {
        if(times[currpos] == -1 || times[currpos] > time) {
          times[currpos] = time;
        }
        currdist -= dists[++currpos];
        time += 1.0 * dists[currpos] / horses[i].second;
      }
    }

    cout << fixed << "Case #" << test+1 << ": " << times[n-1] << endl;;
  }
}
