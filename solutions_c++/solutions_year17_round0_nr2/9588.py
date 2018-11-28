
#include <bits/stdc++.h>
typedef long long int lli;
using namespace std;

int main()
{
	int T; cin>>T;
	for ( int S=1 ; S<=T ; S++ )
	{
		string s; cin>>s;
		int sl = s.length();
		
		int i=1;
		for ( ; i<sl ; i++ )
			if ( s[i] < s[i-1] )
				break;
		
		if ( i < sl )
		{
			int j;
			
			for ( j=i ; j<sl ; j++ )
				s[j] = '9';
			
			char x = s[i-1];
			for ( j=i-1 ; j>=0 && s[j]==x ; j-- )
				s[j]--;
			
			if ( j == -1 )
				for ( j=1 ; j<i ; j++ )
					s[j] = '9';
		}
		
		i = 0;
		while ( i<sl && s[i] == '0' ) i++;
		
		cout<<"Case #"<<S<<": ";
		while ( i<sl ) cout<<s[i++];
		cout<<"\n";
	}
	
	return 0;
}
