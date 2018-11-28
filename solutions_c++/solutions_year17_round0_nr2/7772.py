#include <iostream>
#include <string>
using namespace std;

long long generate_1(int n) {
  long long output = 0;
  for (int i = 0; i < n; i++) output = output * 10 + 1;
  return output;
}

long long generate_0(int n) {
  long long output = 1;
  for (int i = 0; i < n; i++) output = output * 10;
  return output;
}

int main() {
  int N;
  cin >> N;
  for (int c = 0; c < N; c++) {
    string input;
    cin >> input;
    int l = input.length();
    string temp = input;
    long long output = 0;
    for (int i = 0 ; i < l ; i++) {
      int current = temp[0] - '0';
      long hold = generate_1(l - i);
      if (current * hold > stol(temp)) {
        if (current == 1) {
          output = generate_1(l - 1) * 9;
        }
        else {
          output = output * 10 + (current - 1);
          output = output * generate_0(l - i - 1);
          output += generate_1(l - i - 1) * 9;
         }
         break;
      }
      else {
        output = output * 10 + current;
      }
      temp = temp.substr(1);
    }
    cout << "Case #" << c + 1 << ": "<< output << endl;
  }
  return 0;
}
