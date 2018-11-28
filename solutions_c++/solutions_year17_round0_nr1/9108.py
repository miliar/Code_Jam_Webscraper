#include <bits/stdc++.h>  
using namespace std;
int main() {
  int T,k,cnt,l,i,j,checkvar,chng;
  string S;
  cin >> T;  
  for (k = 1; k <= T; k++) {
  	cnt=0;
  	checkvar=0;
    cin >> S >> chng;
    l=S.length();
    
	    for(i=0;i<=l-chng;i++){
	    	if(S[i]=='-'){
	    		cnt++;
	    		for(j=0;j<chng;j++){
	    			if(S[i+j]=='-'){
						S[i+j]='+';
					}
					else{
						S[i+j]='-';
					}
				}	
			}
		}
			 
    	for(i=0;i<l;i++){
    		if(S[i]=='-'){
    			checkvar++;
			}
		}
		if(checkvar==0){
			cout << "Case #" << k << ": " <<cnt<<endl;
   	 	}
   	 	else{
   	 		cout << "Case #" << k << ": " <<"IMPOSSIBLE"<<endl;
   	 	}
  }
  return 0;
}
