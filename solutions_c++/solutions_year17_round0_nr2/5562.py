#include <iostream>
#include <string>

using namespace std;

int check(string& s){
  for(int i=1; i<s.length(); i++){
    if(s[i]-s[i-1] < 0)
      return i-1;
  }
  return -1;
}

string transform (int i, string& s){
  if(i==0 && s[i]=='1'){
    return string(s.length()-1, '9');
  }else{
    s[i] = (char)(s[i]-1);
    for(int j=i+1; j<s.length(); j++)
      s[j] = '9';
    return s;
  }
}

int main(){
  ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  string n;
  int i;
  for(int ind=0; ind<T; ind++){
    cin >> n;
    i=check(n);
    while(i >= 0){
      n = transform(i, n);
      i=check(n);
    }
    cout << "Case #" << (ind+1) << ": " << n << endl;
  }
  return 0;
}