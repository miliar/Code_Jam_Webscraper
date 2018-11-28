#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define fbo find_by_order
#define ook order_of_key
#define rep(i,a,b) for(int i=a;i<b;i++)

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef list<int> li;
typedef long double ld; 
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
typedef set<int>::iterator sit;
typedef map<int,int>::iterator mit;
typedef vector<int>::iterator vit;
typedef list<int>::iterator lit;


int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cout.precision(17);
	int t; cin>>t;
	double pi = 3.14159265359;
	rep(o,0,t){
		double ma = -1;
		int n,k; cin>>n>>k;
		ii a[n];
		rep(i,0,n){
			int x,y;
			cin>>x>>y;
			a[i] = ii(x,y);
		}
		sort(a,a+n);
		double b[n];
		rep(j,0,n){
				b[j]=(double)(a[j].se)*a[j].fi;
			}
		rep(i,k-1,n){
			long r = a[i].fi;
			double m = pi*r*r + 2*pi*r*a[i].se;
			sort(b,b+i);
			double f = 0;
			rep(j,0,k-1){
				f += b[i-j-1];
			}
			m += 2*pi*f;
			if(m>ma) ma=m;
			


		}

		cout<<"Case #"<<o+1<<": "<<ma<<endl;
		
	}
}
