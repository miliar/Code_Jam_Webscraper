#include <iostream>
#include <string>
using namespace std;

int main() {
  int n_case;

  cin >> n_case;
  for (int i_case = 1; i_case <= n_case; ++i_case) {
    string s;
    cin >> s;

    // initialize
    int val[20];
    for(int i=0; i<s.length(); ++i) {
        val[s.length()-i-1] = s[i]-'0'; // reverse order
    }

    // process
    int min_value_memo = 9;
    for(int i=0; i<s.length(); ++i) {
      if(val[i] <= min_value_memo) {
        min_value_memo = val[i];
      } else {
        --val[i];
        for(int j=0; j<i; ++j) {
          val[j] = 9;
        }
        min_value_memo = val[i];
      }
    }

    // check is_zero
    bool is_zero = true;
    for(int i=0; i<s.length(); ++i)
      if(val[i]!=0) {
        is_zero = false;
        break;
      }

    // display result
    if(is_zero) {
      cout << "Case #" << i_case << ": 0\n";
    } else {
      cout << "Case #" << i_case << ": ";
      int leading_idx = s.length()-1;
      while(val[leading_idx]==0) {
        leading_idx--;
      }
      for(int i=leading_idx; i>=0; --i) {
        cout << val[i];
      }
      cout << "\n";
    }
  }
  return 0;
}