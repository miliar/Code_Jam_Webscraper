#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int T;
int num[19];

int main(){

  cin >> T;

  for (int cas=1; cas<=T; cas++){
    string s;
    cin >> s;
    // Turn into number
    for (int i=0; i<s.length(); i++){
      num[i] = s[i] - '0';
    }

    // Find first decreasing position
    int decrease_pos = 0;
    while (decrease_pos < s.length() - 1){
      if (num[decrease_pos] > num[decrease_pos + 1]) break;

      decrease_pos += 1;
    }

    // The number is already tidy
    if (decrease_pos == s.length() - 1){
      cout << "Case #" << cas << ": " << s << endl;
      continue;
    }

    // cout << decrease_pos << endl;
    int start_pos = decrease_pos;
    while (0 < start_pos && num[start_pos-1] == num[decrease_pos]) start_pos -= 1;

    // cout << start_pos << endl;
    num[start_pos] -= 1;
    for (int i=start_pos+1; i < s.length(); i++){
      num[i] = 9;
    }

    bool can_print = false;
    cout << "Case #" << cas << ": ";
    for (int i=0; i < s.length(); i++){
      if (num[i] > 0) can_print = true;
      if (can_print) cout << num[i];
    }
    cout << endl;
  }
  return 0;
}
