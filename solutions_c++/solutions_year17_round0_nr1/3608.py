#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long t,o,count,flag,i,j,k;
	string s;
	cin>>t;
	for(o=0;o<t;o++)
	{
	    cin>>s>>k;
	    count=0;
	    flag=0;
	    for(i=0;i<=s.size()-k;i++)
	    {
	        if(s[i]=='-')
	        {
	            count++;
	            for(j=i;j<i+k;j++)
	            if(s[j]=='-')
	            s[j]='+';
	            else s[j]='-';
	        }
	    }
	    for(;i<s.size();i++)
	    if(s[i]=='-')
	    {
	        flag=1;
	        break;
	    }
	    cout<<"Case #"<<o+1<<": ";
	    if(flag==1)
	    cout<<"IMPOSSIBLE"<<endl;
	    else cout<<count<<endl;
	}
	return 0;
}
