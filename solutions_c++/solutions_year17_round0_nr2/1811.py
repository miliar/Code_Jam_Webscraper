#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int i = 1; i <= T; ++i) {
    string number;
    cin >> number;

    int errPlace = number.size();
    char last = number[number.size() - 1];
    for(int j = number.size() - 2; j >= 0; --j) {
      if( number[j] > last ) {
        errPlace = j;
        last = (char)(number[j] - 1);
      } else {
        last = number[j];
      }
    }

    printf("Case #%d: ", i);
    for(int j = 0; j < errPlace; ++j) {
      cout << number[j];
    }
    if(errPlace < number.size()) {
      if(number[errPlace] != '1') {
        cout << (char)(number[errPlace] - 1);
      }
      for(int j = errPlace + 1; j < number.size(); ++j) {
        cout << 9;
      }
    }
    cout << endl;
  }
  return 0;
}