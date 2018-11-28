#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ggl.txt","w",stdout);
	int t;
	cin>>t;
	int kk=1;
	while(t--)
	{
		string s,s1;
		int k,cnt=0,cnt1=0;
		cin>>s>>k;
		int n=s.size();
		//cout<<n<<" ";
		s1=s;
		s1.size();

		for(int i=0;i<=n-k;i++)
		{
			if(s[i]=='-')
			{
				cnt++;
				for(int j=0;j<k;j++)
				{
					if(s[i+j]=='-')
					s[i+j]='+';
					else
					s[i+j]='-';
					
				}	
			}
			
		}
		for(int i=0;i<=n-k;i++)
		{
			if(s1[i]=='-')
			{
				cnt1++;
				for(int j=0;j<k;j++)
				{
					if(s1[i+j]=='-')
					s1[i+j]='+';
					else
					s1[i+j]='-';
					
				}	
			}
			
		}
		int flag=0,flag1=0;
		for(int i=0;i<n;i++)
		{
			if(s[i]=='-')
			{
				flag=1;
				break;
			}
		}
		for(int i=0;i<n;i++)
		{
			if(s1[i]=='-')
			{
				flag1=1;
				break;
			}
		}
		if(flag&&flag1)
		cout<<"Case #"<<kk<<": IMPOSSIBLE"<<endl;
		else
		cout<<"Case #"<<kk<<": "<<min(cnt,cnt1)<<endl;
		
		kk++;
	}
}
