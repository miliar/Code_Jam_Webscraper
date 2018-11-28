/* In the Name of God */
#include <bits/stdc++.h> 
#define F first
#define S second
#define mod 1000000007

using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 100000+10;

ofstream fout("out.out");


int main()
{
	int t ;
	cin>>t;
	for(int tt = 1 ; tt <= t ; tt ++ )
	{
		
		ll ans = 0 ;
		string s ;
		cin>>s;
		for(int j = s.size() -1 ; j >0 ; j -- )
			if(s[j] < s[j-1] )
			{
				for( int i = j ; i <s.size() ; i ++ )
					s[i] = '9';
				s[j-1]--;

			}

		for(int i = 0 ; i < s.size() ; i ++ )
		 	ans = ans*10+(s[i] - '0');	
		
		fout<<"Case #"<<tt<<": ";
		fout<<ans<<endl;
	}
}	
