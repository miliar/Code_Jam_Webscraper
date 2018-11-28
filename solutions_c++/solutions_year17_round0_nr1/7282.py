#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long t,i,j,k,count,p,l,x;
	int flag;
	
	cin>>t;
	
	for(p=1;p<=t;p++)
	{
	    flag = 0;
	    string s;
	    cin>>s;
	    cin>>k;
	    count = 0;
	    l = 0;
	    while(s[l]!='\0')
	        l++;
	    l++;
	    
	    for(i=0;i<l;i++)
	    {
	        if(s[i]=='-'&&l-(i+1)<k)
	        {
	            cout<<"Case #"<<p<<": "<<"IMPOSSIBLE"<<endl;
                flag = 1;
	            break;
	        }
	        else if(s[i]=='-')
	        {
	            s[i] = '+';
	            
	            x = 0;
	            for(j=i+1;x<k-1;x++,j++)
	            {
	            if(s[j]=='-')
	                s[j] = '+';
	            else
	                s[j] = '-';
	            }   
	            count++;
	        }
	    }
	    
	    if(flag==0)
	        cout<<"Case #"<<p<<": "<<count<<endl;
	}
	return 0;
}
