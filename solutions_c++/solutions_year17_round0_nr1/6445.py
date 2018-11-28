#include <bits/stdc++.h>
using namespace std;

#define ll long long int

int main()
{
	ifstream myfile;
	ofstream printFile;
	myfile.open("A-large.in");
	printFile.open("largeA.txt");
	ll t;
	myfile>>t;
	ll cas=0;
	while(t--)
	{
		cas++;
		ll k;
		string ss;
		myfile>>ss>>k;
		ll c=0;
		ll br=0;
		ll n = ss.length();

		for(ll i=0;i<n;i++)
		{
			if(ss[i] == '-')
			{
				for(ll j=i;j<(i+k);j++)
				{
					if(j<n)
						ss[j]=(ss[j]=='-')?'+':'-';
					else
					{
						br=1;
						break;
					}
				}
				c++;
				if(br == 1)
					break;
			}
		}
		if(br == 1)
		{
			printFile<<"Case #"<<cas<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			printFile<<"Case #"<<cas<<": "<<c<<endl;
		}
	}
	printFile.close();
}