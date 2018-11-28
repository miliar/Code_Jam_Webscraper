#include <bits/stdc++.h>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin>>t;
	for(int j=0;j<t;j++)
	{
		string n;
		int w;
		cin>>n>>w;
		int l=strlen(n.c_str());
		int li=-w-1;
		int mov=0,all=1;
		vector<int >x;
		for(int i=0;i<l;i++)
		{
			if(n[i]=='-')	all=0;
			int s=x.size()-1,c=0;
			while(s>=0)
			{
				if(i-x[s]>=w)
					break;
				c++;
				s--;
			}
			if(c%2==1)
			{
				if(n[i]=='-')	n[i]='+';
				else			n[i]='-';
			}
			if(n[i]=='-')
			{
				mov++;
				li=i;
				x.push_back(i);
			}
		}
		cout<<"Case #"<<j+1<<": ";

		if(all==1)
			cout<<"0\n";
		else if(li<=l-w)
			cout<<mov<<"\n";
		else	cout<<"IMPOSSIBLE\n";
	}

	return 0;
}
