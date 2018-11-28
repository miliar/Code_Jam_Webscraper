#include <iostream>
#include <string>
using namespace std;

int main(void)
{
  int tt;
  cin >> tt;

  for(int t = 1; t <= tt; ++t) {
    string s;
    int i, j, k;
    int answer = 0;

    cin >> s;
    cin >> k;

    for(i = 0; i <= s.length() - k; ++i) {
      if(s[i] == '-') {
        for(j = 0; j < k; ++j) {
          s[i + j] = s[i + j] == '-' ? '+' : '-';
        }
        answer += 1;
      }
    }

    for(i = 0; i < s.length(); ++i) {
      if(s[i] == '-') {
        answer = -1;
        break;
      }
    }

    cout << "Case #" << t << ": ";
    if(answer == -1) {
      cout << "IMPOSSIBLE";
    } else {
      cout << answer;
    }
    cout << endl;
  }
  return 0;
}

