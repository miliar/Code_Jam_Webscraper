#include <cmath>
#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    int t;
	cin>>t;
	for(int j=1;j<=t;j++){
		long n,f=0;
		cin>>n;	
	    string no = to_string(n);
		int rest=no.length(),i;
	    for(i=no.length()-2;i>=0;i--){
	    	if(no[i]>no[i+1]){
				rest=i+1;
				no[i]--;
			}
		}
		for(i=0;i<rest;i++){
			f=f*10+ (no[i]-'0');  
	    }	
		for(;i<no.length();i++){
			f=f*10+ 9;  
	    }
		cout<<"Case #"<<j<<": "<<f<<endl;
	}    
    return 0;
}

