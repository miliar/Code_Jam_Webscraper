#include<bits/stdc++.h>
using namespace std;
int t,k,j;
int y=1;
int main()
{
	freopen ("A-large2.in","r",stdin);
	freopen ("out10.txt","w",stdout);
	
	
	cin>>t;
	string s;
	while(t--)
	{
		cin>>s>>k;
		int l=s.size();
		vector<string>ty(l);
		int i;
		for(i=0;i<l;i++)
			ty[i]=s[i];
		int flaging=0;
		int counting=0;
		for(i=0;i<l;i++)
		{
			if(ty[i]=="+")
				continue;
			else if(ty[i]=="-" && i+k<=l)
			{
				for(j=0;j<k;j++)
				{
					if(ty[i+j]=="+")
						ty[i+j]="-";
					else
						ty[i+j]="+";
					
				}
				counting++;
			}
			else if(ty[i]=="-" && i+k>l)
			{
				flaging=1;
			}
			// for(j=0;j<l;j++)
			// 	cout<<v[j];
			// cout<<endl;
		}
		if (flaging==1)
			cout<<"Case #"<<y<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<y<<": "<<counting<<endl;
		y++;

	}
}
