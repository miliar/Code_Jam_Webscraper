#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen ("in.txt","r",stdin);
    freopen ("out.txt","w",stdout);
    int t,p;
    cin>>t;
    for(p=1;p<=t;p++)
    {
    	int i,j,n,pp;
    	string s,ans;
        cin>>s;
        n=s.length();
        if(s.size()==1)
        {
            cout<<"Case #"<<p<<": "<<s<<"\n";
        }
        else
        {           
        	pp=n;
        	for(i=0;i<n-1;i++)
            {
            	if(s[i]>s[i+1])
                {
                	pp=i;
                	break;
          		}
        	}
        if(pp!=n)
            {
            for(j=pp;s[j]==s[j-1];j--);
            s[j]--;
            for(j++;j<s.size();j++)
                {
                s[j]='9';
            }
        }
            ans="";
            int k=0;
            cout<<"Case #"<<p<<": ";
            for(k=0;s[k]=='0' && k<s.size();k++);
            for(;k<s.size();k++)
            {
                cout<<s[k];
            }
            cout<<"\n";
        }
    }
	return 0;
}
