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
	    int count=0;
	    string s;	
	    cin>>s;
	    int k;
	    cin>>k;	
	    int i;
	    bool flag=false; 	
	    for(i=0;i<=s.size()-k;i++){
		if(s[i]=='-'){
			count++;
			for(int j=1;j<k;j++){
				s[i+j]=((s[i+j]=='+')?'-':'+');
			}
		}
	    }
	    for(;i<s.size();i++){
		if(s[i]=='-'){
			flag=true;
			break;
		}		
	    }
	    cout<<"Case #"<<j<<": ";	
	    if(flag==true)
		cout<<"IMPOSSIBLE"<<'\n';
	    else
		cout<<count<<'\n';				     	    
   } 	
}

