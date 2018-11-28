#include <bits/stdc++.h>
using namespace std;

int i, test, tests, n, k, pz;
string s;
pair<int, int> ans, aux;

pair<int, int> get(int i) {
  pair<int, int> ans = {0, 0};

  while(s[i - ans.first] == '.') ++ans.first;
  while(s[i + ans.second] == '.') ++ans.second;

  --ans.second; --ans.first;
  if(ans.second < ans.first) swap(ans.second, ans.first);

  return ans;
}

int main() {
  ifstream cin("test.in");
  ofstream cout("test.out");
  ios_base::sync_with_stdio(0);

  cin >> tests;
  for(test = 1; test <= tests; ++test) {
    cout << "Case #" << test << ": ";

    cin >> n >> k; s = "O";
    for(i = 1; i <= n; ++i) s += ".";
    s += "O";

    while(k--) {
      ans = {-1, -1}; pz = -1;
      for(i = 1; i <= n; ++i) {
        if(s[i] == 'O') continue;
        aux = get(i);
        if(aux.first > ans.first) ans = aux, pz = i;
        if(aux.first == ans.first && aux.second > ans.second) ans = aux, pz = i;
      }

      s[pz] = 'O';
    }

    cout << ans.second << ' ' << ans.first << '\n';
  }

  return 0;
}