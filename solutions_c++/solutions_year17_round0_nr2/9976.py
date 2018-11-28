#include <iostream>
using namespace std;
typedef long long ll;

int main() {
  int n;
  cin >> n;
  for (int i = 0; i < n; i++) {
    string num;
    cin >> num;
    while (true) {
      bool changed = false;
      for (int j = 0; j < num.length()-1; j++) {
        if (num[j] > num[j+1]) {
          changed = true;
          while (num[j] == '0' && j != 0) {
            j--;
          }
          num[j]--;
          for (int k = j+1; k < num.length(); k++) num[k] = '9';
        }
      }
      if (!changed) break;
    }
    long long fin = 0;
    for (int j = 0; j < num.length(); j++) {
      fin = (fin * 10) + (num[j]-'0');
    }
    cout << "Case #" << i+1 << ": " << fin << endl;
  }


  return 0;
}
