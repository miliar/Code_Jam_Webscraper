#include <bits/stdc++.h>

using namespace std;

int main()
{
	int i,j,min,ind,t,st;
	string s;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>s;
		min = s[s.size()-1];
		ind = s.size();
		for(j=s.size()-1;j>=0;j--)
		{
			if(s[j]>min)
			{
				if(s[j] == '0')
				{
					while(s[j]=='0')
					{
						s[j] = '9';
						j--;
					}	
					s[j]--;
				}
				else
					s[j]--;
				min = s[j];
				ind = j+1;
			}
			else
				min = s[j];
		}
		for(j=ind;j<s.size();j++)
			s[j] = '9';
		st = 0;
		if(s[0] == '0')
			st = 1;
		cout<<"Case #"<<i+1<<": "; 
		for(j=st;j<s.size();j++)
			cout<<s[j];
		cout<<"\n";
	}
	return 0;
}