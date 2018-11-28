#include <stdio.h>
#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

int main() {
  cin.sync_with_stdio(false);

  int t;
  cin >> t;

  for (int test = 1; test <= t; test++) {
    string s;
    cin >> s;
    int n = s.size();

    for (int i = n - 2; i >= 0; i--) {
      if (s[i] > s[i + 1]) {
        s[i] = s[i] - 1;
        for (int j = i + 1; j < n; j++) {
          s[j] = '9';
        }
      }
    }

    reverse(all(s));
    while (!s.empty() && s.back() == '0') {
      s.pop_back();
    }
    reverse(all(s));

    cout << "Case #" << test << ": " << s << '\n';
  }

  return 0;
}
