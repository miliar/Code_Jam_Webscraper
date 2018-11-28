#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);	
	int t;
	cin>>t;
	for(int y=1;y<=t;y++)
	{
		vector<int> v;
		string s;
	    cin>>s;
		int len=(int)s.length();
		for(int j=0;j<len;j++)
		{
			v.push_back((int)(s[j])-48);
		}
		
		int i=0,maxm=v[0];
		
		for(int z=1;z<len;z++)
		{
			if(maxm<v[z])
				{
					i=z;
					maxm=v[z];
				}
			else if(maxm>v[z])
				{
					v[i]--;
					i++;
					for(int k=i;k<len;k++)
					v[k]=9;
					break;
				}
		}
		cout<<"Case #"<<y<<": ";
		for(int x=0;x<len;x++)
		{
			if(v[x]!=0)
				cout<<v[x];
		}
		cout<<'\n';
	}
	return 0;
}