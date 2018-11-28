#include<iostream>
using namespace std;

#define sz(X) (int)X.size()

int main() {
  int t;
  cin >> t;
  for(int c=1;c<=t;++c) {
    string s;
    cin >> s;
    int m = 10, l=sz(s);
    for(int i=sz(s)-1;i>=0;i--) {
      int d  = s[i] - '0';
      if (d > m) {
        l = i;
        m = d-1;
      } else m = d;
    }
    cout << "Case #" << c << ": ";
    for(int i=0;i<l;i++) { 
      cout << s[i];
    }
    if(l<sz(s)) {
      if(s[l] != '1') cout << (char)(s[l] - 1);
      for(int i=l+1;i<sz(s);i++) 
        cout << '9';
    }
    cout << endl;
  }
  return 0;
}
