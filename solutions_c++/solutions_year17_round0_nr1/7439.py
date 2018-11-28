#include <iostream>
#include <string>
using namespace std;
int main() {
  int t, K;
  string S;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> S >> K; 
    int flips = 0;
    bool fail = false;
    for(int j=0;j<S.size()&&!fail;j++){
    	if(S[j]=='-'){
    		if(j>=S.size()-K+1){
		    	cout << "Case #" << i << ": IMPOSSIBLE"<< endl;
		    	fail = true;
    		}
    		else{
		    	for(int m=j;m<K+j;m++){
		    		S[m]=S[m]=='-'?'+':'-';
		    	}
		    	flips++;
	    	}
		}
    }
    if(!fail){
    	cout << "Case #" << i << ": " << flips << endl;
	}
  }
  return 0;
}