#include<iostream>
#include<string>
#include<fstream>
#include<bits/stdc++.h>

using namespace std;


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
//		unsigned long int x=0;
		string n,m;
		cin>>n;
		int k=strlen(n.c_str());
		if(k!=1)
		{
			int x=0,y=1;
			while(x<k && y<k)
			{
				if(n[x]<n[y])
				{
					x=y;
					y++;
				}
				else if(n[x]==n[y])
					y++;
				else
					break;
			}
			if(y!=k)
			{n[x]-=1;
			for(int j=x+1;j<k;j++)
				n[j]='9';
			}
		}
		while(n[0]=='0') n.erase(n.begin());
//		ofstream ofile("output.txt");
		cout<<"Case #"<<i<<": "<<n<<"\n";
	}
}
