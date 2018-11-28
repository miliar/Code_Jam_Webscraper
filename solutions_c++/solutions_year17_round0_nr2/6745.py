#include <iostream>
#include <string>

using namespace std;

string reoder(string input) {
  char s = input[0];
  for (int i = 1; i < input.size(); i++) {
    if (input[i] >= s) break;
    input[i] = s;
  }
  return input;
}

int main() {
  int t; cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    string input;
    cin >> input;

    int l = input.size();
    string ans = "";
    bool carry = false;
    for (int i = l - 1; i >= 0; i--) {
      int num = input[i] - '0';
      if (carry) num--;
      carry = false;
      if (i == 0) {
        if (num >= 1)
        ans = (char)(num + '0') + ans;
      } else {
        int prev = input[i - 1] - '0';
        if (prev <= num) {
          ans = (char)(num + '0') + ans;
        } else {
          carry = true;
          ans = '9' + ans;  
        }
      }
      ans = reoder(ans);
    }
    cout << "Case #" << tc << ": " << ans << endl;
  }
  return 0;
}