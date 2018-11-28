#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define ull unsigned long long int
int main()
{

	//freopen("input1.txt","r",stdin);
	..freopen("output1.txt","w",stdout);
	int t,ii=1;
	cin>>t;
	while(ii<=t)
	{
		string s;
		ll k,ctr=0;
		cin>>s;
		cin>>k;
		int flag=0;
		for(ll i=s.size()-1; i>=0; i--)
		{
			if(s.at(i)=='-')
			{
				ll range=i-(k-1);
				ctr++;
				if(range>=0)
				{
					for(ll j=range; j<=i; j++)
					{
						if(s[j]=='-')
							s[j]='+';
						else
							s[j]='-';
					}
				}
				else
				{
					flag=1;
					break;
				}

			}
		}
		if(flag==0)
			cout<<"Case #"<<ii<<": "<<ctr<<endl;
		else
			cout<<"Case #"<<ii<<": IMPOSSIBLE"<<endl;
		ii++;

	}
	return 0;


}
