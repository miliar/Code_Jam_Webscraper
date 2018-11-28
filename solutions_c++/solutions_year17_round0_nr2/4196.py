#include <iostream>
#include <string>
using namespace std;
long long StrToNum(string* s){
  int l = (int)(*s).length();
  long long res = 0;
  for(int i=0; i<l; i++){
    res*=10;
    res+=((*s)[i]-'0');
  }
  return res;
}
long long cal(string* s) {
  int l = (*s).length();
  int idx = 0;
  bool flag= true;
  for (int i=0; i<l-1; i++) {
    if ((*s)[i] > (*s)[i+1]) {
      flag = false;
      break;
    }else if ((*s)[i] < (*s)[i+1]) {
      idx = i+1;
    }
  }
  if(!flag){
    (*s)[idx]--;
    for(int i=idx+1; i<l; i++){
      (*s)[i] = '9';
    }
  }
  return StrToNum(s);
}

int main() {
  int T;
  cin >> T;
  for(int num = 1; num <= T; num++) {
    string s;
    cin >> s;
    long long res = cal(&s);
    cout << "Case #" << num << ": " << res << endl;
  }
}
