
#include <bits/stdc++.h>
typedef long long int lli;
using namespace std;

void printQ( queue<int> q )
{
	cout<<"Q : ";
	while ( q.empty() == false )
	{
		cout<<q.front()<<" ";
		q.pop();
	}
	cout<<"\n";
}

int main()
{
	int T; cin>>T;
	string s; int sl;
	int k;
	
	for ( int S=1 ; S<=T ; S++ )
	{
		cin>>s>>k;
		sl = s.length();
		
		bool ok = true;
		queue<int> q;
		int ans = 0;
		for ( int i=0 ; i<sl ; i++ )
		{
			while ( q.size() && q.front() < i-k+1 )
				q.pop();
			
			// cout<<i<<" ";	
			// printQ( q );
				
			int qs = q.size();
			if ( qs % 2 )
			{
				s[i] = (s[i]=='+') ? '-' : '+';
			}
			
			if ( s[i] == '-' && i < sl-k+1 )
			{
				s[i] = '+';
				q.push( i );
				ans++;
			}
			
			ok &= s[i]=='+';
		}
		
		cout<<"Case #"<<S<<": ";
		if ( ok == false ) cout<<"IMPOSSIBLE\n";
		else cout<<ans<<"\n";
	}
	
	return 0;
}
