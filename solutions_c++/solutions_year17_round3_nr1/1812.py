#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef long double ld;

ll t;
ll n, k;
const ld PI = 3.14159265359;

bool cmp(pair<ld, ld>& a, pair<ld, ld>& b) {
  return a.second > b.second;
}

ld solve(vector<pair<ld, ld>> v, ll f) {
  if (v.size()-f < k) {
    return 0;
  }
  //cerr << "SOLVING FOR " << f << endl;
  ld anw = v[f].first+v[f].second;
  //cerr << "BEGIN ANW " << anw << endl;
  sort(v.begin()+f+1, v.end(), cmp);
  for (int i = f+1; i < f+k; i++) {
    anw += v[i].second;
  //cerr << "STEP" << i-f << " anw " << anw << endl;
  }
  return anw;
}

void solve() {
    cin >> n >> k;
    vector<pair<ld, ld>> v;
    for (int i = 0; i < n; i++) {
      ll r, h; cin >> r >> h;
      v.push_back({PI*r*r, 2*PI*r*h});
    }
    sort(v.rbegin(), v.rend());
    ld anw = 0;
    for (int i = 0; i < n; i++) {
      anw = max(anw, solve(v, i));
    }
    cout << fixed << anw << endl;

}

int main() {
  ios::sync_with_stdio(0);
  cout.precision(10);
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
  }
}
