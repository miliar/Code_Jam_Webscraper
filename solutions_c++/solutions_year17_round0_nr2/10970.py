#include <iostream>
#include <fstream>
using namespace std;

bool check_num(int n) {
  string numb = to_string(n);
  int i, c = 0;
  for (i = 0; i < numb.length() - 1; i++) {
    if (numb.at(i) <= numb.at(i + 1)) {
      c++;
    }
  }
  if (c == numb.length() - 1)
    return true;
  else
    return false;
}

int main() {
  ifstream f1("/home/pavlos/ClionProjects/jam_2017_2/B-small-attempt2.in");
  ofstream f2("/home/pavlos/ClionProjects/jam_2017_2/uz.out");
  string s;
  getline(f1, s);
  int num;
  for (int i = 1; i <= 100; i++) {
    f1 >> num;

    while (num >= 0) {
      if (check_num(num) == true) {
        f2 << "Case #" << i << ": " << num << endl;
        break;
      }
      num--;
    }
  }
  f2.close();
  return 0;

}