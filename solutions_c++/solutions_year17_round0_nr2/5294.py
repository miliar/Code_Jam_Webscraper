#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t; cin>>t;
	for(int k=1; k<=t; ++k)
	{
		cout<<"Case #"<<k<<": ";
		string n; cin>>n;
		while(true)
		{
			bool ok = true;
			for(int i=1; i<n.size(); ++i)
			{
				if(n[i]<n[i-1])
				{
					n[i-1]--;
					for(int j=i; j<n.size(); ++j) n[j] = '9';
					ok = false;
					break;
				}
			}
			if(ok) break;
		}
		for(int i=0; i<n.size(); ++i) if(n[i]!='0') cout<<n[i];
		cout<<"\n";
	}
	return 0;
}
