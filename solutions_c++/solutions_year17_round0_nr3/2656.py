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

map<ll , ll >m;
set<ll>s;
set<ll>::iterator it;


int main()
{
	int t ;
	cin>>t;
	for(int tt = 1 ; tt <= t ; tt ++ )
	{
		ll n , k ;
		cin>>n>>k;
		
		s.clear();
		m.clear();

		m[n] = 1 ;
		s.insert(n);
		
		ll ans1 , ans2;
		

		while(k > 0)
		{
			it = s.end();
			--it;
			ll num = *it;
			s.erase(num);
			s.insert( (num-1)/2 );
			s.insert( (num)/2 );
			m[ num / 2 ]+=m[num];
			m[ (num-1)/2 ]+=m[num];
			k-=m[num];
			ans1 = num/2;
			ans2=(num-1)/2;

		}

		fout<<"Case #"<<tt<<": ";
		fout<<ans1<<" "<<ans2<<endl;
	}
}	
