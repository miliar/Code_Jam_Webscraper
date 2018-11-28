#include<bits/stdc++.h>
using namespace std;

int T;
string S;

int main(){
  cin >> T;
  for(int t=1; t<=T; t++){
    cin >> S;
    for(int i=S.length()-1; i>0; i--){
      if(S[i] < S[i-1]){
        S[i-1]--;
        for(int j=i; j<S.length(); j++){
          S[j] = '9';
        }
      }
    }
    cout << "Case #" << t << ": ";
    int i;
    for(i=0; i<S.length(); i++){
      if(S[i] != '0')
        break;
    }
    for(int j=i; j<S.length(); j++){
      cout << S[j];
    }
    if(i == S.length())
      cout << '0';
    cout << endl;
  }
}
