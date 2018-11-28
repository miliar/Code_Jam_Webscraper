#include <iostream>
using namespace std;

int main() 
{
	int t;
	cin>>t;
	for (int test=1;test<=t;test++)
	{
	    string s;
	    int k,count=0,flag=0;
	    cin>>s>>k;
	    for (int i=0;i<=s.size()-k;i++)
	    {
	        if (s[i]=='-')
	        {
	            for (int j=i;j<i+k;j++)
	            {
	                if (s[j]=='-')
	                    s[j]='+';
	                else
	                    s[j]='-';
	            }
	            count++;
	        }
	    }
	    for (int i=0;i<s.size();i++)
	    {
	        //cout<<s[i];
	        if (s[i]=='-')
	        {
	            flag=1;
	            break;
	        }
	    }
	    if (flag==0)
	    cout<<"Case #"<<test<<": "<<count<<endl;
	    else
	    cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
	}
	return 0;
}
