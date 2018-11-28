#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i,x,l) for(i=x;i<l;i++)
int main()
{
	ll int t,n,cur,i,j,k,fl,x;
	cin>>t;
	string s,ans;
	for(x=1;x<=t;x++)
	{
		cin>>n;
		
		//cout<<x<<" ";
		cout<<"Case #"<<x<<": ";
		
		s=to_string(n);
		if(s.length()==1)cout<<n<<endl;
		else
		{
		    fl=0;
			for(i=0;i<s.length()-1;i++)
			{
				if(s[i]>s[i+1])
				{
					if(s[i]=='1')
					{
						for(j=0;j<s.length()-1;j++)cout<<"9";
						cout<<endl;
						fl=1;
						break;
					}
					else
					{
					    if(s[i+1]=='0')
					    {
					        s[i]=s[i]-1;
					        for(j=i+1;j<s.length();j++)s[j]='9';
					        for(j=i;j>0;j--)
					        {
					           // cout<<s[j-1]<<" ";
					            if(s[j-1]>s[j])
					            {
					                s[j-1]=s[j-1]-1;
					                s[j]='9';
					            }
					            else break;
					        }
					        cout<<s<<endl;
					        fl=1;
					        break;
					    }
					    s[i]=s[i]-1;
					    for(j=i;j>0;j--)
					    {
					        if(s[j-1]<=s[j])break;
					        else
					        {
					            s[j-1]=s[j-1]-1;
					            s[j]='9';
					        }
					    }
					    for(j=i+1;j<s.length();j++)s[j]='9';
					    cout<<s<<endl;
					    fl=1;
					    break;
					}
				}
			}
			if(fl==0)cout<<n<<endl;
		}
		
		
	} 
	return 0;

}