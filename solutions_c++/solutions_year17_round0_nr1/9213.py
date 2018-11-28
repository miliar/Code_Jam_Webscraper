#include <bits/stdc++.h>

#define ll long long
#define debug(x) cout<<#x<<": "<<x<<endl

using namespace std;

int main() {
  
  ios_base::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int T;
  cin>>T;

  for(int t = 1; t <= T; ++t) {

    string s;
    cin>>s;

    int k;
    cin>>k;

    int bits[s.size()];

    for(int i = 0; i < s.size(); ++i) {
      if(s[i] == '+') {
	bits[i] = 1;
      }
      else {
	bits[i] = 0;
      }
    }
    
    int ans = 0;
    int exp[s.size()];
    memset(exp, 0, sizeof exp);
    int flips = 0;

    for(int i = 0; i <= s.size() - k; ++i) {
      //debug(i); debug(flips);
      
      if(flips % 2 == 1) {
	bits[i] = 1 - bits[i];
      }

      if(bits[i] != 1) {
	++flips;
	exp[i + k - 1] = -1;
	++ans;
	bits[i] = 1 - bits[i];
      }

      /*
      for(int i = 0; i < s.size(); ++i) {
	cout<<bits[i]<<" ";
      }
      cout<<endl;
      */
      
      flips = flips + exp[i];
    }    

    for(int i = s.size() - k + 1; i < s.size(); ++i) {
      if(flips % 2 == 1) {
	bits[i] = 1 - bits[i];
      }

      flips = flips + exp[i];
    }
    
    cout<<"Case #"<<t<<": ";

    int fk = 0;
    for(int i = 0; i < s.size(); ++i) {
      if(bits[i] == 0) {
	fk = 1;
	break;
      }
    }

    if(fk == 0) {
      cout<<ans<<endl;
    }
    else {
      cout<<"IMPOSSIBLE"<<endl;
    }
  }
  
  return 0;
}
