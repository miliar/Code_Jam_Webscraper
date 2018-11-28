#include<iostream>
using namespace std;
int main()
{
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(false);
	int t,x=0;
	cin>>t;
	while(t--)
	{
		long long ans=0;
		string s;
		int a[20],b[20],temp;
		x++;
		cin>>s;
		temp=s.size();
		for(int i=0;i<s.size();i++)
			a[i]=s[i]-48;
		b[0]=a[0];
		for(int i=1;i<s.size();i++)
		{
			if(a[i]>=a[i-1])
				b[i]=a[i];
			else
			{
				b[i-1]--;
				temp=i;
				break;
			}	
		}
		for(int i=temp;i<s.size();i++)
			b[i]=9;
		for(int i=s.size()-1;i>0;i--)
		{
			if(b[i]<b[i-1])
			{
				b[i]=9;
				b[i-1]--;
			}
		}	
		for(int i=0;i<s.size();i++)
			ans=ans*10+b[i];
		cout<<"Case #"<<x<<": "<<ans<<"\n";		
	}
}
