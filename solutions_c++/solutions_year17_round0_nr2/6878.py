#include <iostream>
#include <string>
using namespace std;

int main() {
		int t;
	cin>>t;
	for(int ti=1;ti<=t;ti++)
	{
	    string s;
	    cin>>s;
	    int len;
	    len=s.size();
	    for(int i=0;i<len;i++)
	        for(int j=0;j<len-1;j++)
	        {
	            if(s[j]>s[j+1])
	                {
	                    s[j]--;
	                    for(int k=j+1;k<len;k++)
	                    {
	                        s[k]='9';
	                        
	                    }
	                    break;
	                }
	        }
	  if(s[0]=='0')
	    s.erase(0,1);
	   cout<<"Case #"<<ti<<": "<<s<<endl;
	}
	return 0;
}
