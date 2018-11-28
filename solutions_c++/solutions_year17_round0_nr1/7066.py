#include <iostream>
using namespace std;

int main() {
  int n;
  cin >> n;

  for(int j = 1; j <= n; j++){
    bool has_ans = true;
    int ans = 0;
    int k;
    string s;
    cin >> s >> k;

    int i = 0;

    for(; i <= s.size() - k; i++){
      if(s[i] == '-'){
        for(int l = i; l < i+k; l++){
          s[l] = (s[l] == '+')? '-' : '+';
        }
        ans++;
      }
    }

    for(; i < s.size(); i++){
      if(s[i] == '-'){
        has_ans = false;
      }
    }

    if(has_ans) {
      cout << "Case #" << j << ": " << ans << endl;
    }
    else {
      cout << "Case #" << j << ": IMPOSSIBLE" << endl;
    }
  }
}
