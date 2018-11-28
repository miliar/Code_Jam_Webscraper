#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MOD 1000000007


const double pi = acos(-1);

void insert_to_sorted(vector<double> &v, double a) {
  auto it = lower_bound(v.begin(), v.end(), a);
  v.insert(it, a);
}

double side_surface(pair<double, double> p) {
  return 2.0 * pi * p.first * p.second;
}

double top_surface(pair<double, double> p) {
  return p.first * p.first * pi;
}

int main() {
  int T;
  cin >> T;

  for(int t = 0; t < T; t++) {
    ll K, N;
    cin >> N >> K;

    double ans = 0.0;

    vector< pair<double, double> > cake(N);

    for(ll i = 0; i < N; i++) {
      cin >> cake[i].first >> cake[i].second;
    }

    sort(cake.begin(), cake.end());

    vector<double> v;

    for(ll i = 0; i < K - 1; i++) {
      insert_to_sorted(v, side_surface(cake[i]));
    }

    for(ll i = K - 1; i < N; i++) {
      double sum_surface = top_surface(cake[i]) + side_surface(cake[i]);
      for(ll j = 0; j < K - 1;j ++) {
        sum_surface += v[v.size() - j - 1];
      }
      insert_to_sorted(v, side_surface(cake[i]));
      ans = max(ans, sum_surface);
    }
    cout << setprecision(20);
    cout << "Case #" << t + 1 << ": " << ans << endl;



  }

}
