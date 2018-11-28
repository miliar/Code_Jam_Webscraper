#include <fstream>

using namespace std;

ifstream cin ("test.in");
ofstream cout ("test.out");

int main() {
  int T;
  cin >> T;
  for (int task = 1; task <= T; ++task) {
    string str;
    cin >> str;
    string ans;

    int n = str.size();
    for (int i = 0; i < n; ++i) {
      if (ans.empty() or ans.back() <= str[i]) {
        ans.push_back(str[i]);
      }
      else {
        int j = i - 1;
        ans.push_back('9');
        --ans[j];
        --j;
        bool entered = false;
        while (j >= 0 and (ans[j] > ans[j + 1] or ans[j + 1] == '/')) {
          ans[j + 1] = '9';
          --ans[j];

          --j;
          entered = true;
        }

        if (entered) {
          --ans[j];
        }
        // while (j >= 0 and ans[j] > str[i]) {
        //   if (ans[j] != '0') {
        //     --ans[j];
        //   }
        //   else {
        //     ans[j] = '9';
        //     ans[j - 1]
        //   }
        //   ans[j + 1] = '9';
        //   --j;
        // }

        if (ans[0] == '0') {
          ans.clear();
          for (int k = 0; k < (int) str.size() - 1; ++k) {
            ans.push_back('9');
          }
        }
        else {
          while (ans.size() < str.size()) {
            ans.push_back('9');
          }
        }

        break;
      }
    }

    cout << "Case #" << task << ": " << ans << '\n';
  }
  return 0;
}
