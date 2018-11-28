#include<iostream>
#include<sstream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

bool isCNumTidy(string num) {
  int currMax = -1;
  for (int i = 0; i < num.length(); ++i) {
    int n = num[i] - '0';
    if (n < currMax) return false;
    currMax = n;
  }
  return true;
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    string N;
    cin >> N;
    string candidate = N;

    int nextDigit = N[N.length() - 1] - '0';

    for (int i = N.length() - 2; i >= 0; --i) {
      int n = candidate[i] - '0';
      if (n > nextDigit) {
        n = n - 1;
        candidate[i] = n + '0';
        for (int j = i + 1; j < candidate.length(); ++j) {
          candidate[j] = '9';
        }
      }
      nextDigit = n;
    }
    if (candidate[0] == '0') candidate.erase(0, 1);

    cout << "Case #" << t << ": " << candidate << endl;
  }
  return 0;
}
