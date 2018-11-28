#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int t, i,j,k,l,count, flag;
	string S;
	cin >> t;
	for(i=1;i<=t;i++) {
	    cin >> S;
	    cin >> k;
	    count=0;
	    flag=1;
	    for(j=0;j<S.length();j++ ) {
	        if(S[j]=='-') {
	            count++;
	            for(l=0; l<k;l++) {
	               if(S[j+l]=='-') {
	                    S[j+l]='+';
	               }
	               else  S[j+l]='-';
	               }
	               
	            }
	    }
	    if(strstr(S.c_str(),"-"))
                       {
   cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
                         }
   else cout << "Case #" << i << ": " << count << endl;
	}}
