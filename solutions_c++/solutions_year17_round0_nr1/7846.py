#include <iostream>
#include <string>

using namespace std;

void solve(int idx)
{
  std::string row;
  int k;
  cin >> row >> k;

  int res_count = 0;
  for (int off = 0; off < (int)row.size() - k + 1; off++) {
    if (row[off] == '-') {
      res_count++;

      for (int i = off; i < off + k; ++i) {
        if (row[i] == '-')
          row[i] = '+';
        else
          row[i] = '-';
      }
    }
  }

  bool ok = true;
  for (char c : row) {
    if (c == '-') {
      ok = false;
      break;
    }
  }

  cout << "Case #" << idx << ": ";
  if (ok)
    cout << res_count;
  else
    cout << "IMPOSSIBLE";
  cout << endl;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i)
      solve(i + 1);

    return 0;
}
