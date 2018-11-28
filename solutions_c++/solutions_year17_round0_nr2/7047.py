#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<string>
#include<sstream>
#include<cmath>
#include<numeric>
using namespace std;

int main(){

  int t;
  cin >> t;
  for(int loop=0; loop<t; loop++){
    long long int n;
    cin >> n;
    long long int ans = 1;
    for(long long int i=n; i>=1; i--){
      string s = to_string(i);
      string tmp = s;
      sort(tmp.begin(), tmp.end());
      if( s == tmp ){
        ans = i;
        break;
      }
      // cerr << i << endl;
    }
    cout << "Case #" << loop+1 << ": " << ans << endl;
  }


  return 0;
}
