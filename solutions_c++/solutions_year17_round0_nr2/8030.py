#include <bits/stdc++.h>
using namespace std;
void print(string s)
{
	bool start=false;
	for(int i=0;i<s.size();i++)
	{
		if(start)
		{
			cout<<s[i];
			continue;
		}
		if(s[i]=='0'&&i==(s.size()-1))
		{
			cout<<s[i];
		}
		if(s[i]!='0')
		{
			cout<<s[i];
			start=true;
		}
	}
	cout<<endl;
}
int main()
{
	/*
	 *string s="0";
	 *print(s);
	 *s="000";
	 *print(s);
	 *s="009";
	 *print(s);
	 *s="91029";
	 *print(s);
	 */
	int t;
	cin>>t;
	int cnt=1;
	while(t--)
	{
		string s;
		cin>>s;
		int n=s.size();
		cout<<"Case #"<<cnt<<": ";
		cnt++;
		s="0"+s;
		n++;
		for(int i=0;i<n;i++)
		{
			if(s[i]>=s[i-1])
				continue;
			int j=i-1;
			while(j>0)
			{
				if(s[j]>s[j-1])
				{
					break;
				}
				j--;
			}
			s[j]--;
			for(int idx=j+1;idx<n;idx++)
				s[idx]='9';
			break;
		}
		print(s);
	}
	return 0;
}
