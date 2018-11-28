#include <iostream>
using namespace std;

int main(int argc, char const *argv[]) {
  int n;
  string str;
  cin >> n;
  int m=n;
  while (n--) {
    cin >> str;
    for (int i = 0; i < 20; i++) {
      for (int j = 0; j < str.length()-1; j++) {

        if (str[j+1]<str[j]) {
          for (size_t k = j+1; k < str.length(); k++) {
            str[k] = '9';
          }
          str[j] = str[j] - 1;
        }

      }


    }
    cout << "Case #" << m-n << ": ";
    for (int i = 0; i < str.length(); i++) {
      if (str[i] != '0') {
        cout << str[i];
      }
    }
    cout << endl;
  }
  return 0;
}
