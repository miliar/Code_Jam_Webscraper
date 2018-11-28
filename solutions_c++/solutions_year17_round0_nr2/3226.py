#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>
#include <string>
#include <climits>
using namespace std;

void solution(string& S) {
  int len = S.length();
  int pos = 0;
  bool isOk = true;
  while (pos < len - 1) {
    if (S[pos] > S[pos+1]) {
      isOk =false;
      break;
    }
    pos++;
  }
  //cout << "pos = " << pos << endl;
  if (!isOk) {
    while(pos > 0 && S[pos-1] == S[pos]) pos--;
    if (pos == 0 && S[0] == '1') {
      S = string(S.length()-1, '9');
    } else {
      S[pos] = S[pos] - 1;
      //cout << "pos = " << pos << endl;
      //cout << S << endl;
      for (int i = pos+1; i < S.length(); i++) {
        S[i] = '9';
      }
    }
  }
}

int main() {
    int T;
    string S;
    cin >> T;
    for ( int i = 0; i < T; i++) {
        cin >> S;
        solution(S);
        cout << "Case #" << i+1 <<": " << S << endl;
    }
    return 0;
}
