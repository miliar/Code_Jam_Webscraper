#include <bits/stdc++.h>  
using namespace std;
int main() {
  int T,i,j,l,k;
  string s;
  cin >> T;  
  for (int k = 1; k <= T; k++) {
	    cin>>s;
	    l=s.length();
	    for(i=l-1;i>0;i--){
	    	
	    	if(s[i-1]>s[i]){
	    		s[i-1]=s[i-1]-1;
	    		
	    		for(j=i;j<l;j++){
	    			s[j]='9';
				}
			}
		} 
	    cout << "Case #" << k << ": " <<atoll(s.c_str())<<endl;
  }
  return 0;
}
