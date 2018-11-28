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
		
		string s ;
		int k , ans = 0  ;
		cin>>s>>k ;

		for( int i = 0 ; i <= s.size()-k ; i ++ )
			if(s[i]=='-')
			{
				for(int j = i ; j < i+k; j ++ )
				{
					if(s[j] == '-')
						s[j] = '+';
					else
						s[j] = '-';
				}
				ans ++ ;
			}
		int check = 0 ;
		for( int i = 0 ; i  < s.size() ; i ++ )
			if(s[i] == '-')
			{
				check = 1 ;
				break ;
			}

		fout<<"Case #"<<tt<<": ";
		if(check == 1)
			fout<<"IMPOSSIBLE"<<endl;
		else
			forout<<ans<<endl;
	}
}	
