#include<bits/stdc++.h>
 
#define MOD 	1000000007
#define ll 		long long
#define	inf		1e12
#define MAX		10000000
#define pii		pair<int, int>
#define F 		first
#define S 		second
 
using namespace std;



int main()
{
	
	int t, n;
	string s;
	cin>>t;
	for(int test=1;test<=t;test++)
	{
		cin>>s;
		n = (int)s.length();
		for(int j = n-1;j>0;j--)
		{
			if(s[j]<s[j-1])
			{
				if(s[j-1] == '0')
					s[j-1] = '9';
				else s[j-1]--;
				for(int k=j;k<n;k++)
				{
					s[k] = '9';
				}
			}
		}
		cout<<"Case #"<<test<<": ";
		for(int i=0;i<n;i++)
		{
			if(i==0 && s[i] != '0')
				cout<<s[i];
			else if(i!=0) cout<<s[i];

		}
		if(test!=t)
			cout<<endl;
	}
	return 0;
}