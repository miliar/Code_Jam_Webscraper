#include <iostream>
#include <string>

using namespace std;

int main() {
  int test;
  string str;

  cin >> test;
  for(int T=0;T<test;T++) {
    int k;
    int result = 0;
    cin >> str >> k;
    for(int i=0;i<str.size()-k+1;i++) {
      if ( str[i] == '-' ) {
        result++;
        for(int j=0;j<k;j++) {
          if ( str[i+j] == '+' )
            str[i+j] = '-';
          else
            str[i+j] = '+';
        }
      }
    }
    for(int i=0;i<str.size();i++) {
      if( str[i] == '-' ) result = -1;
    }

    if ( result >= 0 )
      cout << "Case #" << T+1 << ": " << result << endl;
    else
      cout << "Case #" << T+1 << ": " << "IMPOSSIBLE" << endl;
  }
  return 0;
}
