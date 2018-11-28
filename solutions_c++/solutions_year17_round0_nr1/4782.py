#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    string str;
    int k, cnt = 0;
    cin >> str >> k;
    int poses = str.size() - k + 1;
    for (int i = 0; i < poses; ++i)
      if (str[i] == '-') {
        cnt++;
        for (int j = i; j < i + k; ++j)
          str[j] = (str[j] == '-' ? '+' : '-');
      }
    for (int i = poses; i < (int)str.size(); ++i)
      if (str[i] == '-')
        cnt = -1;
    cout << "Case #" << t << ": ";
    if (cnt >= 0)
      cout << cnt;
    else
      cout << "IMPOSSIBLE";
    cout << endl;
  }
  return 0;
}
