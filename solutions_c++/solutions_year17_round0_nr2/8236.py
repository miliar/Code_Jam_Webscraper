// TODO Debug later
#include <fstream>
#include <string>
#include <iostream>

using namespace std;

int main() {
  string filename = "B-small-attempt0";
  ifstream fin(filename + ".in");
  ofstream fout(filename + ".out");

  int num_tests; fin >> num_tests;
  for (int num_test = 0; num_test < num_tests; ++num_test) {
    long long num; fin >> num;
    string number = to_string(num);
    int index = ((number[0] == '1') ? -1 : 0);
    for (int i = 1; i < number.size(); ++i) {
      if (number[i - 1] > number[i]) {
        if (index != -1) {
          // cout << "1" << endl;
          if (number[index] == number[i - 1] && i - 1 != 0) {
            --number[index];
            for (int j = index + 1; j < number.size(); ++j) {
              number[j] = '9';
            }
          }
          else {
            --number[i - 1];
            for (int j = i; j < number.size(); ++j) {
              number[j] = '9';
            }
          }
        }
        else {
          // cout << "2" << endl;
          for (int j = 0; j < number.size(); ++j) {
            number[j] = '9';
          }
          number = number.substr(0, number.size() - 1);
        }
        break;
      }
      else if (number[i - 1] == number[i]) {
        continue;
      }
      index = ((number[i] == '1') ? index : i);
    }

    fout << "Case #" << num_test + 1 << ": " << number << endl;
  }

  fin.close();
  fout.close();  

  return 0;
}

