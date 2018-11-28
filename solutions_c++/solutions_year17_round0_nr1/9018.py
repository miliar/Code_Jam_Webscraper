#include<bits/stdc++.h>
using namespace std;
int solve(string s,int k)
{
	int len=s.size(),ans=0;
	for(int i=0;i<len-k+1;i++)
	{	if(s[i]=='-')
		{
			ans++;
			for(int j=0;j<k;j++)
			{
				if(s[j+i]=='+')s[i+j]='-';
				else s[j+i]='+';
			}
		}
		
	
	}
	//cout<<s<<endl;
	for(int i=len-k;i<len;i++)
	{
		if(s[i]=='-')
		return -1;
	
	}
	return ans;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("GCJ-OP.txt","w",stdout);
	int t;
	cin>>t;
	for(int T=1;T<=t;T++)
	{
		string s;int k;
		cin>>s>>k;
		int ans1=solve(s,k);
		reverse(s.begin(),s.end());
		int ans2=solve(s,k);
//		cout<<ans1<<" "<<ans2<<endl;
		if(ans1>=0 && ans2>=0)
		{
			cout<<"Case #"<<T<<": "<<min(ans1,ans2)<<endl;;
		}
		else if(ans1<0 && ans2<0)
		{
			cout<<"Case #"<<T<<": "<<"IMPOSSIBLE"<<endl;;
		}
		else
		{
			cout<<"Case #"<<T<<": "<<max(ans1,ans2)<<endl;;
		}						
	}
}






