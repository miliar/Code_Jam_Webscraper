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
    string s;
    int k;
    cin >> s >> k;

    int ans = 0;
    for(int i=0; i<s.size(); i++){
      if( s[i] == '-' ){
        if( i+k > s.size() ) continue;
        ans++;
        for(int j=0; j<k; j++){
          if( s[i+j] == '-' ) s[i+j] = '+';
          else s[i+j] = '-';
        }
      }
    }
    bool f = true;
    for(int i=0; i<s.size(); i++){
      if( s[i] == '-' ) f = false;
    }
    cout << "Case #" << loop+1 << ": ";
    if( f ) cout << ans << endl;
    else cout << "IMPOSSIBLE" << endl;
  }


  return 0;
}
