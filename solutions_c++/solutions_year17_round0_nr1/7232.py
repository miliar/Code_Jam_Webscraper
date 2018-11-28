#include<bits/stdc++.h>
using namespace std;

bool check(string str) {
  for(int i=0; i< str.length(); i++)
    if(str[i] == '-')
      return false;
  return true;
}

string modifyString(string str, int start, int end) {
  for(int i=start; i<=end; i++){
    if(str[i] == '+') str[i] = '-';
    else str[i] = '+';
  }
  return str;
}

int main() {

  freopen("A-large.in", "r" , stdin);
  freopen("out", "w", stdout);

  int t;
  cin >> t;

  for(int tt = 1; tt<= t; tt++) {
    string str;
    int s;
    cin >> str >> s;
    int count = 0;

    for(int i=0; i< str.length() ; i++) {
      //cout << str << " " << s << " " << count << "\n";
      if(str[i] == '-' &&  (i+s-1) < str.length()) {
        count++;
        str = modifyString(str, i, i+s-1);
      }
    }

    cout << "Case #"<<tt<<": ";
    if(!check(str)) cout << "IMPOSSIBLE\n";
    else cout << count << "\n";
  }

  return 0;
}
