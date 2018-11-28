#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <map>
#include <cmath>
#include <vector>
#include <algorithm>
using namespace std;  // since cin and cout are both in namespace std, this saves some text


int main() {

  int t;
  string N;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  
  for (int i = 1; i <= t; ++i) {
    cin >> (N) ;  // read n and then m.
    
    bool flag = true;
    for(int i =0; i<N.length()-1;i++) {
      if(N[i] > N[i+1]) {
        flag =false;
      }
    }
    if(flag){
      //cout << N << ' ' << N << endl;
      cout << "case #" <<i << ": " << N << endl;
      continue;
    }

    if(N.length() == 1) {
    }
    else {
      string s = N;
      for(int i = N.length()-1;i>-1;i--) {
        if ( i==N.length()-1) {
          s[i]='9';
        }
        else if (s[i] <= '1' && i!=0 ){
          s[i] = '9';
        }
        else if (s[i]<= '1' && s[i+1] == '9' && i==0) {
          s[i] = '0';
        }
        else if (s[i+1] == '9' ) {
          s[i] = char(N[i] - 1);
        }
        else if (s[i+1] != '9'){
          if( s[i] > s[i+1] ){
            s[i+1] = '9';
            s[i] = s[i] - 1;
          }
        }
      }
      bool zeroFlag = true;
      string finalString = "";
      for(int i=0;i<s.length();i++) {
        if(zeroFlag && s[i] == '0'){
        }
        else {
          zeroFlag = false;
          finalString += s[i];
        }
      }
      //cout << N<< " "  << s << endl;
      //cout << finalString << endl;
      cout << "case #" <<i << ": " << finalString << endl;
      // test string
    }
  }
}
