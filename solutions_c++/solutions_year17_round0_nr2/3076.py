#include <iostream>
#include <fstream>
using namespace std;

int T, N, smallest[20];
string num, tidynum;
bool tidy;

int main() {
  ifstream fin("B-large.in");
  ofstream fout("B-large.out");
  fin >> T;
  for (int t = 1 ; t <= T ; t++) {
    fin >> num;
    tidynum = "";
    tidy = true;

    for (int i = 0 ; i < num.length() && tidy ; i++) {
      if (i < num.length() - 1 && num[i] - '0' > num[i+1] - '0') {
        int j = i;
        while (j >= 0 && num[j] == num[i]) j--;
        j++;
        if (j == 0) {
          if (num[0] != '1') tidynum += (char)(num[0] - '1' + '0');
          j = 1;
        } else {
          for (int k = 0 ; k < j ; k++) {
            tidynum += num[k];
          }
          // for ( ; j <= i ; j++) {
          if (j <= i) {
            tidynum += (char)(num[i] - '1' + '0');
            j++;
          }
        }
        for ( ; j < num.length() ; j++) {
          tidynum += '9';
        }
        tidy = false;
      }
    }
    if (tidy) {
      tidynum = num;
    }
    fout << "Case #" << t << ": " << tidynum << endl;
  }
  return 0;
}