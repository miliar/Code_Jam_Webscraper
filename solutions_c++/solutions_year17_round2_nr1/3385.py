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
  int t;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

  for (int i = 1; i <= t; ++i) {
    int des, n;
    float hours = 0.0;
    cin >> des >> n;
    for(int j = 0; j < n; j++){
      int k, s;
      cin >> k >> s;
      float cur = ((float)(des-k))/s;
      if(cur > hours){
        hours = cur;
      }
    }
    float sp = ((float)des)/hours;
    cout << "Case #" << i << ": ";
    printf("%f\n", sp);
    
    
  }
  
  return 0;
}