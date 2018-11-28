#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int main() {
  int t;
  fin >> t;

  for (int cazul = 1; cazul <= t; ++cazul) {
    string a;
    fin >> a;
    int k;
    fin >> k;

    int nrFlips = 0;

    for (int i = 0; i < a.size() - k + 1; i++) {
      if (a[i] == '-') {
        for (int j = i; j < i + k; ++j) {
          if (a[j] == '-')
            a[j] = '+';
          else
            a[j] = '-';
          }

          ++nrFlips;
      }
    }

    int istGood = true;
    for (int i = 0; i < a.size(); ++i) {
      if (a[i] == '-')
        istGood = false;
    }

    fout << "Case #" << cazul << ": ";

    if (!istGood) {
      fout << "IMPOSSIBLE\n";
    }
    else {
      fout << nrFlips << "\n";
    }

  }

  return 0;


}
