#include <bits/stdc++.h>

using namespace std;

bool pair_compare(const pair<int, char>& first_e, const pair<int, char>& second_e) {
  return (first_e.first > second_e.first) || ((first_e.first == second_e.first) && (first_e.second > second_e.second));
}

void solve() {
  int N; int R; int O; int Y; int G; int B; int V;
  cin >> N >> R >> O >> Y >> G >> B >> V;
  int max_C = max(max(R, Y), B);
  int sum = R+Y+B;
  if((sum-max_C) < max_C) {
    cout << "IMPOSSIBLE";
  } else {
    vector< pair<int, char>  > colors;
    colors.push_back(make_pair(R, 'R'));
    colors.push_back(make_pair(Y, 'Y'));
    colors.push_back(make_pair(B, 'B'));
    char lc = '?';
    sort(colors.begin(), colors.end(), pair_compare);
    sum--;
    if(colors[0].second=='B') {
      cout << colors[1].second;
      lc = colors[1].second;
      colors[1].first = colors[1].first - 1;
    } else {
      cout << colors[0].second;
      lc = colors[0].second;
      colors[0].first = colors[0].first - 1;
    }
    while(sum--) {
      sort(colors.begin(), colors.end(), pair_compare);
      if(colors[0].second != lc) {
        cout << colors[0].second;
        lc = colors[0].second;
        colors[0].first = colors[0].first - 1;
      } else {
        cout << colors[1].second;
        lc = colors[1].second;
        colors[1].first = colors[1].first - 1;
      }
    }
  }
}

int main() {
  int t; cin >> t;
  for(int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    solve();
    cout << endl;
  }
  return 0;
}
