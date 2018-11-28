#include <iostream>

using namespace std;

string caseN() {
  string N;
  cin >> N;

  string result;
  result += N[0];

  for (int i = 1; i < N.size(); ++i) {
    if (N[i] < N[i-1]) {
      char last = result.back();
      result.pop_back();
      while (!result.empty()) {
        if (last > result.back()) {
          result += (last-1);
          break;
        }
        last = result.back();
        result.pop_back();
      }

      if (result.empty() && last > '1')
        result += last-1;

      result += string(N.size()-result.size()-result.empty(), '9');
      break;
    } else {
      result += N[i];
    }
  }

  return result;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
    cout << "Case #"<<t <<": " << caseN() <<endl;
  return 0;
}
