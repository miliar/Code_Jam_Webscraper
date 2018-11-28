#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false),cin.tie(0);

	int tt;
	cin>>tt;
	for (int ti=1; ti<=tt; ti++)
	{
		int res=0;
		string s;
		int n,k;
		cin>>s; n = s.length();
		for (int i=0; i<n; i++)
			s[i] = (s[i]=='+');
		cin>>k;
		
		for (int i=0; i+k-1<n; i++)
			if (s[i]==0 && ++res)
				for (int j=0; j<k; j++)
					s[i+j]=1-s[i+j];
		 
		for (int i=0; i<n; i++)
			if (!s[i]) res=-1;
	
		cerr<<"Case Done "<<ti<<'\n';
		cout<<"Case #"<<ti<<": ";
		if (res==-1)
			cout<<"IMPOSSIBLE";
		else cout<<res;
		cout<<'\n';
	}
	
    return 0;
}
