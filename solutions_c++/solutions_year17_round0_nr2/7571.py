#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
using namespace std;

ifstream fin("b.in");
ofstream fout("b.out");

const int MAXN = 20;

long long nr;
int t;
int cifre[MAXN], nrCif;

int main() {
  fin >> t;

  for (int caz = 1; caz <= t; ++caz) {
    fin >> nr;
    nrCif = 0;

    while (nr > 0) {
      cifre[++nrCif] = nr % 10;
      nr /= 10;
    }

    int found = 0, poz;

    for (int i = nrCif; i > 1; --i) {
      if (cifre[i] > cifre[i - 1]) {
        found = 1;
        poz = i;
        break;
      }
    }

    if (found) {
      cifre[poz] -= 1;
      int poz2 = poz;
      for (int j = poz + 1; j <= nrCif; ++j) {
        if (cifre[j] > cifre[j - 1]) {
          cifre[j] -= 1;
          poz2 = j;
        }
        else break;
      }
      for (int i = poz2 - 1; i >= 1; --i)
        cifre[i] = 9;
    }

    long long nrSol = 0;

    for (int i = nrCif; i >= 1; --i) {
      nrSol = nrSol * 10 + cifre[i];
    }

    fout << "Case #" << caz << ": " << nrSol << "\n";


  }

  return 0;

}
