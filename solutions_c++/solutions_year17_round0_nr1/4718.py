#include <bits/stdc++.h>
#define ll long long

using namespace std ;

int main(int argc, char const *argv[])
{
  ll count;
  cin >> count ;
  for (int j = 0; j < count; ++j) {
    cout << "Case #" << j + 1 << ": " ;
    string ss;
    ll n, flips{0};
    cin >> ss >> n;
    ll i{0};
    for (i = 0; i < ss.size() - n + 1; ++i) {
      if (ss[i] == '-') {
        for (ll k = i; k < i + n; ++k) {
          if (ss[k] == '+') {
            ss[k] = '-';
          }
          else {
            ss[k] = '+';
          }
        }
        flips++;
      }
    }
    size_t found = ss.find("-", i, 1);
    if (found != string::npos) {
      cout << "IMPOSSIBLE" << endl;
    }
    else {
      cout << flips << endl;
    }
  }
  return 0;
}

