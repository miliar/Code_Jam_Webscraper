#include <fstream>

using namespace std;

ifstream cin ("test.in");
ofstream cout ("test.out");

int main() {
  int T;
  cin >> T;
  for (int task = 1; task <= T; ++task) {
    string str;
    int k;
    cin >> str >> k;

    int ans = 0;
    int n = str.size();
    int firstMinus = 0;
    for (;firstMinus < n and str[firstMinus] != '-'; ++firstMinus);

    while (firstMinus + k - 1 < n) {
      for (int i = firstMinus; i <= firstMinus + k - 1; ++i) {
        if (str[i] == '-') {
          str[i] = '+';
        }
        else {
          str[i] = '-';
        }
      }

      for (;firstMinus < n and str[firstMinus] != '-'; ++firstMinus);
      ++ans;
    }

    bool ok = true;
    for (int i = 0; i < n; ++i) {
      if (str[i] == '-') {
        ok = false;
      }
    }

    if (ok) {
      cout << "Case #" << task << ": " << ans << '\n';
    }
    else {
      cout << "Case #" << task << ": IMPOSSIBLE\n";
    }
  }
  return 0;
}
