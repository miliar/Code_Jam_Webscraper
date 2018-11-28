#include <bits/stdc++.h>
using namespace std;

#define ll long long int
#define ld long double
#define vi vector<int> 
#define ii pair<int,int>
#define vii vector<ii>
#define loop(x,i,a,b) for(x i=a;i<=b;i++)
#define loopi(i,a,b) for(int i=a;i<=b;i++)
#define loop2(i,a,b) for(i=a;i<=b;i++)  
#define rloop(x,i,a,b) for(x i=a;i>=b;i--)
#define rloopi(i,a,b) for(int i=a;i>=b;i--)
#define rloop2(i,a,b) for(i=a;i>=b;i--)  
#define X first
#define Y second 
//#define fill(a,x) memset(a,x,sizeof(a))
#define pb push_back
#define mp make_pair
#define all(v) v.begin(),v.end()
//#define DEBUG
const long double pi = atan(1.0)*4.0;
const ll mod = 1e9+7;
const ll INF = 1e18;
#ifdef DEBUG
#define dout(x) cout<<x;
#define douttb(x) cout<<x<<" ";
#define doutln(x) cout<<x<<endl;
#else
#define dout(x)
#define douttb(x)
#define doutln(x)
#endif
#define N 100001

int main()
{	
	// int n,k,t;
	// cin>>t;
	// loop(int,T,0,t-1){
	// 	cin>>n>>k;
	// 	multiset<int> s;
	// 	s.insert(n);
	// 	loop(int,i,0,k-2){
	// 		auto it = s.end();
	// 		it--;
	// 		int x = *it;
	// 		s.erase(it);
	// 		s.insert((x)/2);
	// 		s.insert(((x)-1)/2);
	// 	}		
	// 	auto it = s.end();
	// 	it--;
	// 	cout<<"Case #"<<T+1<<": "<<(*it)/2<<" "<<(*it-1)/2<<endl;
	// }

	ll n,k,t,tt,x,y;
	cin>>t;
	map<ll,ll> m1;
	loop(ll,T,1,t){
		cin>>n>>k;
		m1.clear();
		m1[n] = 1;
		tt = 0 ;
		while(tt < k){
			auto it = m1.end();
			it--;
			x = it->X;
			y = it->Y;
			m1.erase(it);
			m1[x/2] += y;
			m1[(x-1)/2] += y;
			tt += y;
		}
		cout<<"Case #"<<T<<": "<<(x)/2<<" "<<(x-1)/2<<endl;
	}

	return 0;	
}
