#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define f first
#define s second
#define mp make_pair
#define max 200005           
#define num 5000000
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0)
using namespace std;

int main() {
	int t,i,k,x,l,ans,y,r;
	char s[15],c;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		cin>>s>>k;
		l=strlen(s);
		ans=0;
		r=0;
		//cout<<s<<'\n';
		if(l==2)
		{
			if(s[0]=='+' && s[1]=='+')
			  cout<<"Case #"<<i<<": 0"<<'\n';
			else if(s[0]=='-' && s[1]=='-' && k==2)
			  cout<<"Case #"<<i<<": 1"<<'\n';
			else
			  cout<<"Case #"<<i<<": IMPOSSIBLE"<<'\n';
			}
		for(x=0;x<=l-k;x++)
		{
			if(s[x]=='-')
			{
				for(y=x;y<x+k;y++)
				{
					if(s[y]=='-')
					 s[y]='+';
					else
					 s[y]='-';
					
				}
				ans++;
			}
		}
        //cout<<ans;		
		c=s[l-1];
		for(x=l-k;x<l-1;x++)
        {
        	if(s[x]!=c)
        	 {cout<<"Case #"<<i<<": IMPOSSIBLE"<<'\n';
        	  r++;
        	  break;
        	 }
        }	
        
        if(r==0)
        {
        	cout<<"Case #"<<i<<": "<<ans<<'\n';
        }
	}
	// your code goes here
	return 0;
}