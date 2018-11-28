#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <queue>

using namespace std;

const double pi = 3.1415926535897;

int main(int argc, const char * argv[]) {
  ifstream f;
  f.open ("in.txt");
  ofstream myfile;
  myfile.open ("out.txt");
  cout << fixed;
  
  int t;
  f >> t;
  for (int test = 1; test <= t; test++) {
    pair<long long, long long> r[1003];
    int n, k;
    f >> n >> k;
    for (int i = 0; i < n; i++) {
      f >> r[i].first;
      f >> r[i].second;
    }
    sort(r, r + n);
    long long res = 0;
    long long current = 0;
    priority_queue<long long, vector<long long>, greater<long long> > q;
    for (int i = 0; i < k - 1; i++) {
      current += 2 * r[i].first * r[i].second;
      q.push(r[i].first * r[i].second * 2);
    }
    for (int i = k - 1; i < n; i++) {
      res = max(res, current + r[i].first * r[i].second * 2 + r[i].first * r[i].first);
      if (k > 1 && q.top() < r[i].first * r[i].second * 2) {
        current -= q.top();
        current += r[i].first * r[i].second * 2;
        q.pop();
        q.push(r[i].first * r[i].second * 2);
      }
    }
    myfile << setprecision(10) << "Case #" << test << ": " << res * pi << "\n";
  }

  return 0;
}
