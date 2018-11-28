#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main() {
  int T;
  cin >> T;

  for (int t = 0; t < T; ++t) {
    string s;
    cin >> s;

    cout << "Case #" << t + 1 << ": ";
    if (s.size() == 1) {
      cout << s << endl;
      continue;
    }

    bool tidy = true;
    for (int i = 0; i < s.size() - 1; ++i) {
      tidy &= s[i] < s[i + 1];
    }
    if (tidy) {
      cout << s << endl;
      continue;
    }

    int lb = 0;
    for (int i = 1; i < s.size(); ++i) {
      if (s[i-1] < s[i]) {
        lb = i;
      }
      if (s[i-1] > s[i]) {
        s[lb]--;
        for(int j = lb+1; j < s.size(); ++j) {
          s[j] = '9';
        }
        break;
      }
    }

    if (lb == 0 && s[lb] == '0') {
      cout << s.substr(1) << endl;
    } else {
      cout << s << endl;
    }
  }
}
