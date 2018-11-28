#include <iostream>
using namespace std;

bool isTidy(string num) {
  for (int i = 0; i < num.length() - 1; i++) {
    if (num[i] > num[i+1]) {
      return false;
    }
  }
  return true;
}

string makeTidier(string num) {
  for (int i = 0; i < num.length() - 1; i++) {
    if (num[i] > num[i+1]) {
      if (i == 0 && num[i] == '1'){
        num = string(num.length()-1, '9');
        break;
      } else {
        num[i] = num[i] - 1;
        for (int k = i+1; k < num.length(); k++) {
          num[k] = '9';
        }
        break;
      }
    }
  }
  return num;
}

int main() {
  int t;
  string n;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    cin >> n;

    while(!isTidy(n)) {
      n = makeTidier(n);
    }

    cout << "Case #" << i << ": " << n << endl;
  }

  return 0;
}