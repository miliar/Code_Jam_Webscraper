#include<bits/stdc++.h>
using namespace std;
#define lli long long
#define mod 1000000007
#define inf 1000000007
#define pb push_back
#define ppb pop_back
#define mp make_pair
#define fs first
#define sc second
#define lim 200007

int t, n, m;

int main(){
	freopen("file.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>t;
	int l, k, ans, c = 0;
	bool over;
	string tmp, s;
	while( c++ < t )
	{
		cin>>s>>k;
		tmp = s;
		l = s.length();
		ans = 0;
		for( int i = 0; i <= l - k; i++ )
		{
			if( s[i] == '-' )
			{
				for( int j = 0; j < k; j++ )
					s[j+i] = ( s[j+i] == '-' ) ? '+' : '-';
				ans++;
				//cout<<i<<" "<<s<<endl;
			}
		}
		over = 1;
		for( int i = 0; i < l; i++ )
		{
			if( s[i] == '-' )
			{
				over = 0;
				break;	
			}
		}
		cout<<"Case #"<<c<<": ";
		if(over == 1)
			cout<<ans<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
