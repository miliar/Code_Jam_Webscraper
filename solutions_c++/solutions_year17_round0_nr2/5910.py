#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for(int cases = 1; cases <= T; cases++ ) {
    string str;
    cin >> str;
    int n = str.size();
    while(true) {
      int drop = -1;
      for(int i = 0; i < n-1; i ++) 
	if(str[i] > str[i+1]) {drop = i; break;}
      if(drop == -1) break;
      str[drop] --;
      for(int i = drop+1; i < n; i ++ ) str[i] = '9';
    }
    for(int i = 0; i < n; i ++)
      if( str[i] != '0' ) {
	str = str.substr(i);
	break;
      }
    printf("Case #%d: %s\n", cases, str.c_str());
 
  }
  return 0;
}
