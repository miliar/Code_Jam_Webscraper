
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

#define rep(i,n) for (int (i)=0; (i) < (n); ++(i))
#define repf(i,a,b) for (int (i)=(a); (i) <= (b); ++(i))

using namespace std;

typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector< vd > vdd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;

const double PI = acos(-1);

double area(const pii& p) {
  return (PI*p.first)*p.first + 2.0*(PI*p.first)*p.second;
}

int main() {
  int T;
  cin >> T;
  repf (tc,1,T) {
    int N, K;
    cin >> N >> K;
    vpii pancakes(N);
    rep(i,N) {
      cin >> pancakes[i].first >> pancakes[i].second;
    }
    sort(pancakes.begin(), pancakes.end(), std::greater<pii>());

    double ans = 0.0;
    for (int n=0; n<=(N-K); n++) {
      double cans = area(pancakes[n]);
      priority_queue<double> q;
      for (int i=n+1; i<N; i++) {
        q.push(((double)pancakes[i].first)*pancakes[i].second);
      }
      if (q.size() >= (unsigned int)(K-1)) {
        rep (i, K-1) {
          cans += 2*PI*q.top();
          q.pop();
        }
      }
      ans = max(ans, cans);
    }
    cout << "Case #" << tc << ": " << setprecision(8) << fixed << ans << endl;
  }
}
