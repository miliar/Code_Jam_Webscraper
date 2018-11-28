#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;
  cin >> n;

  for(int i = 0; i < n; i++){
    string s;
    cin >> s;

    string t = s;

    int orig_size = s.size();
    char orig_first = s[0];

    if(orig_size == 1){
      cout << "Case #" << i+1 << ": " << s << endl;
      continue;
    }

    for(int j = orig_size-1; j > 0; j--){
      if(s[j] < s[j-1]){
        s[j] = '9';
        s[j-1]--;
      }
    }

    while(s[0] == '0'){
      s.erase(s.begin());
    }

    if(orig_size > s.size() || orig_first > s[0]){
      for(int j = 1; j < s.size(); j++){
        s[j] = '9';
      }
    }

    if(orig_size == s.size()){
      bool magic  = false;
      for(int j = 0; j < s.size(); j++){
        if(magic){
          s[j] = '9';
        }
        if(s[j] != t[j]){
          magic= true;
        }
      }
    }

    cout << "Case #" << i+1 << ": " << s << endl;
  }
}
