#include<bits/stdc++.h>
using namespace std;


bool check(string str){
  for(int i=1; i<str.length(); i++){
    if(str[i] < str[i-1]) {
      return true;
    }
  }
  return false;
}

string modify(string str) {
  int j = -1;
  for(int i=1; i<str.length(); i++){
    if(str[i] < str[i-1]) {
      j = i;
      break;
    }
  }
  if(j == -1) return str;

  str[j-1]--;
  for(; j< str.length(); j++)
    str[j] = '9';

  str.erase(0, min(str.find_first_not_of('0'), str.size()-1));

  return str;
}

int main() {

  freopen("B-large.in" , "r" , stdin);
  freopen("out" , "w" , stdout);

  int t;
  cin >> t;

  for(int tt=1; tt<=t ;tt++) {

    string s;
    cin >> s;

    while(check(s))
      s = modify(s);
    cout << "Case #"<<tt<<": " << s << "\n";
  }



  return 0;
}
