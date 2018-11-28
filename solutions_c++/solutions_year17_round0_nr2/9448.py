#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
  int t, n, output, numCnt, cur, cmp, mark, cache;
  bool flag;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
  	flag = false;
    cin >> n;
    cache = n;
    numCnt = 1;
    mark = -1;
    cmp = 10;
    while(n != 0) {
      cur = cmp;
      cmp = n%10; 
      if (cur <= cmp) {
        mark = numCnt;
      }
      if (cur < cmp) {
      	flag = true;
      }
      numCnt *= 10;
      n = n/10;
    }
    output = (mark != -1 && flag == true) ? ((cache/mark)*mark - 1) : cache;
    cout << "Case #" << i << ": " << output << endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }
  return 1;
}