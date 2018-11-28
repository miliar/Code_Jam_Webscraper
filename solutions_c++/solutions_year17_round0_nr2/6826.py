#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

void solve(string& s, int k) {
  
  for (int i = s.length()-2; i >= 0; i--) {
    
    if (s[i] > s[i+1]) {
        while (s[i] == '0') {
          i--;
        }
        s[i] = s[i]-1;
        for (int k = i+1; k < s.length(); k++) {
          s[k] = '9';
        }
    }
  }
  
}

int main(int argc, char const *argv[]) {
  int t_cases;
  cin >> t_cases;
  for (int c = 1; c <= t_cases; c++) {
    string s;
    
    cin >> s;
    
    solve(s, 0);
    cout << "Case #" << c << ": " << atoll(s.c_str()) << endl;
  }
  return 0;
}
