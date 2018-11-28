#include<bits/stdc++.h>
using namespace std;

string reverse(string s,int l,int r)
{
	for(int i=l;i<=r;i++)
	{
		if(s[i]=='-')
			s[i]='+';
		else
			s[i]='-';
	}
	return s;
}

int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int t;
	cin>>t;
	int j=1;
	while(t--)
	{
		string s;
		int k;
		cin>>s>>k;
		
		int n = s.length();
		int i,count=0;
		for(i=0;i+k-1<n;i++)
		{
			if(s[i]=='-')
			{
				s=reverse(s,i,i+k-1);
				count++;
			}
		}
		
		for(;i<n;i++)
		{
			if(s[i]!='+')
			break;
		}
		
		if(i>=n)
		cout << "Case #" << j << ": " << count << endl;
		else
		cout << "Case #" << j << ": " << "IMPOSSIBLE" << endl;
		j++;
	}
return 0;
}
