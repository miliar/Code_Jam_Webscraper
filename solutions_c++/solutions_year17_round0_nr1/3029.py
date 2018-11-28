#include <iostream>
#include <vector>
#include <string>

using std::cin;  using std::cout;  using std::endl;
using std::vector; using std::string;

int main() {

  int T;
  cin >> T;

  string s;
  getline(cin,s);

  long N, currentN, cN;

  for (int i=1; i<=T; ++i) {

    string pancakes;
    getline(cin, pancakes);

    int p=0;

    while(pancakes[p] == '+' || pancakes[p] == '-')
      p++;
    int len = p;

    p++;

    int K = 0;
    while(p < pancakes.length())
      K = K*10 + pancakes[p++]-'0';
      
    bool imp = false;
    
    int count = 0;
    for (int j = 0; j<= len-K;  ++j) {
      if (pancakes[j] == '-') {
	++count;
	for (int k=0; k<K; ++k) {
	  if (pancakes[j+k] == '-')
	    pancakes[j+k] = '+';
	  else
	    pancakes[j+k] = '-';
	}
      }
    }
    for (int j = len-K+1; j< len;  ++j) {
      if (pancakes[j] == '-') {
	imp = true;
      }
    }

    if (imp)
      cout << "case #" << i << ": " << "IMPOSSIBLE" << endl;
    else
      cout << "case #" << i << ": " << count << endl;

  }

  return 0;
}
