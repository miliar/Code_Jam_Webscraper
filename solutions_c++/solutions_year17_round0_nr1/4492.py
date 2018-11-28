#include <bits/stdc++.h>
 
using namespace std;
 
#define FOR(i,a,b) for(i= (a) ; i<(b); ++i)
#define out(x) cout<<x<<"\n"
 
int main()
{
	int t,tc=1;
	cin>>t;
	while(t--)
	{
		int n,i,j,k,x,y,z;
		string s; cin>>s;
		cin>>k;
		n = s.length();
		z = 0;
		FOR(i,0,n-k+1)
		{
			if(s[i]=='-'){
				z++;
				FOR(j,i,i+k)
				{
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
		}
		bool ok = 1;
		FOR(i,0,n)
		{
			if(s[i]=='-'){
				ok = 0; break;
			}
		}
		cout<<"Case #"<<tc++<<": ";
		if(!ok) out("IMPOSSIBLE");
		else out(z);
	}
	return 0;
} 