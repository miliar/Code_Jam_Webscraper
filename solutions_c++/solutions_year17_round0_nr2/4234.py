#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("ggl.txt","w",stdout);
	int t,kk=0;
	cin>>t;
	while(t--)
	{
		int isd=0;
		string s,x;
		cin>>s;
		int n=s.size();
		int temp=n-1;
		for(int i=n-1;i>0;i--)
		{
			if(s[i-1]>s[i])
			{
				
				s[i-1]=s[i-1]-1;
				for(int j=temp;j>=i;j--)
				{
					s[j]='9';	
				}
				temp=i-1;
			}
		}
		int cntt=0;
		for(int i=0;i<n;i++)
		{
			if(s[i]!='0')
			break;
			cntt++;
		}
		//cout<<cntt<<endl;
		x=s.substr(cntt,n-cntt);
		kk++;
		cout<<"Case #"<<kk<<": "<<x<<endl;
	}
}
