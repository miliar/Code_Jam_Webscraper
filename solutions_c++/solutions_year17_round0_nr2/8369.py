#include <iostream>
#include <fstream>
using namespace std;

int main() {
  ifstream input("tidy.in");
  ofstream output("tidy.out");
  string line;
  int i, j, n, last, curr, num;
  long long soln, pow;
  
  getline(input, line);
  num = atoi(line.c_str());

  for (i = 0; i < num; i++) {
    getline(input, line);
    n = line.length();
    pow = 1;
    soln = 0;
    last = 9;
    for (j = 0; j < n; j++) {
      curr = line[n-j-1]-'0';
      if (curr > last) soln = pow-1 + pow*(--curr);
      else soln += pow*curr;
      last = curr;
      pow *= 10;
    }
    cout << "Case #" << (i+1) << ": " << soln << endl;
    output << "Case #" << (i+1) << ": " << soln << endl;
  }
}
