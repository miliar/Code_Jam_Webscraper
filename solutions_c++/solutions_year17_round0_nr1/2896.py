#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int transform(const string s, const char c, const char d, const int k){
  string t = s;
  int changes = 0;
  for(int i = 0; i < t.size(); i++){
    if(t[i] == d){
      if(i > (t.size()-k)){
        return INT_MAX;
      }
      for(int j = i; j < (i+k); j++){
        t[j] = t[j] == c ? d : c;
      }
      changes++;
    }
  }
  return changes;
}

string itoa(int n){
  char s[10];
  sprintf(s, "%d", n);
  return string(s);
}

string pancakeFlipper(const string s, const int k){
  int b = transform(s, '+', '-', k);
  string t = s;
  reverse(t.begin(), t.end());
  int d = transform(t, '+', '-', k);
  if(b == INT_MAX && d == INT_MAX){
      return "IMPOSSIBLE";
  }
  return itoa(min(b, d));
}

int main() {
  int cases, k;
  string s;
  while(cin >> cases){
    for(int i = 1; i <= cases; i++){
      cin >> s >> k;
      printf("Case #%d: %s\n", i, pancakeFlipper(s, k).c_str());
    }
  }
  return 0;
}
