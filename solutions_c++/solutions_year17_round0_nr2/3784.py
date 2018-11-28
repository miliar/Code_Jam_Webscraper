#include <iostream>
#include <string>
#include <algorithm>

typedef unsigned int ui;
using namespace std;


void fillNines(string& n, ui index) {
  for (ui i = index; i < n.size(); ++i)
    n[i] = '9';
}


string lastTidy(string n) {
  string nSorted = n;
  sort(nSorted.begin(), nSorted.end());

  if (n == nSorted)
    return n;

  for (ui i = 0; i < n.size() - 1; ++i) 
    if (n[i] > n[i + 1]) {
      --n[i];
      fillNines(n, i + 1);
      break;
    }
  return lastTidy(n);
}


int main() {
  ui t;
  cin >> t;
  string num;

  for (ui i = 0; i < t; i++) {
    cin >> num;
    std::cout << "Case #" << i + 1 << ": " << stoul(lastTidy(num)) << "\n";
  }
}
