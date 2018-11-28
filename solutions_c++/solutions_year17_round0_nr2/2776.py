#include<bits/stdc++.h>
using namespace std;

typedef long long lld;

lld solve(string s)
{
	lld ans=0;
	
	for(lld i=0;i<s.size()-1;i++)
	{
		if(s[i]>=s[i+1])
		{
			lld temp=0;
			lld temp2=0;
		    for(lld j=i;j<s.size();j++)
			{
				temp=temp*10+(s[j]-'0');
				temp2=temp2*10+1;
			}
			temp2=temp2*(s[i]-'0');
		    
		    if(temp2>temp)
		    {
		    	s[i]=s[i]-1;
		    	ans=ans*10+s[i]-48;
		    	i=i+1;
		    	for(lld j=i;j<s.size();j++)
		    	{
		    		ans=ans*10+9;
		    	}
		    	return ans;
		    }
		    
		    
		}
		
		ans=ans*10+(s[i]-48);
	
	}
	ans=ans*10+(s[s.size()-1]-48);
	return ans;
}




int main()
{
   freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);
	
	lld t;
	cin>>t;
	for(lld tc=1;tc<=t;tc++)
	{
		lld n;
		cin>>n;
		
		lld temp=n;
		string s;
		
		while(temp)
		{
			lld r=temp%10;
			s.push_back(r+48);
			temp=temp/10;
		}
		
		reverse(s.begin(),s.end());
		lld ans=solve(s);
		
		cout<<"Case #"<<tc<<": "<<ans<<"\n";
	}

}
