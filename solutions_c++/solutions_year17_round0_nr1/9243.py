#include<iostream>
using namespace std;

int check(string s, int k)
{
	int length = s.length();
	int count = 0;
	for(int i=0;i<=length-k;i++)
	{
		if(s[i]=='-')
		{
			count++;
			for(int j=0;j<k;j++)
			{
				s[i+j] = (s[i+j]=='+') ? '-' : '+';
			}
		}
	}
	for(int i=0;i<k;i++)
	{
		if(s[length-k+i+1]=='-') return -1;
	}
	return count;
}
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-small-output.txt", "w", stdout);
	
	int t,k;
	string s;
	cin>>t;
	int count =0;
	while(t--)
	{
		count++;
		cin>>s;
		cin>>k;
		int p = check(s,k);
		cout<<"Case #"<<count<<": ";
		if(p==-1) cout<<"IMPOSSIBLE"<<endl;
		else cout<<p<<endl;
	}
	return 0;
}
