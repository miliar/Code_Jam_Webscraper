#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int MAX_N = 300030;
const ll  MODD = 1000000007;

int A[MAX_N];

void do_case(){
  string s; cin >> s;
  int t,ans=0; cin >> t;
  for(int i=0;i+t<=s.length();i++)
    if(s[i] == '-'){
      ans++;
    for(int j=0;j<t;j++)
      s[i+j] ^= 6;
  }

  if(s.find('-') != string::npos){
    cout << "IMPOSSIBLE" << endl;
    return;
  }
  cout << ans << endl;
}

int main(){
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(9);
  
  int T,C=1; cin >> T;
  
  while(T--) {
    cout << "Case #" << C++ << ": ";
    do_case();
    //do_case();
  }
  
  return 0;
}
