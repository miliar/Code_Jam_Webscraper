#include <bits/stdc++.h>
using namespace std;

void repl(string &s,int pos,char c){
  for(int i=pos;i<s.size();i++) s[i] = c;
}

int main(){
  int T; cin >> T;
  for(int ttt=1;ttt<=T;ttt++){

    string s; cin >> s;
    int n = s.size();
    string res(n,'0');
    int num = 1;
    int pos = 0;
    for(;num<10&&pos<n;){
      repl( res, pos, num+'0' );
      if( stol(res) > stol(s) ) {
        num--;
        repl( res, pos, num+'0' );
        pos++;
      } else {
        num++;
      }
    }

    cout << "Case #" << ttt << ": ";
    cout << stol(res) << endl;
  }
}