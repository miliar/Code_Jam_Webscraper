#include <bits/stdc++.h>  
using namespace std;
int main() {
  int T,k,count,l,i,j,flag,flip;
  string s;
  cin >> T;  
  for (k = 1; k <= T; k++) {
  	count=0;
  	flag=0;
    cin >> s >> flip;
    l=s.length();
    
	    for(i=0;i<=l-flip;i++){
	    	if(s[i]=='-'){
	    		count++;
	    		for(j=0;j<flip;j++){
	    			if(s[i+j]=='-'){
						s[i+j]='+';
					}
					else{
						s[i+j]='-';
					}
				}	
			}
		}
			 
    	for(i=0;i<l;i++){
    		if(s[i]=='-'){
    			flag++;
			}
		}
		if(flag==0){
			cout << "Case #" << k << ": " <<count<<endl;
   	 	}
   	 	else{
   	 		cout << "Case #" << k << ": " <<"IMPOSSIBLE"<<endl;
   	 	}
  }
  return 0;
}
