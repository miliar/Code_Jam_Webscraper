// Author: Krzysztof Bochenek
// Email:  kpbochenek@gmail.com
// --------------------------------
#include <stdio.h>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>

typedef long long int ll;
typedef unsigned long long ull;

using namespace std;

int main() {

  int T;

  cin >> T;

  for (int t=1; t<=T; ++t) {
    bool impossible = false;
    int answer = 0, k;
    string s;

    cin >> s >> k;

    for (int i=0; i<s.size()-k+1; ++i) {
      if (s[i] == '-') {
	answer++;
	for (int j=0; j<k; ++j) {
	  if (s[i+j] == '+') s[i+j] = '-';
	  else s[i+j] = '+';
	}
      }
    }

    for (auto a: s) {
      if (a == '-') impossible = true;
    }

    if (impossible) {
      cout << "Case #" << t << ": IMPOSSIBLE" << endl; 
    } else {
      cout << "Case #" << t << ": " << answer << endl; 
    }
  }

  return 0;
}
