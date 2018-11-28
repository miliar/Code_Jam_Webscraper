#include <iostream>
#include <string>
#include <queue>
#define MAX_LEN 1000
using namespace std;

int main() {
  int n_case;

  cin >> n_case;
  for (int i_case = 1; i_case <= n_case; ++i_case) {
    int k;
    string s;
    cin >> s >> k;

    // initialize
    int ans = 0;
    bool is_impossible = true;

    // process
    for(int i=0; i<=s.length()-k; ++i) {
      if(s[i]=='-') {
        ans++;
        for(int j=0; j<k; ++j) {
          s[i+j] = (s[i+j]=='+'?'-':'+');
        }
      }
    }

    // check
    for(int i=0; i<s.length(); ++i) {
      if(s[i]=='-') {
        is_impossible = false;
        break;
      }
    }

    // display result
    if(is_impossible) {
      cout << "Case #" << i_case << ": " << ans << "\n";
    } else {
      cout << "Case #" << i_case << ": IMPOSSIBLE\n";
    }
  }
  return 0;
}