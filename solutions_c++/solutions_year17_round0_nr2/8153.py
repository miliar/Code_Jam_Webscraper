#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  string N;

  cin >> T;

  for (int i = 0; i < T; i++) {
    cin >> N;

    int len = N.length();
    //cout << "i: " << i << " =========== " << endl;

    for (int j = 1; j < len; j++) {
      //cout << "j: " << j << " => " << N.at(len-j-1) << endl;
      if (N.at(len-j-1) > N.at(len-j)) {
        N.at(len-j-1) -= 1;
        for (int k = 0 ; k < j; k++) {
          N.at(len-k-1) = '9';
        }
        //cout << "do something" << endl;
      }
    }

    cout << "Case #" << (i + 1) << ": "; 
    int j = 0;
    for (j = 0; j < len; j++) {
      if (N.at(j) != '0')
        break;
    } 
    cout << N.substr(j) << endl;
  }

  return 0;
}