#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
using namespace std;
int main() {
  int t;
  cin>>t;
  for(int l = 1; l <= t; l++) {
    char s[1001];
    cin>>s;
    int k, cn = 0, fn = 0, ans = 0;
    cin>>k;
    for(int i = 0; s[i] != '\0'; i++) {
      if(s[i] == '-') {
        cn++;
        fn = 1;
        if(cn == k) {
          cn = 0;
          ans++;
          fn = 0;
        }
      }
      if(s[i] == '+' && fn == 1) {
        int temp = i, c = 0;
        for(int j = i; j < temp + k - cn && s[j] != '\0'; j++) {
          if(s[i] == '+')
            s[i] = '-';
          else
            s[i] = '+';
          i++;
        }
          cn = 0;
          ans++;
          i = temp - 1;
      }
    }
    if(ans == -1 || cn != 0)
      cout<<"Case #"<<l<<": IMPOSSIBLE\n";
    else
      cout<<"Case #"<<l<<": "<<ans<<"\n";
  }
}
