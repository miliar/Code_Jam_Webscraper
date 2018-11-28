#include <iostream>
using namespace std;



int main() {
	// your code goes here
	long o,t,i,j;
	string s;
	cin>>t;
	for(o=1;o<=t;o++)
	{
	    cin>>s;
	    for(i=1;i<s.size();i++)
	    {
	        if(s[i]=='0' || s[i]<s[i-1])
	        {
	            s[i]='9';
	            j=i-1;
	            
	            while(j>0)
	            {
	                if(s[j]=='1')
	                {
	                    s[j]='9';
	                    j--;
	                   
	                    
	                }
	                else
	                {
	                    s[j]--;
	                    if(s[j]<s[j-1])
	                    {
	                        s[j]='9';
	                        j--;
	                        
	                    }
	                    else
	                    break;
	                }
	            }
	            if(j==0)
	            {
	                if(s[j]=='1')
	                s[j]='0';
	                else s[j]--;
	            }
	            for(;i<s.size();i++)
	            s[i]='9';
	            
	        }
	        
	    }
	    cout<<"Case #"<<o<<": ";
	    if(s[0]=='0')
	    {
	        for(i=1;i<s.size();i++)
	        cout<<s[i];
	        cout<<endl;
	    }
	    else cout<<s<<endl;
	}
	return 0;
}
