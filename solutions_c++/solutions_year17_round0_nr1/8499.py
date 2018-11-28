#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
	    string s;
	    int k,count=0,j,b=0;
	    cin>>s>>k;
	    for( j=0;j<=(s.size()-k);j++){
	        if(s[j]=='+');
	        else{
	            count++;
	            for(int l=j;l<j+k;l++)
	            if(s[l]=='-')s[l]='+';
	            else s[l]='-';
	        }
	    }
	    for(int l=j;l<s.size();l++)
	    if(s[l]=='-'){b=1;cout<<"Case #"<<i<<": IMPOSSIBLE\n";break;}
	    if(b==0)cout<<"Case #"<<i<<": "<<count<<endl;
	    
	}
	return 0;
}
