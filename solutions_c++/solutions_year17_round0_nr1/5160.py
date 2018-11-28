#include <iostream>
#include <string>
#include <cstring>
using namespace std;

int main() {
	long long int n,i,j,k,l,h,cnt,t,g=1;
	string mystring;
	cin>>n;
	for(i=0;i<n;i++)
	{
	    cin>>mystring;
	    cin>>k;
	  
        char * cstr = new char [mystring.length()+1];
        strcpy (cstr, mystring.c_str());

	    l=mystring.length();
	    
	    cnt=0;
	    for(j=0;j<=l-k;j++)
	    {
	  
	        if(cstr[j]=='-')
	        {
	            
	            cnt++;
	            for(h=j;h<j+k;h++)
	            {
	                if(cstr[h]=='-')
	                    cstr[h]='+';
	                else
	                    cstr[h]='-';
	            }
	        }
	        
	    }
	    t=0;
	    for(h=l-k;h<l;h++)
	    {
	        if(cstr[h]=='-')
	        {
	           
	            t=1;
	            break;
	        }
	    }
	    if(t==1)
	    {
	        cout<<"Case #"<<g<<": "<<"IMPOSSIBLE"<<"\n";
	        g++;
	    }
	    else
	    {
	       cout<<"Case #"<<g<<": "<<cnt<<"\n";
	       g++;
	    }
	    
	}
	return 0;
}
