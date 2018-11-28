#include <iostream>
#include <cstdio>
using namespace std;


int main() {
  int T;
  cin >> T;
  for(int cases=1; cases <= T; cases++){
    string str;
    int n, k;
    cin >> str >> k;
    n = str.size();
    int ans = 0;
    for(int i = 0; i <= n-k; i ++) {
      if( str[i] == '-') {
	ans ++;
	for(int j = 0; j < k; j ++)
	  str[i+j] = (str[i+j] == '-')?('+'):('-');
      }
    }
    for(int i = 0; i < n; i ++) 
      if( str[i] == '-') {
	ans = -1;
	break;
      }
    printf("Case #%d: ", cases);
    if( ans == -1 ) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
  }

  return 0;
}
