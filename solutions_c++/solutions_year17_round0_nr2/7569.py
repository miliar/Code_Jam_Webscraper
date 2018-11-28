#include <iostream>
#include <string>
using namespace std;

typedef unsigned long long ull;

string tidy(ull n) {
  string tmp = to_string(n);
  
  if (tmp.size() == 1) {
    return tmp;
  }
  
  for (int i = tmp.size() - 1; i > 0; --i) {
    if (tmp[i] < tmp[i - 1]) {
      tmp[i - 1] = (tmp[i - 1] - '0' - 1) + '0';
      for (int j = i; j < tmp.size(); ++j) {
        tmp[j] = '9';
      }
    }
  }
  
  string answer = "";
  for (int i = 0; i < tmp.size(); ++i) {
    if (tmp[i] != '0') {
      answer += tmp[i];
    }
  }
  
  return answer;
}

int main() {
  int t;
  cin >> t;
  
  for (int i = 1; i <= t; ++i) {
    ull n;
    cin >> n;
    cout << "Case #" << i << ": " << tidy(n) << "\n";
  }
  
  return 0;
}
