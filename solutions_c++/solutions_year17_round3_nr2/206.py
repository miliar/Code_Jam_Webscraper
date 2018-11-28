#include <bits/stdc++.h>

#define all(x) x.begin(),x.end()
using namespace std;

typedef long long ll;
typedef long double ld;

ll getans(ll n[2], vector<pair<ll, ll>> mas[2]) {
  ll curans = 0;
  ll curlen = 0;
  vector<pair<pair<ll, ll>, bool>> vec;
  for (int i = 0; i < mas[0].size(); ++i) {
    vec.push_back({mas[0][i], false});
    curlen += mas[0][i].second - mas[0][i].first;
  }
  for (int i = 0; i < mas[1].size(); ++i) {
    vec.push_back({mas[1][i], true});
  }
  sort(all(vec));
  vector<pair<ll, ll>> can;
  for (int i = 0; i < vec.size() - 1; ++i) {
    if (vec[i].second == false && vec[i + 1].second == false) {
      can.push_back({0, vec[i + 1].first.first - vec[i].first.second});
      curans += 2;
    } else if (vec[i].second != vec[i + 1].second) {
      curans++;
      can.push_back({1, vec[i + 1].first.first - vec[i].first.second});
    }
  }
  if (vec[0].second == false && vec[vec.size() - 1].second == false) {
    can.push_back({0, vec[0].first.first + 1440 - vec[vec.size() - 1].first.second});
    curans += 2;
  } else if (vec[0].second != vec[vec.size() - 1].second) {
    curans++;
    can.push_back({1, vec[0].first.first + 1440 - vec[vec.size() - 1].first.second});
  }
  sort(all(can));
  for (int i = 0; i < can.size(); ++i) {
    if (curlen + can[i].second <= 720) {
      if (can[i].first == 0) {
        curans -= 2;
      }
      curlen += can[i].second;
    } else {
      curlen = 720;
    }
  }
  if (curlen == 720) {
    return curans;
  } else return 228228;
}

int run() {
  ll n[2];
  cin >> n[0] >> n[1];
  vector<pair<ll, ll>> mas[2];
  mas[0].resize(n[0]);
  mas[1].resize(n[1]);
  for (int i = 0; i < n[0]; ++i) {
    cin >> mas[0][i].first >> mas[0][i].second;
  }
  for (int i = 0; i < n[1]; ++i) {
    cin >> mas[1][i].first >> mas[1][i].second;
  }
  ll ans = getans(n, mas);
  swap(n[0], n[1]);
  swap(mas[0], mas[1]);
  ans = min(ans, getans(n, mas));
  cout << ans << endl;
  return 0;
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ll t;
  cin >> t;
  for (int q = 0; q < t; ++q) {
    cout << "Case #" << q + 1 << ": ";
    run();
  }
  return 0;
}