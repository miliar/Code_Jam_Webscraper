#include "bits/stdc++.h"

using namespace std;


int rev(string s, int k) {
  int sz = (int)s.size();
  int flip = 0;
  for(int i = 0 ;i< sz ; i++) {
    if(s[i] == '-' ) {
      if((sz-i) >= k) {
        flip++;
        for(int j = i ; j < i+k ; j++) {
          s[j] = (s[j] == '-' ? '+' : '-');
        }
      } else {
        return -1;
      }
    }
  }
  return flip;
}

int main(int argc, char const *argv[])
{
  freopen("AL.in", "r", stdin);
  freopen("AL.out", "w", stdout);
  int k;
  string s;
  int tcase,cas=1;
  cin>>tcase;
  while(tcase--) {
    cin>>s>>k;

    int sol = -1;

    sol = rev(s, k);
    reverse(s.begin(), s.end());
    int tmp = rev(s, k);

    if(sol == -1) tmp = sol;
    else {
      if(tmp != -1 && tmp < sol) sol = tmp; 
    }

    cout<<"Case #"<<cas++<<": ";

    if(sol == -1) {
      cout<<"IMPOSSIBLE"<<endl;
    } else cout<<sol<<endl;
  }

  return 0;
}