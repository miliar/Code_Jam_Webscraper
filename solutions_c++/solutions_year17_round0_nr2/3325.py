#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> get_digits(long long N)
{
  vector<int> ans;
  while (N != 0) {
    ans.push_back(N % 10);
    N /= 10;
  }
  reverse(ans.begin(), ans.end());
  return ans;
}

long long to_value(vector<int> digit)
{
  long long ans = 0;
  for (int i = 0; i < digit.size(); i++) {
    ans *= 10;
    ans += digit[i];
  }
  return ans;
}

long long tidy(long long N)
{
  vector<int> digit = get_digits(N);
  int index = digit.size();
  for (int i = digit.size() - 1; i > 0; i--) {
    if (digit[i - 1] > digit[i]) {
      digit[i - 1]--;
      index = i;
    }
  }

  for (int i = index; i < digit.size(); i++) {
    digit[i] = 9;
  }
  return to_value(digit);
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    long long N;
    cin >> N;

    cout << "Case #" << t << ": " << tidy(N) << "\n";
  }

  return 0;
}

