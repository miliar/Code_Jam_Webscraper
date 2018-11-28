#include <iostream>
#include <string>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int ti=1;ti<=t;ti++)
	{
	    int k=0,len,c=0,f=1;
	    string s;
	    cin>>s>>k;
	 //   cout<<s<<" "<<s.size()<<endl;
	    len=s.size();
	    
	    for(int i=0;i<=len-k;i++)
	    {
	        if(s[i]=='-')
	        {
	            c++;
	            for(int j=i;j<k+i;j++)
	                {
	                    if(s[j]=='-')
	                        s[j]='+';
	                    else
	                        s[j]='-';
	                   
	                }
	               
	        }
	    }
	    for(int i=0;i<len;i++)
	        if(s[i]=='-')
	            f=0;
	   if(f==1)
	    cout<<"Case #"<<ti<<": "<<c<<endl;
	   else
	    cout<<"Case #"<<ti<<": "<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
