#include <iostream>
#include <fstream>

#include <string>
#include <iomanip>
#include <vector>

using namespace std;

using std::vector;
using std::string;
using std::pair;

void work(std::ifstream& in, std::ofstream& out) {

  int d, n;
  in >> d >> n;
  vector<int> ps(n);
  vector<double> s(n);
  double speed = 0;
  for (int i = 0; i < n; ++i) {
    in >> ps[i] >> s[i];
    double curr = d / ((d - ps[i]) / s[i]);
    if (i == 0 || speed > curr) {
      speed = curr;
    }
  }
  out << std::setprecision(20) << speed << '\n';
}

int main() {

  std::ifstream in("input.in");
  std::ofstream out("output.out");

  size_t T;
  in >> T;

  for (size_t i = 0; i < T; ++i) {
    out << "Case #" << i + 1 << ": ";
    work(in, out);
  }
  return 0;
}