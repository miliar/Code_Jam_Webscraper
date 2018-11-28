#include<iostream>
#include <bits/stdc++.h>
using namespace std;


int main() {
	int t,siz,p,change;
	char c;
	string s,ans;
	cin>>t;
	for(int k=0;k<t;k++){
	    cin>>s;
	    siz=s.size();
	    for(int i=0;i+1<siz;i++){
	        change=0;
	        //cout<<s<<endl;
	        if(s[i]-'0'>s[i+1]-'0'){
	            s[i]=s[i]-'0'+47;
        		i++;
    	        while(i<siz){
    	            s[i]='9';
    	            i++;
    	        }
    	            change++;
	        }
	        if(change>0 && s[0]!='0')i=-1;
	        //else cout<<"dn"<<endl;
	    }
	    //cout<<s<<endl;
	   // ans="";
	   // for(int i=siz-1;i>=0;i--){
	   //     if(s[i]=='0'){
	   //         while(i>0){
	   //             s[i]='9';
	   //             i--;
	   //         }
	   //         s[0]='0';
	   //         i--;
	   //     }
	   // }
	    cout<<"Case #"<<k+1<<": ";
	    for(int i=0;i<siz;i++){
	        if(s[i]!='0')cout<<s[i];
	    }
	    cout<<endl;
	}
	
	return 0;
}
