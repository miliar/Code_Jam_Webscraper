#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen ("A-large.in","r",stdin);
	freopen ("out2.txt","w",stdout);
	int t,k,j;
	int h=1;
	cin>>t;
	string s;
	while(t--)
	{
		cin>>s>>k;
		int l=s.size();
		vector<string>v(l);
		int i;
		for(i=0;i<l;i++)
			v[i]=s[i];
		int flag=0;
		int count=0;
		for(i=0;i<l;i++)
		{
			if(v[i]=="+")
				continue;
			else if(v[i]=="-" && i+k<=l)
			{
				for(j=0;j<k;j++)
				{
					if(v[i+j]=="+")
						v[i+j]="-";
					else
						v[i+j]="+";
					
				}
				count++;
			}
			else if(v[i]=="-" && i+k>l)
			{
				flag=1;
			}
			// for(j=0;j<l;j++)
			// 	cout<<v[j];
			// cout<<endl;
		}
		if (flag==1)
			cout<<"Case #"<<h<<": "<<"IMPOSSIBLE"<<endl;
		else
			cout<<"Case #"<<h<<": "<<count<<endl;
		h++;

	}
}