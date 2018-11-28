#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>  // includes cin to read from stdin and cout to write to stdout
#include <map>  // includes cin to read from stdin and cout to write to stdout
#include <algorithm>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main() {
  int t, n, m;
  double k;
  double s;
  double d;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> d >> n;  // read n and then m.
    cin >> k >> s;
    // std::cerr << "k:" << k << "s:" << '\n';
    double min =  (d*s/(d-k));
    for(int j = 1; j<n; ++j){
      cin >> k >> s;
      double curr = (d*s/(d-k));
      if(curr < min) min = curr;
    }


    // cout << "Case #" << i << ": " << min << endl;
    printf("Case #%d: %.6f \n",i, min);
  }
  return 0;
}
