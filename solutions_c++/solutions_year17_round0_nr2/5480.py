#include <iostream>
#include <string>
using namespace std;

int main(){
  int T;
  cin >> T;
  for(int i=0; i<T; ++i){    
    string N; cin >> N;

    for(int j=0; j<N.size()-1; ++j){
      if(N[j]>N[j+1]){
	N[j]-=1;

	int k=j;
	while(k>0 && N[k]<N[k-1]){
	  k--;
	  N[k]-=1;
	}

	for(int m=k+1; m<N.size(); ++m) N[m]='9';
	break;
      }
    }

    if(N[0]=='0')N.erase(0, 1);

    string ans=N;
    cout << "Case #" << i+1 << ": " << ans << endl;
  }
  
  return 0;
}

