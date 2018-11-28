#include <bits/stdc++.h>
using namespace std;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;

const int minutes_day = 24 * 60;
const int minutes_person = minutes_day / 2;
const int cameron = 1;
const int jamie = 2;
const int inf = 1000000;

void read_day(int n, vector<int> &day, int mark) {
  for (int i = 0; i < n; ++i) {
    int a, b;
    cin >> a >> b;
    for (int k = a; k < b; ++k) {
      day[k] = mark;
    }
  }
}

int dp[minutes_day + 1][minutes_person + 1][3][3];
int f(int current, int remaining_cameron, int first, int last, vector<int> &day) {
  if (day[current - 1] == last) return inf;

  if (current == minutes_day) {
    return last != first;
  }

  if (dp[current][remaining_cameron][first][last] == -1) {
    int remaining_jamie = minutes_person - current + minutes_person - remaining_cameron;

    int a = inf;
    if (remaining_cameron) a = (cameron != last) + f(current + 1, remaining_cameron - 1, first, cameron, day);

    int b = inf;
    if (remaining_jamie) b = (jamie != last) + f(current + 1, remaining_cameron, first, jamie, day);
    dp[current][remaining_cameron][first][last] = min(a, b);
  }

  return dp[current][remaining_cameron][first][last];
}

int main() { IO;
  int t;
  cin >> t;

  for (int ncase = 1; ncase <= t; ++ncase) {
    cout << "Case #" << ncase << ": ";

    int ac, aj;
    cin >> ac >> aj;

    vector<int> day(minutes_day);
    read_day(ac, day, cameron);
    read_day(aj, day, jamie);

    memset(dp, -1, sizeof dp);
    int a = f(1, minutes_person - 1, cameron, cameron, day);  // current, remaining cameron, first, last
    int b = f(1, minutes_person, jamie, jamie, day);
    int ans = min(a, b);
    cout << ans << endl;
  }

  return 0;
}
