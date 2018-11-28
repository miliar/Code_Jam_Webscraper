#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	    string s;
	    cin>>s;
	    int k,ans=0,flag=0;
	    cin>>k;
	    if(k>s.length())
        cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        else
        {
	    for(int j=0;j<s.length()-k+1;j++)
	    {
	        if(s[j]=='+')
	        continue;
	        if(s[j]=='-')
	        {
	            ans++;
	            for(int h=j;h<j+k;h++)
	            {
	                if(s[h]=='+')
	                s[h]='-';
	                else
	                s[h]='+';
	            }
	        }
	    }
	    for(int j=s.length()-k+1;j<s.length();j++)
	    {
	        if(s[j]=='+')
	        continue;
	        else
	        {
	        flag=1;
	        break;
	        }
	    }
	    if(flag==0)
	    cout<<"Case #"<<i<<": "<<ans<<endl;
	    else
	    cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }
	}
	return 0;
}
