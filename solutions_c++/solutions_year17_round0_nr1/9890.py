#include<bits/stdc++.h>


using namespace std;

void flip(string &s,int st,int k)
{
	for(int i=st;i<st+k;i++)
	{
		if(s[i] == '+')
		s[i] = '-';
		else s[i] = '+';
	}
}

bool ifpossible(string &s,int k)
{
	int cnt1= 0,cnt2 = 0;

	for(int i=s.length() - k;i<s.length();i++)
	{
		if(s[i] == '-')
		return false;
	}

	return true;

}

int main()
{
	int t,k,cs = 1;

	cin>>t;

	while(t--)
	{
		string s;
		cin>>s>>k;

		int result = 0,f = 0;

		if(k > s.length())
		cout<<"Case #"<<cs<<": IMPOSSIBLE"<<"\n";
		else
		{
			for(int i=0;i<=s.length()-k;i++)
			{

				if(s[i] == '-')
				{
					flip(s,i,k);
					//cout<<s<<" "<<f<<"\n";
					result++;
				}
			}

			if(!ifpossible(s,k))
			cout<<"Case #"<<cs<<": IMPOSSIBLE"<<"\n";
			else cout<<"Case #"<<cs<<": "<<result<<"\n";

		}

		cs++;
	}
}
				
