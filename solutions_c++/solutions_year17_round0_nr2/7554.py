#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int m=1;
	while(t--)
	{
		string st;
		cin>>st;
		int n = st.size();
		int i;
		int on = 0;
		int in = 0;
		for(i=0;i<n;i++)
		{
			if(st[i]=='1')
				in++;
			if(st[i]=='0')
				on++;
		}
		if(on==1 and in==n-1)
		{
			st[0]='0';
			for(i=1;i<n;i++)
				st[i]='9';
		}
		else {
			for(i=0;i<n-1;i++)
			{
				if(st[i]>st[i+1])
				{
					int yt = st[i];
					st[i] = st[i]-1;
					for(int j = i+1;j<n;j++)
					{
						st[j] = '9';
					}
					for(int j = 0;j<i;j++)
					{
						if(st[j]>st[i])
						{
							st[j] = st[i];
							for(int k = j+1;k<n;k++)
								st[k] = '9';
							break;
						}
					}
				}
			}
		}
		i=0;
		cout<<"Case #"<<m<<": ";
		while(st[i]=='0')
			i++;
		for(;i<n;i++)
		{
			cout<<st[i];
		}
		cout<<endl;
		m++;
	}
	return 0;
}
