#include <iostream>
#include <string>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i=0; i<T; ++i){
    int K, flip=0; string S;
    cin >> S; cin >> K;
    int c=0;
    while(c<S.size()-K+1){
      if(S[c]=='-'){
	flip++;
	for(int j=0; j<K; ++j){
	  S[c+j]=(S[c+j]=='+')?'-':'+';
	}
      }
      ++c;
    }

    bool ok=true;
    for(int j=0;j<S.size();j++)if(S[j]=='-')ok=false;
    string ans = ok ? to_string(flip) : "IMPOSSIBLE";
    
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  
  return 0;
}
