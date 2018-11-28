#include <bits/stdc++.h>
using namespace std;

int main() 
{
	int t,operations;
	cin>>t;operations=t;
	while(t--)
	{
	    int kameena;
		string chootstring;
	    int uttar=0;
	    cin>>chootstring;
	    cin>>kameena;
	    
	    
	    for(int i=0;i<=chootstring.length()-kameena;i++)
	         {if(chootstring[i]!='+')
	    
		         {for(int j=i;j<i+kameena;j++)
	    
		               {if(chootstring[j]=='+')
	                        chootstring[j]='-';
	                        else
	                        chootstring[j]='+';
	                                               }
	    uttar++;    
	    }
	        
	    }
	    int jhanda=0;
	   
	 for(int i=0;i<chootstring.length();i++)
	     if(chootstring[i]=='-')
	 
	            {cout<<"Case #"<< operations-t<<": "<<"IMPOSSIBLE"<<endl;
	             jhanda=1;
	            break;
	                       }
	     if(jhanda==0)
	        cout<<"Case #"<< operations-t<<": "<<uttar<<endl;
	}
}
