#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("op.txt", "w", stdout);
	long long T,t,i,j,n,k,ar[1002];
	string s;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		bool res=true;
		long long cnt = 0;
		cin>>s>>k;
		for(i=0;i<s.size();i++)
		{
			if(s[i] == '+')
			{
				ar[i]=1;
				continue;
			}
			ar[i]=0;
		}

		for(i=0;i<=s.size()-k;i++)
		{
			if(!ar[i])
			{

				cnt++;
				for(j=0;j<k;j++)
				{
					ar[i+j]=!ar[i+j];
					
				}
			}
		}
		for(i=0;i<s.size();i++)
			if(!ar[i])
			{
				res=false;
				break;
			}
		if(!res)
			cout<<"Case #"<<t<<": IMPOSSIBLE\n";
		else
			cout<<"Case #"<<t<<": "<<cnt<<"\n";
	}
}