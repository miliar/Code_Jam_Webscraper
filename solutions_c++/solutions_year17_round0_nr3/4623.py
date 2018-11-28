#include <bits/stdc++.h>
 
using namespace std;
 
typedef long long ll;
typedef vector<int> vi;
typedef vector<long long> vii;
typedef vector<vector<int> > vvi;
typedef vector<vector<long long> > vvii;

 
#define boost std::ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define FOR(i,a,b) for(i= (a) ; i<(b); ++i)
#define pb push_back
#define mp make_pair
#define all(x) (x).rbegin() , (x).rend()
#define out(x) cout<<x<<"\n"
#define sz(x)  (x).size()
#define nl cout<<"\n"
#define INF 500001
#define F first
#define S second

int main()
{
	int t,tc=1;
	cin>>t;
	while(t--)
	{
		ll n,m,i,j,k,x,y,z;
		cin>>n>>k;
		cout<<"Case #"<<tc++<<": ";
		multiset<ll> s;
		s.insert(n);
		FOR(i,1,k+1)
		{
			if(i==k){
				z = *s.rbegin();
				x = z/2;
				if(z%2 == 0){
					cout<<x<<" ";
					if(x==0)
						cout<<0;
					else
						cout<<x-1;
				}
				else{
					cout<<x<<" "<<x;
				}
				nl;
			}
			else{
				z = *s.rbegin();
				auto itr = s.find(z);
				s.erase(itr);
				if(z%2 == 1){
					if(z/2>0){
						s.insert(z/2);
						s.insert(z/2);
					}
				}
				else{
					if(z/2>0)
						s.insert(z/2);
					if(z/2>1)
						s.insert(z/2-1);
				}
			}
		}
	}
	return 0;
} 