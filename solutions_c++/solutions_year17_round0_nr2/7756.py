#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
typedef long long ll;
#define F first
#define S second
#define N 2020

int t[N];

int main(){
  int T; cin >> T;
  for(int j=1; j<=T; ++j){
    string s; cin >> s;
    reverse(s.begin(), s.end());
    for(unsigned int i=0; i<s.size()-1; ++i){
      if(s[i] < s[i+1]){
        if(s[i+1]=='0') continue;
        --s[i+1];
        for(unsigned int k=0; k<=i; ++k) s[k]='9';
      }
    }
    cout << "Case #" << j << ": ";
    int n = s.size()-1;
    if(s[n]=='0') --n;
    for(int i = n; i>=0; --i){
      cout << s[i];
    }
    cout << "\n";
  }
}
