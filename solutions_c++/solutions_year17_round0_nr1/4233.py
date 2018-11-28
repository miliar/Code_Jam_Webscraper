#include <iostream>
using namespace std;

int main() {
	int f=0,t,k,i,j,co;
	string s;
	cin>>t;
	while(t--){
        f++;
	    cin>>s>>k;
	    co=0;
	    for(i=0;i<=s.length()-k;i++){
	        if(s[i]=='-'){
	            co++;
	            for(j=i;j<i+k;j++){
	                if(s[j]=='-')
	                s[j]='+';
	                else
	                s[j]='-';
	            }
	            
	        }
	    }
	    for(i=0;i<s.length();i++){
	        if(s[i]=='-'){
	            cout<<"Case #"<<f<<": IMPOSSIBLE\n";
	            break;
	        }
	    }
	    if(i==s.length())
	    cout<<"Case #"<<f<<": "<<co<<"\n";
	}
	return 0;
}
