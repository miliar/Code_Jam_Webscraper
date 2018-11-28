#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
	int T,i,j,k,n;
	string s;
	cin>>T;
	for(k=1;k<=T;k++)
	{
	    cin>>s;
	    n=s.size();
	    for(i=n-1;i>0;i--)
	    if(s[i]<s[i-1])
	    {
	        s[i-1]=s[i-1]-1;
	        for(j=i;j<n;j++)
	        s[j]='9';
	    }
	    while(s[i++]=='0');
	    cout<<"Case #"<<k<<": ";
	    for(j=i-1;j<n;j++) cout<<s[j];
	    cout<<"\n";
	}
	return 0;
}

