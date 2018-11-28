#include <iostream>
#include <string>
using namespace std;

int main() {
  int t;

  cin >> t;

  for(int q = 1; q <= t; q++) {
    long long n;
    cin >> n;

    if ( n < 10 ) {
      cout << "Case #" << q << ": " << n << endl;
    } else {
      string s = to_string(n);
      string result;
      int a = 0;
      int c = 0;

      for(int i = 0; i < s.size() - 1; i++) {
        if ( s[i] > s[i+1] ) {
          if ( i == 0 ) {
            if ( s[i] == '1' ) {
              for (int j = 0; j < s.size() - 1; j++) {
                result.push_back('9');
              }
              break;
            } else {
              result.push_back(s[i] - 1);
              for (int j = 0; j < s.size() - 1; j++) {
                result.push_back('9');
              }
              break;
            }
          } else {
            i -= a;
            if ( s[i] - 1 != '0' ) {
              result.push_back(s[i] - 1);
            }
            for (int j = i; j < s.size() - 1; j++) {
              result.push_back('9');
            }
            break;
          }
        } else {
          if ( s[i] == s[i+1] ) {
            a++;
          } else {
            c++;
            result.push_back(s[i]);
          }
        }
      }

      int ac = a + c;

      if ( (c == s.size() - 1) || (a == s.size() - 1) || ( ac == s.size() - 1 ) ) {
        cout << "Case #" << q << ": " << s << endl;
      } else {
        cout << "Case #" << q << ": " << result << endl;
      }
    }
  }

  return 0;
}