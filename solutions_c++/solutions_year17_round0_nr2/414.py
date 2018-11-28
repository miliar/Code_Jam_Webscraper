#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 300030;
const ll  MODD = 1000000007;

int A[MAX_N];

string f(string s){
  if(s.size() == 0)
    return s;
  if(s == "0") return "";
  
  string ans = "";
  while(s.size() && s.find('0') != string::npos){
    ans = string(s.length()-s.find('0'),'9') + ans;
    stringstream ss(s.substr(0,s.find('0')));
    long long x; ss >> x; s = to_string(x-1);
    if(s == "0") s = "";
  }
  
  for(int i=0;i+1<(int)s.size();i++)
    if(s[i] > s[i+1]){
      ans = string(s.size()-i-1,'9') + ans;
      stringstream ss(s.substr(0,i+1));
      long long x; ss >> x; s = to_string(x-1);
      return f(s) + ans;
    }
  
  return s + ans;
}

string do_case(){
  string s; cin >> s;
  return f(s);  
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(9);
  
  int T,C=1; cin >> T;
  
  while(T--) {
    cout << "Case #" << C++ << ": ";
    cout << do_case() << endl;
    //do_case();
  }
  
  return 0;
}
