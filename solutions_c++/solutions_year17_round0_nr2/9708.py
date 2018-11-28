#include <bits/stdc++.h>

#define ll long long
#define debug(x) cout<<#x<<": "<<x<<endl

using namespace std;

int main() {
  
  int T;
  cin>>T;

  for(int t = 1; t <= T; ++t) {

    string s;
    cin>>s;

    int n[18];
    memset(n, 0, sizeof n);
    
    for(int i = 17, j = s.size() - 1; j >= 0; --i, --j) {
      n[i] = s[j] - '0';
    }

    for(int i = 0; i < 20; ++i) {

      int pt = -1;
      for(int j = 1; j < 18; ++j) {
	if(n[j] < n[j - 1]) {
	  pt = j - 1;
	  break;
	}
      }

      if(pt == -1) break;
      
      --n[pt];
      for(int j = pt + 1; j < 18; ++j) {
	n[j] = 9;
      }
    }

    cout<<"Case #"<<t<<": ";
    int i = 0;
    while(n[i] == 0) {
      ++i;
    }

    for( ; i < 18; ++i) {
      cout<<n[i];
    }
    cout<<endl;
	
  }
  
  return 0;
}
