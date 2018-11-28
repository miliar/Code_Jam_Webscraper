#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <map>
#include <iostream>
#include <fstream>
#include <unordered_map>
#include <queue>
#include <set>
using namespace std;
typedef unsigned long long ull;

ifstream fin("C-small-2-attempt4.in");
ofstream fout("C-small.out");

//ifstream fin("C-large.in");
//ofstream fout("C-large.out");

void task() {
  ull n = 0, k = 0;
  fin >> n >> k;

  ull minLR = n;
  ull maxLR = n;

  if (k == n) {
    fout << 0 << " " << 0;
    return;
  }
  /*
  if (n % 2 == 0 && n == k * 2) {
    fout << 1 << " " << 0;
    return;
  }
  if (n % 2 != 0 && n == k * 2 - 1) {
    fout << 0 << " " << 0;
    return;
  }
  if (n % 2 != 0 && n == k * 2 + 1) {
    fout << 1 << " " << 1;
    return;
  }
  */
  multiset<ull> q;
  q.insert(n);
  ull j = 0;

  for (ull i = 0; i < k; ++i) {
    auto x = *(--q.end());
    q.erase(--q.end());

    maxLR = x / 2;
    minLR = (x - 1) / 2;
    ++j;

    if (maxLR == 0 && minLR == 0) {
      fout << 0 << " " << 0;
      return;
    }

    q.insert(maxLR);
    q.insert(minLR);
    
  }
  
  fout << maxLR << " " << minLR;
}

int main() {

  long long t = 0;
  fin >> t;

  for (long long i = 0; i < t; i++) {
    fout << "case #" << i + 1 << ": ";
    task();
    fout << endl;
    cout << i + 1 << endl;
  }
  fout.close();
  cout << "OK";
  return 0;
}