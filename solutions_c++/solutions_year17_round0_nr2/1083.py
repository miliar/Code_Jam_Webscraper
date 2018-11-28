#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <map>
#include <climits>
#include <stack>
#include <string>
#include <stdio.h>
#include <ctype.h>
#include <cstdint>
#include <unordered_set>
#include <unordered_map>
#include <utility>
#include <math.h>

using namespace std;

int main() {
  int t, k;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  int count = 10;
  for (int i = 1; i <= t; ++i) {
    string s;
    cin >> s;
    for(int i = (int)s.size() - 1; i > 0; i--){
      if(s[i] < s[i - 1]){
        for(int j = i; j < s.size(); j++)
          s[j] = '9';
        s[i - 1] = s[i - 1] - 1;
      }
    }
    if(s[0] == '0')
      s.erase(0,1);
    cout << "Case #" << i << ": " << s << endl;
  }
  
  return 0;
}