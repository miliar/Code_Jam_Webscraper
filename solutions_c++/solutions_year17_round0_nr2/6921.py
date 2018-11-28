
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string>
#include <cstdlib>

using namespace std;

int main(){

    int T,j=1;
    string N;
    freopen ("in.in","r",stdin);
    freopen ("out.out","w",stdout);
    cin>>T;
    while(j<=T){
    	cin>>N;
    	if(N.length()>=2){
    		for(int i = N.length()-1;i>0;i--){
    			if(N.at(i) < N.at(i-1)) {//two consecutive digits in decreasing order.
    				int digit = N.at(i-1)-1 -48;
					string str = to_string(digit);
    				N.replace(i-1,1, str); // decrement first digit
    				N.replace(i,1, "9");
    			}
    		}
    		//go from front to end to check again
    		for(int i=0;i<N.length()-1;i++){
    			if(N.at(i) > N.at(i+1)){ //two consecutive digits in decreasing order
    				N.replace(i+1,1,"9");
    			}
    		}

    	}
    	// remove leading zero
    	for(int i=0;i<N.length();i++){
    		if(N.at(i)!='0')
    			break;
    		N.replace(i,1,"");
    	}
        cout<<"Case #"<<j<<": "<<N<<endl;
        j++;
    }
    return 0;
}
