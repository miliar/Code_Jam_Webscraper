#include <bits/stdc++.h>
using namespace std;

#define lli long long int

int i, j, k, t, n, flips=0, cases=0;
int a[1009];
string s;
bool possible;


int main()
{
	cin>>t;
	while(t--)
	{
		cin>>s;
		cin>>k;

		for(i=0;i<s.length();i++)
			a[i]=s[i]=='+'?1:0;

		n=s.length();
		flips=0;
		possible=true;

		for(i=0;i<n-k+1;i++)
		{
			if(a[i]==0)
			{
				flips++;
				for(j=i;j<i+k;j++)
					a[j]=1-a[j];
			}
		}
		for(i=0;i<n;i++)
		{
			if(a[i]!=1)
			{
				cout<<"Case #"<<++cases<<": IMPOSSIBLE"<<endl;
				possible=false;
				break;
			}
		}
		if(possible)
			cout<<"Case #"<<++cases<<": "<<flips<<endl;
	}
	return 0;
}