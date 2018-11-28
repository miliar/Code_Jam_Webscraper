#include <bits/stdc++.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int count = 1;count <=T;count++)
	{
	    long long Number;
	    cin>>Number;
	    string mystring = to_string(Number);
	    int n = mystring.length();
	    
	    for(int i = n-2;i>=0;i--)
	    {
	        if(mystring[i] <= mystring[i+1])
	        continue;
	        
	        mystring[i] = mystring[i]  - 1  ;
	        for(int j = i+1;j<n;j++)
	        mystring[j] = '9';
	        
	    }
	    
	    cout<<"Case #"<<count<<": ";
	    Number = stoll(mystring);
	    cout<<Number<<endl;
	}
	return 0;
}
