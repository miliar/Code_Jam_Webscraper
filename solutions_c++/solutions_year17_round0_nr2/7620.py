#include <bits/stdc++.h>
using namespace std;

int main(int argc, char const *argv[])
{
	int t;
	cin>>t;
	int p=1;
	while(t--)
	{
		string n;
		cin>>n;
		for(int i=n.length()-2;i>=0;i--)
		{
			if(n[i]>n[i+1])
			{
				n[i] = (char)((int)n[i]-1);
				for(int j=i+1;j<n.length();j++)
					n[j]='9';
			}
		}
		int k=0;
		while(n[k]=='0')
			k++;
		cout<<"Case #"<<p<<": ";
		for(;k<n.length();k++)
			cout<<n[k];
		cout<<"\n";
		p++;
	}
	return 0;
}